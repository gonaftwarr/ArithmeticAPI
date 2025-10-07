import hashlib
import time
import subprocess
import os

# ----------------------------
# CONFIGURATION
# ----------------------------
WATCH_FILE = "app.py"                  # File to monitor
DOCKER_IMAGE = "gonaft/myapp"          # Docker Hub repo
CONTAINER_NAME = "myapp_container"     # Custom container name
CHECK_INTERVAL = 5                     # Seconds between checks
# ----------------------------


def file_hash(filename):
    """Return SHA-256 hash of the file contents."""
    try:
        with open(filename, "rb") as f:
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        return None


def get_latest_commit_hash():
    """Return the latest Git commit hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, encoding="utf-8", errors="ignore"
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except Exception:
        return None


def rebuild_and_push(trigger_source):
    """Rebuild, push Docker image, and restart the container."""
    print(f"[+] Change detected from {trigger_source}! Rebuilding Docker image...")

    # Rebuild the Docker image
    build = subprocess.run(
        ["docker", "build", "-t", DOCKER_IMAGE, "."],
        text=True, encoding="utf-8", errors="ignore"
    )
    if build.returncode != 0:
        print("[x] Build failed!")
        return

    print("[✓] Build successful. Pushing to Docker Hub...")
    push = subprocess.run(
        ["docker", "push", f"{DOCKER_IMAGE}:latest"],
        text=True, encoding="utf-8", errors="ignore"
    )
    if push.returncode != 0:
        print("[x] Push failed!")
        return

    print("[✓] Push successful! Restarting container with new image...")

    # Stop and remove existing container
    subprocess.run(["docker", "stop", CONTAINER_NAME], text=True, encoding="utf-8", errors="ignore")
    subprocess.run(["docker", "rm", CONTAINER_NAME], text=True, encoding="utf-8", errors="ignore")

    # Run new container version
    run = subprocess.run([
        "docker", "run", "-d",
        "--name", CONTAINER_NAME,
        "-p", "5000:5000",
        DOCKER_IMAGE
    ], text=True, encoding="utf-8", errors="ignore")

    if run.returncode == 0:
        print("[🚀] Container restarted successfully! Your API is now live at http://127.0.0.1:5000\n")
    else:
        print("[x] Failed to restart container!")


def main():
    print(f"[*] Monitoring {WATCH_FILE} and Git commits every {CHECK_INTERVAL} seconds.")
    last_file_hash = file_hash(WATCH_FILE)
    last_commit_hash = get_latest_commit_hash()

    if last_file_hash is None:
        print(f"[x] Error: {WATCH_FILE} not found!")
        return
    if last_commit_hash is None:
        print("[x] Warning: Could not read Git commit hash. Make sure this folder is a Git repo.")

    while True:
        time.sleep(CHECK_INTERVAL)

        # Check for local file changes
        current_file_hash = file_hash(WATCH_FILE)
        if current_file_hash and current_file_hash != last_file_hash:
            rebuild_and_push("local file change")
            last_file_hash = current_file_hash

        # Check for new Git commits
        current_commit_hash = get_latest_commit_hash()
        if current_commit_hash and current_commit_hash != last_commit_hash:
            rebuild_and_push("new Git commit")
            last_commit_hash = current_commit_hash


if __name__ == "__main__":
    main()

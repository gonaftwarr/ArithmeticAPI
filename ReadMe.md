# Arithmetic API – Automated Docker and GitHub Deployment

This project is a simple Flask API that automatically rebuilds and redeploys its Docker image whenever the code changes locally or a new commit is pushed to GitHub.

---

## Requirements

- Python 3.12+
- Flask (installed from requirements.txt)
- Docker Desktop (latest version)
- PyCharm with Docker and GitHub integration plugins enabled
- A GitHub account (for version control)
- A Docker Hub account (for storing the built image)

---

## What the Project Does

1. A Flask API (`app.py`) provides basic routes for arithmetic operations and a `/test` route for rebuild testing.
2. A Python script (`monitor.py`) constantly watches the project for:
   - local code changes  
   - new Git commits  
3. When a change or commit is detected, it:
   - rebuilds the Docker image  
   - pushes it to Docker Hub  
   - restarts the running container automatically  

This creates a local mini CI/CD pipeline — everything updates on its own after code edits or commits.

---

## How to Set Up and Run

1. **Clone or open the project in PyCharm.**

2. **Create and activate the virtual environment** (PyCharm does this automatically when you open the project).

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Open Docker Desktop**

Make sure it’s running before continuing.


5. **Build the Docker image manually the first time:**

```bash
docker build -t gonaft/myapp .
```

6. **Run the container manually once:**

```bash
docker run -p 5000:5000 --name vigilant_panini gonaft/myapp
```
The app should now be available at:
http://127.0.0.1:5000


7. **Run the monitor script:**

```bash
python monitor.py
```
It will now watch for any code changes or Git commits.


8. **Test automatic updates:**

- Edit app.py and save (for example, add or delete or modify the /test route).

- Or make a commit and push to GitHub.

- The terminal will show that the Docker image was rebuilt and pushed.

- Your container will restart automatically.


9. **Verify the update:**

Visit (if u added the '/test' route in app.py):

http://127.0.0.1:5000/test

If you see your new message, the rebuild worked.









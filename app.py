from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route (home page)
@app.route('/')
def home():
    return "Welcome to the Arithmetic API!"



# Addition route
@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 + num2})
    except Exception as e:
        return jsonify({"error": str(e)})

# Subtraction route
@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 - num2})
    except Exception as e:
        return jsonify({"error": str(e)})

# Multiplication route
@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 * num2})
    except Exception as e:
        return jsonify({"error": str(e)})


# Division route
@app.route('/divide', methods=['GET'])
def divide():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"})
        return jsonify({"result": num1 / num2})
    except Exception as e:
        return jsonify({"error": str(e)})


# ✅ Test endpoint to confirm rebuild worked
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "This is a test endpoint — rebuild successful!"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

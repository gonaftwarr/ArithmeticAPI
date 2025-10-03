from flask import Flask, request, jsonify

app = Flask(__name__)

# Addition
@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 + num2})
    except Exception as e:
        return jsonify({"error": str(e)})

# Subtraction
@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 - num2})
    except Exception as e:
        return jsonify({"error": str(e)})

# Multiplication
@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({"result": num1 * num2})
    except Exception as e:
        return jsonify({"error": str(e)})

# Division
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

if __name__ == '__main__':
    app.run(debug=True)


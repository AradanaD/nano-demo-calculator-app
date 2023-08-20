from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "Welcome to the Calculator API!", 200

@app.route("/add", methods=['POST'])
def add():
    try:
        data = request.get_json()
        first = data.get('first')
        second = data.get('second')

        if first is None or second is None:
            return jsonify({"error": "Missing 'first' or 'second' parameter"}), 400

        result = first + second
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/subtract", methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        first = data.get('first')
        second = data.get('second')

        if first is None or second is None:
            return jsonify({"error": "Missing 'first' or 'second' parameter"}), 400

        result = first - second
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')



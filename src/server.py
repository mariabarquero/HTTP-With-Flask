from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"response": "If you want to see my name write /name or /lastname"})

@app.route('/name', methods=['GET'])
def my_name():
    return jsonify({"response": "Maria Jose"})

@app.route('/lastname', methods=['GET'])
def my_lastname():
    return jsonify({"response": "Barquero"})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)

    
# add_numbers.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

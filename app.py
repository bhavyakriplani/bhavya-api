from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sayHello')
def say_hello():
    return jsonify({
        "message": "Hello User"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


from flask import Flask, render_template, request, jsonify
from scanner import scan_network
from sql_security import setup_database, vulnerable_login, secure_login

app = Flask(__name__)

# Create the local SQL demonstration database
setup_database()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')

    if not target:
        return jsonify({"error": "Please enter an IP address or domain."})

    results = scan_network(target)
    return jsonify(results)


@app.route('/sql-test', methods=['POST'])
def sql_test():
    data = request.json

    username = data.get('username', '')
    password = data.get('password', '')

    vulnerable_result = vulnerable_login(username, password)
    secure_result = secure_login(username, password)

    return jsonify({
        "vulnerable_login": bool(vulnerable_result),
        "secure_login": bool(secure_result)
    })


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from scanner import scan_network

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.json.get('target')
    results = scan_network(target)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
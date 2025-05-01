from flask import Flask, render_template, request, jsonify
from encryption import encrypt_message, decrypt_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    encrypted_msg = encrypt_message(data['message'])
    return jsonify({"encrypted": encrypted_msg})

@app.route('/decrypt_message', methods=['POST'])
def decrypt_message_api():
    data = request.json
    decrypted_msg = decrypt_message(data['encrypted'])
    return jsonify({"decrypted": decrypted_msg})

if __name__ == "__main__":
    app.run(debug=True)

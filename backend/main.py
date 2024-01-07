# from flask import Flask, request, jsonify, session
# from flask_cors import CORS
# import StepAndRool as sar

# app = Flask(__name__)
# CORS(app, origins="https://tic-tac-toe-front-4a0m.onrender.com")
# # CORS(app, origins="http://localhost:5173")

# # app.secret_key = 'your_secret_key'

# @app.route('/api/data', methods=['POST'])
# def post_data():
#     data = request.get_json()
#     squares = data.get('squares', [])
#     vsAI = data.get('vsAI')

#     nested_array = [squares[i:i+3] for i in range(0, 9, 3)]
#     squares = nested_array

#     result = sar.make_step(squares, vsAI)

#     if sar.win(squares) is False:
#         return jsonify({"squares":squares , "win": False})
#     else:
#         result = sar.win(squares)
#         return jsonify({"squares":squares , "win": result})


# if __name__ == '__main__':
#     app.run(debug=True, port=5001)



import os
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import StepAndRool as sar
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, origins="https://tic-tac-toe-front-4a0m.onrender.com")

secret_key = bytes(os.getenv('SECRET_KEY'), 'utf-8')

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    encrypted_data = data.get('encryptedData')

    cipher = AES.new(secret_key, AES.MODE_CBC)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)

    decrypted_json = json.loads(decrypted_data.decode('utf-8'))

    squares = decrypted_json.get('squares', [])
    vsAI = decrypted_json.get('vsAI')

    nested_array = [squares[i:i+3] for i in range(0, 9, 3)]
    squares = nested_array

    result = sar.make_step(squares, vsAI)

    if sar.win(squares) is False:
        return jsonify({"squares":squares , "win": False})
    else:
        result = sar.win(squares)
        return jsonify({"squares":squares , "win": result})


if __name__ == '__main__':
    app.run(debug=True, port=5001)

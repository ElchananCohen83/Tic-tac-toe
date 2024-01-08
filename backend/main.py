from flask import Flask, request, jsonify, session
from flask_cors import CORS
import StepAndRool as sar

app = Flask(__name__)
CORS(app, origins="https://tic-tac-toe-front-4a0m.onrender.com")
# CORS(app, origins="http://localhost:5173")

# app.secret_key = 'your_secret_key'

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    squares = data.get('squares', [])
    vsAI = data.get('vsAI')

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



# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import StepAndRool as sar
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# import base64
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# CORS(app, origins="http://localhost:5173")

# @app.route('/api/data', methods=['POST'])
# def post_data():
#     data = request.get_json()

# def decrypt_data(encrypted_data, secret_key):
#     # Convert the base64-encoded string to bytes
#     encrypted_bytes = base64.b64decode(encrypted_data)

#     # Create an AES cipher object with the provided secret key and mode
#     cipher = AES.new(secret_key, AES.MODE_CBC)

#     # Decrypt the data and unpad it using PKCS7 padding
#     decrypted_data = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)

#     # Convert the bytes to a string and return
#     return decrypted_data.decode('utf-8')
    

#     secret_key = bytes(os.getenv('SECRET_KEY'), 'utf-8')
#     encrypted_data = data['data']
#     print("decrypt_data", decrypt_data(encrypted_data, secret_key))


#     squares =[1,2,3,4,5,6,7,7,8,] #data.get('squares', [])
#     vsAI = 2 #data.get('vsAI')

#     nested_array = [squares[i:i+3] for i in range(0, 9, 3)]
#     squares = nested_array

#     result = sar.make_step(squares, vsAI)
#     if sar.win(squares) is False:
#         return jsonify({"squares": squares, "win": False})
#     else:
#         result = sar.win(squares)
#         return jsonify({"squares": squares, "win": result})


# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
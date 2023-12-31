from flask import Flask, request, jsonify
from flask_cors import CORS
import StepAndRool as sar

app = Flask(__name__)
CORS(app, origins=["https://tic-tac-toe-front-4a0m.onrender.com"], supports_credentials=True)

@app.route('/api/data', methods=['POST', 'OPTIONS'])
def post_data():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "Preflight request received"})
    else:
        data = request.get_json()
        squares = data.get('squares', [])
        vsAI = data.get('vsAI')

        nested_array = [squares[i:i+3] for i in range(0, 9, 3)]
        squares = nested_array

        result = sar.make_step(squares, vsAI)

        if sar.win(squares) is False:
            response = jsonify({"squares": squares, "win": False})
        else:
            result = sar.win(squares)
            response = jsonify({"squares": squares, "win": result})

    # Add CORS headers to the response
    response.headers['Access-Control-Allow-Origin'] = 'https://tic-tac-toe-front-4a0m.onrender.com'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)








# from flask import Flask, request, jsonify, session
# from flask_cors import CORS
# import StepAndRool as sar

# app = Flask(__name__)
# CORS(app, origins="https://tic-tac-toe-front-4a0m.onrender.com")
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

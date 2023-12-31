from flask import Flask, request, jsonify, session
from flask_cors import CORS
import StepAndRool as sar

app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True, methods=["GET", "POST", "OPTIONS"], headers=["Content-Type", "Authorization"])
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

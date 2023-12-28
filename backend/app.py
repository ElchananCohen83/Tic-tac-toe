from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    try:
        # Print the details of the request object
        print("Request Method:", request.method)
        print("Request URL:", request.url)
        print("Request Headers:", request.headers)
        print("Request Args (Query Parameters):", request.args)
        print("Request Form Data:", request.form)
        print("Request JSON Data:", request.json)

        # Your business logic or data retrieval here (replace with actual implementation)
        data = {'message': 'Hello from the backend!'}

        return jsonify(data)
    except Exception as error:
        # Handle exceptions and return an error response
        print(f"Error in get_data: {error}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) #By default, Flask uses port 5000. 

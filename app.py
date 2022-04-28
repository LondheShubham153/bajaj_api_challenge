from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def welcome():
    print(request.json["data"])
    numbers = []
    alphabets = []
    for data in request.json["data"]:
        if data.isalpha():
            alphabets.append(data)
        else:
            numbers.append(data)
    return jsonify({
        "is_success": True,
        "user_id": "john_do_17091999",
        "email" : "john@xyz.com",
        "roll_number":"ABCD123",
        "numbers": numbers,
        "alphabets": alphabets}
    )

if __name__ == '__main__':
    app.run()
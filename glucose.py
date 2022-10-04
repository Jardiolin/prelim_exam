from flask import Flask, jsonify, request
app = Flask(__name__)

glucose =[
    {
        "glucose_id" : "1234",
        "date" : "10/04/2022",
        "glucose" : "70 mg"
    },
    {
        "glucose_id" : "1235",
        "date" : "10/03/2022",
        "glucose" : "75 mg"
    }
]

@app.route('/', methods=['POST','GET'])
def insertview():
    if request.method == 'POST':
        val = request.get_json()
        if val:
            glucose_inf.append(val)
        return jsonify(glucose)

    elif request.method == 'GET':
        return jsonify(glucose)


@app.route('/view/<int:num>', methods=['GET'])
def view(num):
    return jsonify(glucose[num])

@app.route('/<int:num>', methods=['PUT', 'GET','DELETE'])
def editdelete(num):
    if request.method == 'PUT':
        new = request.get_json()
        glucose[new] = new
        return jsonify(glucose)

    elif request.method == 'DELETE':
        glucose.pop(num)

if __name__ == '__main__':
    app.run()
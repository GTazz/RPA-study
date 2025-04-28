#GET: Request data from a specified resource
#POST: Send data to a server to create/update a resource
#PUT: Update a current resource with new data
#DELETE: Delete a specified resource

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@gmail.com"}

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200 # 200 means OK

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201 # 201 means Created

if __name__ == '__main__':
    app.run(debug=True)
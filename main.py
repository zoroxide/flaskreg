from flask import Flask, request, jsonify
from pymongo import MongoClient
from pdf import create_pdf_with_names_then_print
from utils import parseID, addAtt, printUserData

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('idofuser')
    
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    db = client.get_database("attendence")
    users_collection = db.get_collection("users")
    data = parseID(user_id)
    
    user_data = users_collection.find_one({"attendanee_id": data})

    if not user_data:
        return jsonify({"error": "User not found"}), 404

    user_data["_id"] = str(user_data["_id"])
    # printUserData(user_data['contact_name'], user_data['company_name'])
    # printUserData(user_data['contact_name'], user_data['company_name'])
    create_pdf_with_names_then_print(user_data['contact_name'], user_data['company_name'])
    addAtt(user_data)
    return jsonify(user_data), 200

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')

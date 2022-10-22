from fileinput import filename
from pickle import TRUE
from flask import Flask,request,jsonify
import json
import flask
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from model import model

UPLOAD_FOLDER='./files'

app=Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)

@app.route('/result' ,methods=["POST"])
def data():
    print("HELLO")
    if request.method == "POST":
        print(request.form,flush=True)
        period=request.form['period']
        date=request.form['date']
        f=request.files['file']
        print(f)
        file_secure = secure_filename(f.filename) 
        f.save(os.path.join(app.config["UPLOAD_FOLDER"],file_secure))
        print(file_secure)

        stored_filename='./files/'
        stored_filename+=file_secure
        print(stored_filename)
        predict = model(stored_filename,period,date)
        #os.remove(os.path.join(app.config["UPLOAD_FOLDER"],file_secure))
        print(predict)
        return jsonify(data = predict)

if __name__ == "__main__":
    app.run(debug=True)

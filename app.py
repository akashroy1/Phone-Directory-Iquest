from flask import Flask, request, jsonify, json, make_response, render_template
import pymongo
import json
from pymongo import MongoClient
from pymongo import collection

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://Admin:admin@cluster0.zuemm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.get_database("user")
records = db.user


@app.route("/", methods=['GET', 'POST'])
def home():

    if(request.method == 'POST'):
        name = request.form['name']
        number = request.form['number']

        user = {"name": name, "number":number}
        records.insert_one(user)
            
    
        # if(request.form['search-btn'] == 'searching'):
        #     key = request.form['search']
        #     print(key)
        #     # target = records.find_one({'name': key})
        #     # print(target)

    return render_template('index.html')

@app.route("/search", methods=['GET', 'POST'])
def search():

    key = request.form['search']
    target = records.find({'name': key})
    allResult = []
    for result in target:
        allResult.append(result)

    # for res in allResult:
    #     print(type(res))
    #     print(res["number"])
    print(allResult)
    if(allResult== []):
        return render_template('index.html', results=allResult, tag=0)

    return render_template('index.html', results=allResult, tag=1)



if (__name__ == "__main__"):
    app.run(debug=True)
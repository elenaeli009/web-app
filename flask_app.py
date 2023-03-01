from flask import Flask
import sqlite3
import json
from flask import request
import pymongo
from flask import render_template

app = Flask(__name__)

def get_db():
    """
    Function to connect with MongoDB localhost
    :return: Company collection
    """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    add_company = client["MyProject"]
    my_col = add_company["Companies"]
    return my_col

db = get_db()

@app.route('/get_data', methods=["GET"])
def get_companies():
    """
     GET method and function to connect and execute data from SQLite database
    :type: str
    :return: list of company names
    """
    try:
        conn = sqlite3.connect("C:/Users/Elena/Documents/data.db")
        print('Connected to database successfully.')

        x = conn.cursor()
        x.execute('SELECT * FROM companies')

        rows = x.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(e)

@app.route('/save_data', methods=["POST"])
def add_companies():
    """
    POST method and function for inserting companies in MongoDB
    :type: str
    :return: Successfully added data (companies) in MongoDB
    """
    companies = json.loads(request.data)
    for i in companies:
        try:
            companies_add = db["Companies"]
            companies_add.insert_one(i)
        except Exception as e:
            print(e)
    return "Data Added"

@app.route('/get_cleaned_data', methods=["GET"])
def get_cleaned_data():
    """
    GET method for connecting and geting data
    from MongoDB collection Companies.Companies
    :type: list
    :return: Successfully got data from
    MongoDB collection Companies.Companies
    """
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    add_company = client["MyProject"]
    my_col = add_company["Companies.Companies"]
    x   = []
    company = my_col.find()
    for i in company:
        x.append(i)
    return x

@app.route("/frontend")
def index():
    """
    Showing cleaned companies data to the frontend
    :type: list of dict
    :return: Renders template index.html
    """
    content = get_cleaned_data()
    return render_template("index.html", content=content)

if __name__ == '__main__':
    app.run()
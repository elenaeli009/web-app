import json
import requests

def read_data():
    """
    Getting all companies and their information from the local flask app
    :type: str
    :return: list of cleaned company names
    """
    companies = requests.get("http://127.0.0.1:5000/get_data").json()
    for i in range(len(companies)):
        companies[i][1] = clean_company_name(companies[i][1])
    return companies

def clean_company_name(company_name):
    """
    Clean company name which is gotten as an argument,
    :param company_name: Company_name saves company name
    :type: str
    :return: cleaned company name
    """
    company_name = company_name.lower()
    company_name = company_name.title()
    company_name = company_name.replace('-', '').replace('LTD.', '').replace('Ltd.', '').replace('ltd.', '').replace(
        'limited.', '').replace('Limited.', '').replace('LIMITED.', '').replace('Ltd.', '').replace('LTD', '').replace(
        'ltd', '').replace('limited', '').replace('Limited', '').replace('LIMITED', '').replace('Ltd', '')
    company_name = company_name.split(",")[0]
    while "(" in company_name:
        x = company_name.split("(", 1)
        company_name = x[0]
        x = x[1].split(")", 1)
        company_name = company_name + x[1]
    company_name = company_name.strip()
    return company_name

x = read_data()

def post_data(companies):
    """
    Sending the cleaned companies to the local flask application
    :param companies: list of companies for which we want to add to MongoDB local server
    :type: str
    :return: Successfully added data(companies) in MongoDB
    """
    url = "http://127.0.0.1:5000/save_data"
    try:
        company_add = []
        for i in companies:
            company = {
                "id": i[0],
                "name": i[1],
                "country_iso": i[2],
                "city": i[3],
                "nace": i[4],
                "website": i[5],
            }
            company_add.append(company)
        x = requests.post(url, data=json.dumps(company_add))
        print(x.text)
        return "Data added"
    except Exception as e:
        print(f"=> {e}")
        return "You have problem with your data"

y = post_data(x)
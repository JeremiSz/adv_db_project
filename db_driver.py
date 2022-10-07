import requests

AUTH = ("CouchDB","CouchDB")
URL = "http://127.0.0.1:5984/"
DATABASE = "papers"

response = requests.get(URL,auth=AUTH)

print(response)

def add_doc():
    return
def get_all():
    response = requests.get(URL + DATABASE + "/_all_docs", auth=AUTH)
    return response.json()
def get_doc(id : str):
    return requests.get(URL + DATABASE + "/" + id,auth=AUTH).json()
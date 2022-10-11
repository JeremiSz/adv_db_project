from email.header import Header
from urllib import response
import requests
import json

AUTH = ("CouchDB","CouchDB")
URL = "http://127.0.0.1:5984/"
DATABASE = "papers"
HEADER = {"Content-type":"application/json"}

class Doc:
    def __init__(
        self, authors : list[str], title:str, journal:str,
        year:int, page_from:int, page_to:int,
        volume:int, issue:int
        ) -> None:
        self.author = authors
        self.title = title
        self.journal = journal
        self.year = year
        self.pages = (page_from,page_to)
        self.volume = volume
        self.issue = issue
        return
    def new(
        authors : str, title:str, journal:str,
        year:str,page_from:str,page_to:str,
        volume:str,issue:str
    ):
        authors = authors.strip()
        title = title.strip()
        journal = journal.strip()
        year = year.strip()
        page_from = page_from.strip()
        page_to = page_to.strip()
        volume = volume.strip()
        issue = issue.strip()

        if not (authors and title and journal and year and
         page_from and page_to and volume and issue):
            return False

        authors = authors.replace('and',',')
        authors = authors.split(',')
        if not (page_from.isnumeric() and page_to.isnumeric() and
         year.isnumeric() and volume.isnumeric() and issue.isnumeric()):
            return False
        return Doc(
            authors,title,journal,
            int(year),int(page_from),int(page_to),
            int(volume),int(issue))


def add_doc(doc : Doc):
    requests.post(
        URL + DATABASE,
        auth=AUTH, 
        data= json.dumps(doc.__dict__),
        headers=HEADER)
    return

#unused
def get_all():
    response = requests.get(URL + DATABASE + "/_all_docs", auth=AUTH)
    return response.json()

def get_doc(id : str):
    return requests.get(URL + DATABASE + "/" + id,auth=AUTH).json()

def remove_doc(id : str, rev:str):
    responce = requests.delete(
        URL + DATABASE + "/" + id,
        auth=AUTH,
        params={"rev":rev})
    print(responce)
    return

def update_doc(id : str, rev : str, doc : Doc):
    doc._rev = rev
    requests.put(
        URL + DATABASE + "/" + id,
        auth=AUTH, 
        data= json.dumps(doc.__dict__),
        headers=HEADER)
    return

def get_docs_by_journal():
    response = requests.get(URL + DATABASE + "/_design/aggregate/_view/by-journal", auth=AUTH)
    return response.json()

def get_year_counts(year:str=""):
    if year:
        response = requests.get(URL + DATABASE + "/_design/aggregate/_view/count-year?key=" + year, auth=AUTH)
    else:
        response = requests.get(URL + DATABASE + "/_design/aggregate/_view/count-year", auth=AUTH)
    return response.json()
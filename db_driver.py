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
        self.authors = authors
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
    responce = requests.post(
        URL + DATABASE,
        auth=AUTH, 
        data= json.dumps(doc.__dict__),
        headers=HEADER)
    return

def get_all():
    response = requests.get(URL + DATABASE + "/_all_docs", auth=AUTH)
    return response.json()

def get_doc(id : str):
    return requests.get(URL + DATABASE + "/" + id,auth=AUTH).json()

def remove_doc(id : str, rev:str):
    print("remove")
    print(id + " " + rev)
    return

def update_doc(doc : Doc):
    print("update")
    print(doc)
    return
import os
from time import time
import PySimpleGUI as sp
import add_doc_page
import details_page
import db_driver
import os

REFRESH = "Refresh Page"
ADD_DOC = "Add Document"
UPDATE = "U"
REMOVE = "R"

def start():
    test= 0
    add_doc_btn = sp.Button(
        ADD_DOC,
        tooltip="Add a new document to your store",
        )
    refresh_btn = sp.Button(
        REFRESH,
        tooltip="Refresh to sync with the database"
    )
    layout = [[add_doc_btn,refresh_btn]]
    for row in db_driver.get_all()['rows']:
        doc = db_driver.get_doc(row['id'])
        layout.append(_make_doc_ui(doc))
    window = sp.Window("Academic Refrences",layout)

    while True:
        event,values = window.read()
        if event == sp.WIN_CLOSED:
            break
        elif event == REFRESH:
            _refresh(window)
        elif event == ADD_DOC:
            add_doc_page.start()
        elif event[1] == UPDATE:
            details_page.start(event[0])
        elif event[1] == REMOVE:
            db_driver.remove_doc(event[0],event[2])
            window = _refresh(window)
    return

def _make_doc_ui(doc) ->list:
    if not 'title' in doc:
        return[]
    return [
        sp.Text("Title: "+ doc["title"]),
        sp.Button("Details",key=(doc['_id'],UPDATE)),
        sp.Button("Remove", key=(doc['_id'],REMOVE,doc["_rev"]))
    ]
def _refresh(window : sp.Window):
    os.system("python main.py &")
    window.close()
    return
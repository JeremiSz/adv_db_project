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
CHECK_DATE = "Year Count"

def start():
    add_doc_btn = sp.Button(
        ADD_DOC,
        tooltip="Add a new document to your store",
        )
    refresh_btn = sp.Button(
        REFRESH,
        tooltip="Refresh to sync with the database"
    )
    fresh_btn = sp.Button(
        CHECK_DATE,
        tooltip="Check how many document you have for a given year"
    )
    layout = [[add_doc_btn,refresh_btn,fresh_btn]]
    for row in db_driver.get_docs_by_journal()['rows']:
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
        elif event == CHECK_DATE:
            _show_fresh()
    return

def _show_fresh():
    text = sp.PopupGetText("Which year?")
    amount = db_driver.get_year_counts(text)['rows'][0]['value']
    sp.Popup(
        amount,
        title="Freshness"
    )
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
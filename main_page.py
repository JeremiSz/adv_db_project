import PySimpleGUI as sp
import add_doc_page
import details_page
import db_driver

REFRESH = "Refresh Page"
ADD_DOC = "Add Document"
UPDATE = "U"
REMOVE = "R"

def start():
    
    window = sp.Window("Academic Refrence", _refresh() )

    while True:
        event,values = window.read()
        if event == sp.WIN_CLOSED:
            break
        elif event == REFRESH:
            window.layout = _refresh()
        elif event == ADD_DOC:
            add_doc_page.start()
        elif event[1] == UPDATE:
            details_page.start(event[0])
            
        elif event[1] == REMOVE:
            window.layout = _refresh()
    return

def _make_doc_ui(doc) ->list:
    if not 'title' in doc:
        return[]
    return [
        sp.Text("Title: "+ doc["title"]),
        sp.Button("Details",key=(doc['_id'],UPDATE)),
        sp.Button("Remove", key=(doc['_id'],REMOVE))
    ]
def _refresh():
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
        
    return layout
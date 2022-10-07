import PySimpleGUI as sp
import add_doc_page
import db_driver

REFRESH = "refresh"
ADD_DOC = "add_doc"

def start():
    
    window = sp.Window("Academic Refrence", _refresh() )

    while True:
        event,values = window.read()
        if event == sp.WIN_CLOSED:
            break
        print(event)
        match event:
            case "Refresh Page":
                window.layout = _refresh()
            case "Add Document":
                print("stuff")
                add_doc_page.start()
            case _:
                print(event)
                print(values)
    return

def _make_doc_ui(doc) ->list:
    author = "Author: "
    print(doc)
    if not 'author' in doc:
        return []
    for name in doc['author']:
        author += name + ", "

    pages = doc['pages']
    return [
        #sp.Text(author),
        sp.Text("Title: "+ doc["title"]),
        #sp.Text("Journal: " + doc["journal"]),
        #sp.Text("Year: " + str(doc["year"])),
        #sp.Text("Pages: from " + str(pages['from']) + " to " + str(pages['to'])),
        #sp.Text("Volume: " + str(doc['volume'])),
        #sp.Text("Issue: " + str(doc['issue']))
        sp.Button("Details",key=doc['_id'])
    ]
def _refresh():
    add_doc_btn = sp.Button(
        "Add Document",
        tooltip="Add a new document to your store",
        )
    refresh_btn = sp.Button(
        "Refresh Page",
        tooltip="Refresh to sync with the database"
    )
    layout = [[add_doc_btn,refresh_btn]]
    for row in db_driver.get_all()['rows']:
        doc = db_driver.get_doc(row['id'])
        layout.append(_make_doc_ui(doc))
        
    return layout
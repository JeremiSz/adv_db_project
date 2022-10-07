import PySimpleGUI as sp
import db_driver

def start(id:str):
    doc = db_driver.get_doc(id)

    author = ""
    for name in doc['author']:
        author += name + ", "

    pages = doc['pages']
    layout =  [
        [sp.Text("Author: "), sp.InputText(default_text=author)],
        [sp.Text("Title: "), sp.InputText(doc["title"])],
        [sp.Text("Journal: "), sp.InputText(doc["journal"])],
        [sp.Text("Year: "), sp.InputText(str(doc["year"]))],
        [sp.Text("Pages: from "),sp.InputText(str(pages['from'])), sp.Text(" to "), sp.InputText(str(pages['to']))],
        [sp.Text("Volume: "), sp.InputText(str(doc['volume']))],
        [sp.Text("Issue: "), sp.InputText(str(doc['issue']))],
        [sp.Button("Update")]
    ]
    window = sp.Window(doc["title"],layout=layout,modal=True)
    while True:
        event,values = window.read()
        if event == sp.WIN_CLOSED:
            window.close()
            break
        elif event == "Update":
            db_driver.update_doc(doc)
            window.close()
            break
    return
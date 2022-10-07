from turtle import title
import PySimpleGUI as sp
import db_driver
def _make_journal():
        return [
            [sp.Text("Authors: "), sp.InputText()],
            [sp.Text("Title: "), sp.InputText()],
            [sp.Text("Journal: "), sp.InputText()],
            [sp.Text("Year: "), sp.InputText()],
            [sp.Text("Pages: ")],
            [sp.Text("From: "), sp.InputText()],
            [sp.Text("To: "), sp.InputText()],
            [],
            [sp.Text("Volume: "), sp.InputText()],
            [sp.Text("Issues: "), sp.InputText()],
            [sp.Button("Add")]
        ]


def start():
    layout = [_make_journal()]
    window = sp.Window("Add Document",layout,modal=False)
    while True:
        event, values = window.read()
        if event == sp.WIN_CLOSED:
            break
        elif event == "Add":
            if _add(values):
                
                window.close() 
                break
    return

def _add(values):
    doc = dict()

    authors = values[0].strip()
    if authors == "":
        return False
    authors = authors.split(',')
    doc['authors'] = authors

    title = values[1].strip()
    if title == "":
        return False
    doc['title'] = title

    journal = values[2].strip()
    if journal == "":
        return False
    doc['journal'] = journal

    year = values[3].strip()
    if year == "" or not year.isnumeric():
        return False
    doc['year'] = int(year)

    pages = ()
    return


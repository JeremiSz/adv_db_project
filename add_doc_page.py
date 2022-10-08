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
    result = db_driver.Doc.new(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
    if not result:
        return result
    db_driver.add_doc(result)
    return True


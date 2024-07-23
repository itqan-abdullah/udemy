import FreeSimpleGUI as sg
label = sg.Text("Enter feet")
label2 = sg.Text("Enter inches")
inp1 = sg.InputText()
inp2 = sg.InputText()
conv = sg.Button("Convert")
window2 = sg.Window("Convertor",layout=[[label,inp1],[label2,inp2],[conv]])

window2.read()

window2.close()

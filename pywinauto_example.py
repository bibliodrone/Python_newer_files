#pywinauto_example

from pywinauto.application import Application
 
#Start Caculator application.
app = Application().Start('calc')
mainframe = app.CalcFrame
mainframe.Wait('ready')
 
#Get and press number 1 button.
btn1 = mainframe.Button5
btn1.Click()
 
#Get and press add button.
btnPlus = mainframe.Button23
btnPlus.Click()
 
#Get and press number 2 button.
btn2 = mainframe.Button11
btn2.Click()
 
#Get and press equals button.
btnEquals = mainframe.Button28
btnEquals.Click()
 
#Get result
result = mainframe.Static4
 
assert '3' in result.Texts()
 
print ('Test passed')
 
#Close application
app.Kill_()

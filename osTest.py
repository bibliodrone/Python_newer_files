import os

stamp='7784'
userName=os.getlogin()
fn = "List_"+stamp+".txt"
defaultPath = 'C://Users//'+userName+'//Desktop'
os.system ("@ echo on")
os.system("cd.. ")
os.system ("dir & pause") 
print (defaultPath)



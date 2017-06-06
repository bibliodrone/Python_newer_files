#Python 'subprocess' module (similar to module 'os')


import subprocess as sp

def subPro():
    command = sp.run("echo hello") 
    repr(command)


subPro()






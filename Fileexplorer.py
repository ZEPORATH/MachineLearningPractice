#select a file by a simple gui
'''
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print (filename)
'''
import tkFileDialog
from Tkinter import Tk
import easygui
'''
#take an user input 
import easygui

value = int(easygui.enterbox(msg = 'Enter the port no:',title='PORT'))
print value, type(value)

easygui.msgbox(msg = 'User has entered this port',title = 'PORT')
p = easygui.fileopenbox()
print p, type(p)
s = easygui.filesavebox()
print s
'''
def file_save():
    Tk().withdraw()
    f = tkFileDialog.asksaveasfile(mode='w')
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    print f
    s = str(f)
    lst = s.split("'")
    print lst[1], type(lst[1])

file_save()









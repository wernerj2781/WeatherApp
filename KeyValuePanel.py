__author__ = 'Jeff Werner'

from tkinter import *

class KeyValuePanel(Frame):
    def __init__(self,master, key_var, value_var, xPos, yPos):
        super(KeyValuePanel, self).__init__(master)
        self.createFields(master, key_var, value_var, xPos, yPos)

    def createFields(self, master, key_var_output, value_var_output, xPos, yPos):
        key_label = Label(master)
        key_label['text'] = key_var_output
        key_label['width'] = 15
        key_label.place(x=xPos, y=yPos)
        value_label = Label(master)
        value_label['text'] = value_var_output
        value_label['width'] = 15
        value_label.place(x=xPos+150, y=yPos)



from Tkinter import *
import subprocess
import Constants

class Project(Frame):
  def createWidgets(self):
    self.create_label = Label(self.inner_frame, text=Constants.CREATE_MESSAGE)
    self.create_label.grid(row=0, column=0, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

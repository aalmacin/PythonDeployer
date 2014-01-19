from Tkinter import *
import subprocess
import Constants

class Project(Frame):
  def createWidgets(self):
    self.new_button = Button(self)

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

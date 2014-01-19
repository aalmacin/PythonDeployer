from Tkinter import *
import Constants

class Home(Frame):
  def createWidgets(self):
    self.home_label = Label(self, text=Constants.HOME_TXT)
    self.home_label.grid(row=0, column=0, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createWidgets()


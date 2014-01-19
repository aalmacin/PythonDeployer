from Tkinter import *
import subprocess
import Constants

class Deploy(Frame):
    def run_deployment(self):
      subprocess.call(['sh test.sh'], shell=True)

    def createWidgets(self):
      self.deployer_button = Button(self, text='Deploy', command=self.run_deployment)
      self.deployer_button.grid(row=1, column=1, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

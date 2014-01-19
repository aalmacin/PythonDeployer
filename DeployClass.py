from Tkinter import *
import subprocess
import Constants

class Deploy(Frame):
    def run_deployment(self):
      subprocess.call(['sh test.sh'], shell=True)


    def createWidgets(self):
        self.inner_frame = Frame(self, width=100, height=100)
        self.inner_frame.grid(row=0, column=0, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

        self.quit_button = Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(row=1, column=0, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

        self.deployer_button = Button(self, text='Deploy', command=self.run_deployment)
        self.deployer_button.grid(row=1, column=1, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

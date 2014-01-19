from Tkinter import *
import subprocess
from DeployClass import Deploy
from HomeClass import Deploy
from  import Deploy

class Application(Frame):
    def createWidgets(self):
      home = Home()
      home.grid(row=0, column=0)

      new_projects = Project()
      new_projects.grid(row=0, column=0)

      deployer = Deploy()
      deployer.grid(row=0, column=0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

def main():
  root = Tk()
  app = Application(master=root)
  app.mainloop()
  root.destroy()

if __name__ == "__main__": main()

from Tkinter import *
import subprocess
from Pages import *
import Constants

class Application(Frame):

    def show_home(self):
      self.home.grid()
      self.projects.grid_remove()
      self.deployer.grid_remove()

    def show_project(self):
      self.home.grid_remove()
      self.projects.grid()
      self.deployer.grid_remove()

    def show_deploy(self):
      self.home.grid_remove()
      self.projects.grid_remove()
      self.deployer.grid()

    def createWidgets(self):
      # Home Button
      self.home_button = Button(text=Constants.HOME_TXT, command=self.show_home)
      self.home_button.grid(row=0, column=0, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.project_button = Button(text=Constants.PROJECT_TXT, command=self.show_project)
      self.project_button.grid(row=0, column=1, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.deploy_button = Button(text=Constants.DEPLOY_TXT, command=self.show_deploy)
      self.deploy_button.grid(row=0, column=2, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.quit_button = Button(text='Quit', command=self.quit)
      self.quit_button.grid(row=2, column=0, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.home = Home()
      self.home.grid(row=1, column=0)

      self.projects = Project()
      self.projects.grid(row=1, column=0)
      self.projects.grid_remove()

      self.deployer = Deploy()
      self.deployer.grid(row=1, column=0)
      self.deployer.grid_remove()


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

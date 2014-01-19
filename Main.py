from Tkinter import *
import subprocess
from Pages import *
import Constants

class Application(Frame):

    def remove_all(self):
      self.home.grid_remove()
      self.projects.grid_remove()
      self.deployer.grid_remove()

    def show_home(self):
      self.remove_all()
      self.home.grid()

    def show_project(self):
      self.remove_all()
      self.projects.grid()

    def show_deploy(self):
      self.remove_all()
      self.deployer.grid()

    def createWidgets(self):
      # Home Button
      self.button_frame = Frame(self)
      self.button_frame.home_button = Button(text=Constants.HOME_TXT, command=self.show_home)
      self.button_frame.home_button.grid(row=0, column=0, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.button_frame.project_button = Button(text=Constants.PROJECT_TXT, command=self.show_project)
      self.button_frame.project_button.grid(row=0, column=1, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.button_frame.deploy_button = Button(text=Constants.DEPLOY_TXT, command=self.show_deploy)
      self.button_frame.deploy_button.grid(row=0, column=2, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)
      self.button_frame.grid(row=0, column=0, columnspan=3)

      self.quit_button = Button(text='Quit', command=self.quit)
      self.quit_button.grid(row=2, column=0, columnspan=3, ipadx=Constants.C_PADDING_SIZE, ipady=Constants.C_PADDING_SIZE)

      self.home = Home()
      self.home.grid(row=1, column=0, columnspan=3)

      self.projects = Project()
      self.projects.grid(row=1, column=0, columnspan=3)
      self.projects.grid_remove()

      self.deployer = Deploy()
      self.deployer.grid(row=1, column=0, columnspan=3)
      self.deployer.grid_remove()


    def __init__(self, master=None):
        Frame.__init__(self, master, width=Constants.APP_WIDTH, height=Constants.APP_HEIGHT)
        self.grid()
        self.createWidgets()

def main():
  root = Tk()
  app = Application(master=root)
  app.mainloop()
  root.destroy()

if __name__ == "__main__": main()

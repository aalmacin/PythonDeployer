from Tkinter import *
import subprocess
import Constants

class Project(Frame):
  def show_new_project_text(self):
    self.new_project_frame.grid(row=1, column=0, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

  def createWidgets(self):
    # Button for new project added
    self.new_button = Button(self, text=Constants.NEW_PROJECT_TEXT, command=self.show_new_project_text)
    self.new_button.grid(row=0, column=0, padx=Constants.C_PADDING_SIZE, pady=Constants.C_PADDING_SIZE)

    self.new_project_frame = Frame(self)

    # Project Name
    self.new_project_frame.project_name_label = Label(self.new_project_frame, text=Constants.PROJECT_NAME_TXT)
    self.new_project_frame.project_name_label.grid(row=0, column=0)

    self.new_project_frame.project_name_entry = Entry(self.new_project_frame)
    self.new_project_frame.project_name_entry.grid(row=0, column=1)

    # Project IP
    self.new_project_frame.project_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
    self.new_project_frame.project_ip_label.grid(row=1, column=0)

    self.new_project_frame.project_ip_entry = Entry(self.new_project_frame)
    self.new_project_frame.project_ip_entry.grid(row=1, column=1)

    # Project username
    self.new_project_frame.project_username_label = Label(self.new_project_frame, text=Constants.PROJECT_USERNAME_TXT)
    self.new_project_frame.project_username_label.grid(row=2, column=0)

    self.new_project_frame.project_username_entry = Entry(self.new_project_frame)
    self.new_project_frame.project_username_entry.grid(row=2, column=1)

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

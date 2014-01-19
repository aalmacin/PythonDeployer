from Tkinter import *
import subprocess
import Constants
import re

class Project(Frame):
  def _create_config(self):
    project_name = self.new_project_frame.project_name_entry.get()
    project_ip = self.new_project_frame.project_ip_entry.get()
    project_username = self.new_project_frame.project_username_entry.get()

    new_project_path = str.lower(re.sub(r'\W+', '_', project_name))
    new_project_cmd = 'mkdir projects/' + new_project_path
    fail = subprocess.call([new_project_cmd], shell=True)
    f = open('projects/' + new_project_path + '/staging.conf','w')
    f.write('ip=' + project_ip + '\nusername=' + project_username + '\npath=/home/' + project_username + '/staging')
    f.close()

    self.new_project_frame.grid_forget()
    if fail:
      self.error_message = Label(self, text=Constants.PROJECT_EXISTS_MESSAGE)
      self.error_message.grid(row=1, column=0)
    else:
      print 'Created'


    project_frame_winfo = self.new_project_frame.winfo_children()
    for i in range(0, len(project_frame_winfo)):
      if isinstance(project_frame_winfo[i], Entry):
        project_frame_winfo[i].delete(0)

  def grid_remove(self):
    Frame.grid_remove(self)
    if hasattr(self, 'new_project_frame'):
      self.new_project_frame.grid_remove()
      self._remove_error_message()

  def _remove_error_message(self):
    if hasattr(self, 'error_message'):
      self.error_message.grid_forget()

  def show_new_project_text(self):
    self._remove_error_message()
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

    self.new_project_frame.create_button = Button(self.new_project_frame, text=Constants.NEXT_TXT, command=self._create_config)
    self.new_project_frame.create_button.grid(row=3, column=0, columnspan=2)

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

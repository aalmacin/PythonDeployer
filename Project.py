from Tkinter import *
import subprocess
import Constants
import re

FILE_CREATION_FORMAT = 'ip=%(ip)s\npath=%(path)s'
GLOBAL_FILE_CREATION_FORMAT = 'username=%(username)s'
FILE_NAME_FORMAT = '%(path)s/%(env)s.conf'
class Project(Frame):
  def _create_config(self):
    project_name = self.new_project_frame.project_name_entry.get()
    project_username = self.new_project_frame.project_username_entry.get()

    new_project_path = str.lower(re.sub(r'\W+', '_', project_name))
    global_path = 'projects/%(path)s' % {"path": new_project_path}
    new_project_cmd = 'mkdir %(path)s' % {"path": global_path}
    fail = subprocess.call([new_project_cmd], shell=True)

    f = open(FILE_NAME_FORMAT % {"path":global_path, "env": "global"},'w')
    f.write(GLOBAL_FILE_CREATION_FORMAT % {"username": project_username})
    f.close()

    self.new_project_frame.grid_forget()

    if fail:
      self.error_message = Label(self, text=Constants.PROJECT_EXISTS_MESSAGE)
      self.error_message.grid(row=1, column=0)
    else:
      self._create_config_files(global_path)


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

    # Project username
    self.new_project_frame.project_username_label = Label(self.new_project_frame, text=Constants.PROJECT_USERNAME_TXT)
    self.new_project_frame.project_username_label.grid(row=1, column=0)

    self.new_project_frame.project_username_entry = Entry(self.new_project_frame)
    self.new_project_frame.project_username_entry.grid(row=1, column=1)

    # Project environments
    self.new_project_frame.project_environments_label = Label(self.new_project_frame, text=Constants.ENVIRONMENTS_TXT)
    self.new_project_frame.project_environments_label.grid(row=2, column=0, columnspan=2)
    row_count = 3

    # Environment Fields
    self._create_env_fields(self.new_project_frame)
    self._show_env_fields(row_count)


    # Create button
    self.new_project_frame.create_button = Button(self.new_project_frame, text=Constants.SAVE_TXT, command=self._create_config)
    self.new_project_frame.create_button.grid(row=24, column=0, columnspan=2)


  def _create_env_fields(self, project_frame):
    env_texts = [Constants.DEV_TXT, Constants.QA_TXT, Constants.STAGING_TXT, Constants.STAGING_2_TXT, Constants.LIVE_TXT, Constants.LIVE_2_TXT]
    self.env_fields = []
    for i in range(0, len(env_texts)):
      self.env_fields.append(
        {
          'name': env_texts[i],
          'env_label': Label(project_frame, text=env_texts[i]),
          'path_label': Label(project_frame, text=Constants.PATH_TXT),
          'path_entry': Entry(project_frame),
          'ip_label': Label(project_frame, text=Constants.PROJECT_IP_TXT),
          'ip_entry': Entry(project_frame)
        }
      )

  def _show_env_fields(self, row_count):
    for i in range(0, len(self.env_fields)):
      grid_c = row_count + (i * 3)
      env_field = self.env_fields[i]
      env_field['env_label'].grid(row=grid_c, columnspan=2)
      env_field['path_label'].grid(row=grid_c + 1, column=0)
      env_field['path_entry'].grid(row=grid_c + 1, column=1)
      env_field['ip_label'].grid(row=grid_c + 2, column=0)
      env_field['ip_entry'].grid(row=grid_c + 2, column=1)

  def _create_config_files(self, global_path):
    for i in range(0, len(self.env_fields)):
      env_field = self.env_fields[i]
      path = env_field['path_entry'].get()
      ip = env_field['ip_entry'].get()

      env = str.lower(re.sub(r'\W+', '_', env_field['name']))
      local_path = FILE_NAME_FORMAT % {"path" : global_path, "env" : env}
      config_file = open(local_path, 'w')
      config_file.write(FILE_CREATION_FORMAT % {"ip" : ip, "path" : path})
      config_file.close()

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.project_entries = []
    self.createWidgets()

from Tkinter import *
import subprocess
import Constants
import re

class Project(Frame):
	def _create_config(self):
		project_name = self.new_project_frame.project_name_entry.get()
		project_username = self.new_project_frame.project_username_entry.get()

		dev_ip = self.new_project_frame.project_dev_ip_entry.get()
		dev_path = self.new_project_frame.project_dev_path_entry.get()

		qa_ip = self.new_project_frame.project_qa_ip_entry.get()
		qa_path = self.new_project_frame.project_qa_path_entry.get()

		staging_ip = self.new_project_frame.project_staging_ip_entry.get()
		staging_path = self.new_project_frame.project_staging_path_entry.get()

		staging_2_ip = self.new_project_frame.project_staging_2_ip_entry.get()
		staging_2_path = self.new_project_frame.project_staging_2_path_entry.get()

		live_ip = self.new_project_frame.project_live_ip_entry.get()
		live_path = self.new_project_frame.project_live_path_entry.get()

		live_2_ip = self.new_project_frame.project_live_2_ip_entry.get()
		live_2_path = self.new_project_frame.project_live_2_path_entry.get()

		new_project_path = str.lower(re.sub(r'\W+', '_', project_name))
		global_path = 'projects/%(path)s' % {"path": new_project_path}
		new_project_cmd = 'mkdir %(path)s' % {"path": global_path}
		fail = subprocess.call([new_project_cmd], shell=True)

		self.new_project_frame.grid_forget()

		file_creation_format = 'ip=%(ip)s\npath=%(path)s'
		global_file_creation_format = 'username=%(username)s'
		file_name_format = '%(path)s/%(env)s.conf'

		if fail:
			self.error_message = Label(self, text=Constants.PROJECT_EXISTS_MESSAGE)
			self.error_message.grid(row=1, column=0)
		else:
			f = open(file_name_format % {"path":global_path, "env": "global"},'w')
			f.write(global_file_creation_format % {"username": project_username})
			f.close()

			dev_local_path = file_name_format % {"path":global_path, "env": "dev"}
			f = open(dev_local_path,'w')
			f.write(file_creation_format % {"ip": dev_ip, "path": dev_path})
			f.close()

			qa_local_path = file_name_format % {"path":global_path, "env": "qa"}
			f = open(qa_local_path,'w')
			f.write(file_creation_format % {"ip": qa_ip, "path": qa_path})
			f.close()

			staging_local_path = file_name_format % {"path":global_path, "env": "staging"}
			f = open(staging_local_path,'w')
			f.write(file_creation_format % {"ip": staging_ip, "path": staging_path})
			f.close()

			staging_2_local_path = file_name_format % {"path":global_path, "env": "staging_2"}
			f = open(staging_2_local_path,'w')
			f.write(file_creation_format % {"ip": staging_2_ip, "path": staging_2_path})
			f.close()

			live_local_path = file_name_format % {"path":global_path, "env": "live"}
			f = open(live_local_path,'w')
			f.write(file_creation_format % {"ip": live_ip, "path": live_path})
			f.close()

			live_2_local_path = file_name_format % {"path":global_path, "env": "live_2"}
			f = open(live_2_local_path,'w')
			f.write(file_creation_format % {"ip": live_2_ip, "path": live_2_path})
			f.close()


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
		self.new_project_frame.project_username_label.grid(row=2, column=0)

		self.new_project_frame.project_username_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_username_entry.grid(row=2, column=1)

		# Project environments
		self.new_project_frame.project_environments_label = Label(self.new_project_frame, text=Constants.ENVIRONMENTS_TXT)
		self.new_project_frame.project_environments_label.grid(row=3, column=0, columnspan=2)

		# Dev env
		self.new_project_frame.dev_label = Label(self.new_project_frame, text=Constants.DEV_TXT)
		self.new_project_frame.dev_label.grid(row=4, column=0, columnspan=2)

		self.new_project_frame.project_dev_path_label = Label(self.new_project_frame, text=Constants.PATH_TXT)
		self.new_project_frame.project_dev_path_label.grid(row=5, column=0)

		self.new_project_frame.project_dev_path_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_dev_path_entry.grid(row=5, column=1)

		# Dev IP
		self.new_project_frame.project_dev_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
		self.new_project_frame.project_dev_ip_label.grid(row=6, column=0)

		self.new_project_frame.project_dev_ip_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_dev_ip_entry.grid(row=6, column=1)

		# QA env
		self.new_project_frame.qa_label = Label(self.new_project_frame, text=Constants.QA_TXT)
		self.new_project_frame.qa_label.grid(row=7, column=0, columnspan=2)

		self.new_project_frame.project_qa_path_label = Label(self.new_project_frame, text=Constants.PATH_TXT)
		self.new_project_frame.project_qa_path_label.grid(row=8, column=0)

		self.new_project_frame.project_qa_path_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_qa_path_entry.grid(row=8, column=1)

		# QA IP
		self.new_project_frame.project_qa_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
		self.new_project_frame.project_qa_ip_label.grid(row=9, column=0)

		self.new_project_frame.project_qa_ip_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_qa_ip_entry.grid(row=9, column=1)

		# STAGING env
		self.new_project_frame.staging_label = Label(self.new_project_frame, text=Constants.STAGING_TXT)
		self.new_project_frame.staging_label.grid(row=10, column=0, columnspan=2)

		self.new_project_frame.project_staging_path_label = Label(self.new_project_frame, text=Constants.PATH_TXT)
		self.new_project_frame.project_staging_path_label.grid(row=11, column=0)

		self.new_project_frame.project_staging_path_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_staging_path_entry.grid(row=11, column=1)

		# STAGING IP
		self.new_project_frame.project_staging_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
		self.new_project_frame.project_staging_ip_label.grid(row=12, column=0)

		self.new_project_frame.project_staging_ip_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_staging_ip_entry.grid(row=12, column=1)

		# STAGING env
		self.new_project_frame.staging_2_label = Label(self.new_project_frame, text=Constants.STAGING_2_TXT)
		self.new_project_frame.staging_2_label.grid(row=13, column=0, columnspan=2)

		self.new_project_frame.project_staging_2_path_label = Label(self.new_project_frame, text=Constants.PATH_TXT)
		self.new_project_frame.project_staging_2_path_label.grid(row=14, column=0)

		self.new_project_frame.project_staging_2_path_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_staging_2_path_entry.grid(row=14, column=1)

		# STAGING IP
		self.new_project_frame.project_staging_2_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
		self.new_project_frame.project_staging_2_ip_label.grid(row=15, column=0)

		self.new_project_frame.project_staging_2_ip_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_staging_2_ip_entry.grid(row=15, column=1)

		# LIVE env
		self.new_project_frame.live_label = Label(self.new_project_frame, text=Constants.LIVE_TXT)
		self.new_project_frame.live_label.grid(row=16, column=0, columnspan=2)

		self.new_project_frame.project_live_path_label = Label(self.new_project_frame, text=Constants.PATH_TXT)
		self.new_project_frame.project_live_path_label.grid(row=17, column=0)

		self.new_project_frame.project_live_path_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_live_path_entry.grid(row=17, column=1)

		# LIVE IP
		self.new_project_frame.project_live_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
		self.new_project_frame.project_live_ip_label.grid(row=18, column=0)

		self.new_project_frame.project_live_ip_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_live_ip_entry.grid(row=18, column=1)

		# LIVE_2 env
		self.new_project_frame.live_2_label = Label(self.new_project_frame, text=Constants.LIVE_2_TXT)
		self.new_project_frame.live_2_label.grid(row=19, column=0, columnspan=2)

		self.new_project_frame.project_live_2_path_label = Label(self.new_project_frame, text=Constants.PATH_TXT)
		self.new_project_frame.project_live_2_path_label.grid(row=20, column=0)

		self.new_project_frame.project_live_2_path_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_live_2_path_entry.grid(row=20, column=1)

		# LIVE_2 IP
		self.new_project_frame.project_live_2_ip_label = Label(self.new_project_frame, text=Constants.PROJECT_IP_TXT)
		self.new_project_frame.project_live_2_ip_label.grid(row=21, column=0)

		self.new_project_frame.project_live_2_ip_entry = Entry(self.new_project_frame)
		self.new_project_frame.project_live_2_ip_entry.grid(row=21, column=1)

		# Create button
		self.new_project_frame.create_button = Button(self.new_project_frame, text=Constants.SAVE_TXT, command=self._create_config)
		self.new_project_frame.create_button.grid(row=24, column=0, columnspan=2)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

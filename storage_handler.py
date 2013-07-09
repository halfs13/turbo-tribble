import json
from customer_handler import *
from invoice_handler import *

STATES = []

class storage:
	json_object = {}
    	
	def __init__(self, file_name):
        if(file_name is None or file_name == ''):
            load_data_default_file()
        else:
            load_data_file(file_name)
        
	def load_data_default_file(self):
		global customers
		try:
		    storage_file = open('database.json', 'r')
		    file_string = ''
		    for line in storage_file:
		        file_string += line
		    self.json_object = json.loads(file_string)
		except IOError:
		    print("Error reading file -- no such file exists. Creating")
		    storage_file = open('database.json', 'a')
		    storage_file.close()
		    self.load_data_default_file()

	def load_data_file(self, file_name):
		print("TODO")

def in_state_list(state_string):
    return false

def get_states():
    global STATES
    return STATES

import json

class customers:
	customer_list = {}

	def __init__(self, json_object):
		self.customer_list = json_object

	def new_customer(self, details_json):
		valid = true
		#if(not(in_state_list(details_json))):
		#    valid = false
		if(not('name' in details_json)):
		    valid = false

	def list_customers(self, params):
		if(params != None and params != ""):
			return self.customer_list
		else:
			keys_list = self.customer_list.keys()
			result = []
			for i in range(len(keys_list)):
				result.append(self.customer_list[keys_list[i]])
			return result

	def get_customer(self, name):
		return self.customer_list[name]

	def update_customer(self, params):
		print("todo")

	def delete_customer(self, name):
		print("TODO")

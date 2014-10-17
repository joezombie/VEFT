class PhoneBook(object):
	def __init__(self):
		self.contacts = {}

	def add(self, contact):
		if contact.name in self.contacts:
			raise Exception('Name already in contacts')
		self.contacts[contact.name] = contacts

	def search(self, name):
		for k in self.contacts.keys():
			if (k.startswith(name)):
				return selef.contacts.get(key)
		return self.contacts.get(name)

	def search2(self, name):
		name = name.lower()
		return_contacts = []
		for k in self.contacts.keys():
			if (k.lower().startswith(name)):
				return_contacts.append(self.contacts.get(k.name))
		return return_contacts
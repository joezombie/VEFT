class Contact(object):
	def __init__(self, name, address, phone_number):
		self.name = name
		self.address = address
		self.phone_number = phone_number

	def __str__(self):
		return '{0} {1} {2}'.format(self.name, self.address, self.phone_number)





c = Contact('Joi', 'Skolavegur', '5551234')
print c
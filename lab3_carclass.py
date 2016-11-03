class Car(object):
	"""Car class, blue print for car objects """
	def __init__(self,name = None,model=None,car_type = None):

		self.car_type =car_type
		self.name ='General'
		if  not name== None:
			self.name = name

		if model == None:
			self.model = 'GM'
		else:
			self.model =model
		if name == 'Koenigsegg' or name =='Porshe':
			self.num_of_doors =2
		else:
			self.num_of_doors =4
		if car_type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels =4
		self.speed =0


	def is_saloon(self):
		"""Returns false if car True if car is not a trailer"""
		if self.car_type != 'trailer':
			return True
		else:
		 return False
	def drive(self,s):
	    """Gets the at driving speed"""
	    if self.car_type == 'trailer' and s>0:
			self.speed= 77
			return self
	    elif self.name =='Mercedes' and s>0:
			self.speed = 1000
			return self
	    else:
		    return self
































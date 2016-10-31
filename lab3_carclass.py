class Car(object):
    

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
		if self.car_type != 'trailer':
			return True
	def drive(self,s):
		if self.car_type == 'trailer':
			self.speed= (s * 11)
			return self
		elif self.name =='Mercedes':
			self.speed =(500 * (s-1))
			return self
































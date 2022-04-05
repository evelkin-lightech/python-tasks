class Serie:
	"""
		Начиная с Python v3 все классы явно и неявно наследуются от базового
	   	класса object
	"""

	def __new__(cls, *args, **kwargs):
		"""Вызывается перед созданикм класса"""
		return super().__new__(cls)

	def __init__(self, *args):
		"""Инициализатор объектов класса"""
		self.args = [*args]

	def __del__(self):
		"""Финализатор класса"""
		pass

	def __repr__(self):
		"""Class"""
		return 'Serie()'

	def __str__(self):
		"""Values"""
		return str(self.args)

	def __iter__(self):
		return self

	def lenght(self):
		"""
		Count items in the series
		"""
		count = 0
		for i in self.args:
			count += 1
		return count

	def add(self, value):
		"""
		Append new item in end of the series
		"""
		self.args = self.args + [value]
		return self.args

	def update(self, *args):
		"""
		Append a few item in end of the series
		"""
		self.args = self.args + [*args]
		return self.args

	def remove(self, value):
		"""
		Find and remove item in the series
		"""
		new_series = [] 
		for i in self.args:
			if i != value:
				new_series = new_series + [i]
		if new_series == self.args:
			return f'{value} - not found into this series'
		else:
			return new_series


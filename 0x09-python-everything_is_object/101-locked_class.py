class LockedClass:
	def __init__(self):
		self.locked = True
	def __setattr__(self, key, value):
		if key == 'locked':
			raise AttributeError('locked is a read-only attribute')
		else:
			super().__setattr__(key, value)
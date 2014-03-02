def func():
	x = 'ni'
	def nested():
		nonlocal x = 'spam'
	nested()
	print(x)
func()
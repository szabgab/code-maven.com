import nose
from nose.plugins.attrib import attr

# nose decors and attr

def copy_attrs(source, to):
		for attr in dir(source):
			if attr.startswith('_'):
				continue
			if attr.startswith('func_'):
				continue
			to.__setattr__(attr, getattr(source, attr))

def one(func):
	def created_in_one():
		print("\nin one {} {} {}".format(func.__name__, getattr(func, 'hello', None), getattr(created_in_one, 'hello', None)))
		#print(dir(func))
		print(dir(created_in_one))
		
		# for attr in dir(created_in_one):
			# if attr.startswith('_'):
				# continue
			# if attr.startswith('func_'):
				# continue
			# func.__setattr__(attr, getattr(created_in_one, attr))

		copy_attrs(created_in_one, func)
			
		func()
		print("out one {} {} {}".format(func.__name__, getattr(func, 'hello', None), getattr(created_in_one, 'hello', None)))
	created_in_one.__name__ = func.__name__
	return created_in_one
		
def two(func):
	def created_in_two():
		#print(dir(func))
		print(dir(created_in_two))
		print("in two {} {} {}".format(func.__name__, getattr(func, 'hello', None), getattr(created_in_two, 'hello', None)))
		copy_attrs(created_in_two, func)
		func()
		print("out two {} {} {}".format(func.__name__, getattr(func, 'hello', None), getattr(created_in_two, 'hello', None)))
	created_in_two.__name__ = func.__name__
	return created_in_two

def three(func):
	def created_in_three():
		#print(dir(func))
		print(dir(created_in_three))
		print("in two {} {} {}".format(func.__name__, getattr(func, 'hello', None), getattr(created_in_three, 'hello', None)))
		func()
		print("out two {} {} {}".format(func.__name__, getattr(func, 'hello', None), getattr(created_in_three, 'hello', None)))
	created_in_three.__name__ = func.__name__
	return created_in_three

@attr("world")
@attr("hello")
@one
@two
@three
def test_a():
	print("a - start")
	print(dir(test_a))
	

# @one
# @two
# @attr("hello")
# def test_b():
	# print("b - start")


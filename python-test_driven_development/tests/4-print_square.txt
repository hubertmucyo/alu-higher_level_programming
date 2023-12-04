import the module:
	>>> show = __import__("4-print_square").print_square
	>>> show(2)
	##
	##

test 0 input:
	>>> show(-1)
	Traceback (most recent call last):
	...
	ValueError: size must be >= 0

test string inpupt:
	>>> show("nic")
	Traceback (most recent call last):
	...
	TypeError: size must be an integer

test for float input:
	>>> show(1.3)
	Traceback (most recent call last):
	...
	TypeError: size must be an integer

test for no input:
	>>> show()
	Traceback (most recent call last):
	...
	TypeError: print_square() missing 1 required positional argument: 'size'

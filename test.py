print('Hello WOrld!')
x = 'im outside'
def test():
	print(x)
	test2()
def test2():
	global y
	y = 'im from 2nd function'
	for i in range(3):
		print(i)
# print(y)
test()
print(y)
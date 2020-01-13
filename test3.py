def squares(n=5):
	list1=[]
	# print(n)
	for i in range(1, n+1):
		print(i)
		list1.append(i**2)
	print(list1)
	return list1
def squares2(n):
	return sum([i*i for i in range(1,n+1)])
def sum_of_squares(e,n):
	# print('bb')
	list1 = squares()
	list2 = squares2(n)
	print(list1)
	print(list2)
	x = list(sorted(list1)).pop()
	print(list1 , x)
	return sum(list1)
print(sum_of_squares(3,10))
# print()
# assert sum_of_squares(1) == 1
# assert sum_of_squares(2) == 5
# assert sum_of_squares(10) == 385
# assert sum_of_squares(11) == 506
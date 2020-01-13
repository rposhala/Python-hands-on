def longestprefix(lstrs):
	llstrs = []
	a= [len(i) for i in lstrs]

	output = ''
	a.sort()
	
	w = 0
	while(w < a[0]):
		k = [i[w] for i in lstrs]
		print(k)
		s = set(k)
		print(s)
		if len(s) == 1:
			output = output + k[0]
		else :
			break
		w += 1
	print(output)
lstrs = ['flioyu','flioyut','flioyhhg']
# longestprefix(lstrs)

def say(n):
	olist = ['rohith','1']
	
	for i in range(1,31):
		# print(i)
		# print(len(olist))
		a = olist[i]

		for j in range(len(a)):
			if j == 0:
				b = a[j]
				sub = ''
				count = 0
			else :
				s = 0
				if b != a[j]:
					sub = sub + str(count) + b
					s = 1
					count = 0
			count+=1
			b = a[j]
			# if a[j] == a[len(a)-1]:

		sub = sub + str(count) + b
		olist.append(sub)
	print(olist)
say(5)



%%%% plot for quadratic model fit %%%%%
figure(7)
plot(x,y,'+',x,f2,'b');
xlabel('x');
ylabel('f(x)');
title('Plot of the data and the resulting regression line(Quadratic polynomial)');
legend('y','Quadratic polynomial with min. least square error');

%%%%%%%%%%%%%%%%

%%%% plot for linear model fit%%%%%
figure(6)
plot(x,y,'x',x,f1,'r');
xlabel('x');
ylabel('f(x)');
title('Plot of the data and the resulting regression line(Linear function)');
legend('y','Linear function fitting data with min. least square error');




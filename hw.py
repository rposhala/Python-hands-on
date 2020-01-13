# def computeMedian():
#     """
#     The function has no input parameter, return median value of the list
#     """
#     # YOUR CODE HERE
#     import math
# #     infile = open('data_p2.txt','r')
# #     line = infile.readline()filename = input('What is the name of the file? ')
#     filename = input('What is the name of the file? ')
#     with open(filename,'r') as f:
#         med_list=[]
#         i = 0
#         j = 0
#         for line in f:
#             i += 1 
# #             while line:
#             s = line.strip()
#             d = {}

#             try :
#                 med_list.append(float(s))
# #                     line = infile.readline()
#             except Exception as error:
#                 print(error)
#                 j += 1
# #                     line = infile.readline()
#                 continue
#         print(i)
#         print(j)
#         med_list.sort()
#         l=len(med_list)
#         if l % 2 == 0 :
#             print((med_list[l/2] + med_list[(l/2)+1])/2)
#         elif l % 2 != 0:
#             print(med_list[math.floor(l/2)])

# computeMedian()


# import time
# def monitorTime(N):
        # YOUR CODE HERE
    # import time
    # x = list(range(1,N+1))
    # y = ["No."+ str(j) for j in x]

    # time_list = []
    # i = 0
    # l_k = []
    # z = dict(zip(y,x))
    # for k in z.keys():
    #     l_k.append(k)

    # while i < N:
    #     ss = time.time()
    #     del z[l_k[i]]
    #     en = time.time()
    #     if N == 1000000 :
    #         i += 10000
    #         time_list.append(en - ss)
    #     elif N == 10000000 : 
    #         i += 100000
    #         time_list.append(en - ss)
    # return time_list
        

# import matplotlib.pyplot as plt
# %matplotlib inline
# x = list(range(0,len(monitorTime(1000000))))
# y = monitorTime(1000000)
# z = monitorTime(10000000)
# print(y)
# print(z)
# print(y[99])
# print(z[9])


# plt.plot(x,y)
# plt.plot(x,z)

def asd():
    return True,4567
print(asd()[0])
print(asd()[1])
y = asd()
print(type(y))

















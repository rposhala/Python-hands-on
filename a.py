def computeMedian():
    """
    The function has no input parameter, return median value of the list
    """
    # YOUR CODE HERE
    import math
    # infile = open('data_p2.txt','r')
    # line = infile.readline()filename = input('What is the name of the file? ')
    filename = input('What is the name of the file? ')
    with open(filename,'r') as f:
        med_list=[]
        i = 0
        j = 0
        for line in f:
            i += 1 
            while line:
            s = line.strip()
            d = {}

            try :
                med_list.append(float(s))
                    line = infile.readline()
            except Exception as error:
                print(error)
                j += 1
                    line = infile.readline()
                continue
        print(i)
        print(j)
        med_list.sort()
        l=len(med_list)
        if l % 2 == 0 :
            print((med_list[l/2] + med_list[(l/2)+1])/2)
        elif l % 2 != 0:
            print(med_list[math.floor(l/2)])

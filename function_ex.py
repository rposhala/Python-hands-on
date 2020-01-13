def calculate_distance(x1,y1,x2,y2):
    import math
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return distance

print(calculate_distance(4, 6, 28, 13))

point1 = (4,6)
point2 = (28,13)

def calculate_distance2(point1, point2):
    import math
    distance = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
    return distance

print(calculate_distance2(point1, point2))


def modify_point(point):
    point[0] = 10
    point[1] = 20
    print(point[0])

    return point

# print(modify_point(point1))

point_list = [4,6]
modify_point(point_list)
print(point_list)
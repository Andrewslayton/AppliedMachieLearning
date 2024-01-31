import matplotlib.pyplot as plt
from scipy.spatial import distance

x = [10, 16]
y = [9, 20] 
x2 = x[0] * 2, x[1] * 2
y2 = y[0] * 2, y[1] * 2
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

def EclideanDistance(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

def ManhattanDistance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

print(EclideanDistance(x,y))
print(EclideanDistance(x, y) == distance.euclidean(x, y))
print(EclideanDistance(x2, y2))
print(ManhattanDistance(x,y))
print(ManhattanDistance(x, y) == distance.cityblock(x, y))
print(ManhattanDistance(x2, y2))

from heapq import *

class Point:  
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __lt__(self, other): #because of this definition, we are less if our dist is greater...alternatively we could've made dist return a negative value 
    return self.dist() > other.dist()
  
  def dist(self): #don't need to worry about sqrt b/c the order will be the same
    return (self.x*self.x) + (self.y*self.y)

  def print_point(self):
    print('[' + str(self.x) + ', ' + str(self.y) + ']', end="")

def k_closest(points, k):
  result = []
  for i in range(k):
    heappush(result, points[i])

  for i in range(k, len(points)):
    if points[i].dist() < result[0].dist():
      heappop(result)
      heappush(result, points[i])
  return result

def main():

  result = k_closest([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()
  print()

  result = k_closest([Point(1, 2), Point(1, 3)], 1)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()
  print()


main()
from graphics import *
win = GraphWin("SkyScraper", 300, 300)
#win.yUp()

buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
min = buildings[0][0]
max = buildings[len(buildings)-1][1] + 1
yVals = []
xVals = []

def sort():
   for index in range(1,len(xVals)):
     currentvalueX = xVals[index]
     currentvalueY = yVals[index]
     position = index
     while position>0 and xVals[position-1]>currentvalueX:
         xVals[position] = xVals[position-1]
         yVals[position] = yVals[position-1]
         position = position-1
     xVals[position] = currentvalueX
     yVals[position] = currentvalueY
     
def makeOnlyPoints():
	rng = len(xVals)
	lastY = 0
	lastX = 0
	i = 0
	while i < rng:
		if yVals[i] == lastY:
			xVals.pop(i)
			yVals.pop(i)
			i -= 1
			rng -= 1
		else:
			if yVals[i] < lastY:
				lastX = xVals[i]-1
			else:
				lastX = xVals[i]
			xVals[i] = lastX
			lastY = yVals[i] 
		i += 1

for b in buildings:
	left = b[0]
	right = b[1]
	top = b[2]
	for i in range(left, right+1):
		if i in xVals:
			ind = xVals.index(i)
			if top > yVals[ind]:
				yVals[ind] = top
		else:
			xVals.append(i)
			yVals.append(top)
			
for i in range(min, max+1):
	if i not in xVals:
		xVals.append(i)
		yVals.append(0)

sort()
makeOnlyPoints()
print("Points")
for i in range(len(yVals)):
	print("X: " + str(xVals[i]) + ", Y: " + str(yVals[i]))
pt1 = Point(min*10, 300)
pt2 = Point(-1, -1)
for i in range(len(xVals)):
	X = xVals[i]*10
	Y = yVals[i]*10
	if i == len(xVals)-1:
		pt2 = Point(X, 300-Y)
		line = Line(pt1, pt2)
		line.draw(win)
	else:
		pt2 = Point(X, 300-Y)
		line = Line(pt1, pt2)
		line.draw(win)
		pt1 = Point(xVals[i+1]*10, 300-Y)
		line = Line(pt1, pt2)
		line.draw(win)
	
win.getMouse()
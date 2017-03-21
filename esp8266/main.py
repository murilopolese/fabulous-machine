from machine import Pin
from time import sleep

sequence = [
	[ 1, 0, 0, 0 ],
	[ 1, 1, 0, 0 ],
	[ 0, 1, 0, 0 ],
	[ 0, 1, 1, 0 ],
	[ 0, 0, 1, 0 ],
	[ 0, 0, 1, 1 ],
	[ 0, 0, 0, 1 ],
	[ 1, 0, 0, 1 ]
]

up = ( 1, 0 )
down = ( -1, 0 )
left = ( 0, 1 )
right = ( 0, - 1 )
upLeft = ( up[0] + left[0], up[1] + left[1] )
upRight = ( up[0] + right[0], up[1] + right[1] )
downLeft = ( down[0] + left[0], down[1] + left[1] )
downRight = ( down[0] + right[0], down[1] + right[1] )

left1 = Pin( 16, Pin.OUT )
left2 = Pin( 5, Pin.OUT )
left3 = Pin( 4, Pin.OUT )
left4 = Pin( 0, Pin.OUT )
right1 = Pin( 14, Pin.OUT )
right2 = Pin( 12, Pin.OUT )
right3 = Pin( 13, Pin.OUT )
right4 = Pin( 15, Pin.OUT )

speed = 0.005
scale = 2

def get_line(start, end):
	"""Bresenham's Line Algorithm
	Produces a list of tuples from start and end

	>>> points1 = get_line((0, 0), (3, 4))
	>>> points2 = get_line((3, 4), (0, 0))
	>>> assert(set(points1) == set(points2))
	>>> print points1
	[(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
	>>> print points2
	[(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
	"""
	# Setup initial conditions
	x1, y1 = start
	x2, y2 = end
	dx = x2 - x1
	dy = y2 - y1

	# Determine how steep the line is
	is_steep = abs(dy) > abs(dx)

	# Rotate line
	if is_steep:
		x1, y1 = y1, x1
		x2, y2 = y2, x2

	# Swap start and end points if necessary and store swap state
	swapped = False
	if x1 > x2:
		x1, x2 = x2, x1
		y1, y2 = y2, y1
		swapped = True

	# Recalculate differentials
	dx = x2 - x1
	dy = y2 - y1

	# Calculate error
	error = int(dx / 2.0)
	ystep = 1 if y1 < y2 else -1

	# Iterate over bounding box generating points between start and end
	y = y1
	points = []
	for x in range(x1, x2 + 1):
		coord = (y, x) if is_steep else (x, y)
		points.append(coord)
		error -= abs(dy)
		if error < 0:
			y += ystep
			error += dx

	# Reverse the list if the coordinates were swapped
	if swapped:
		points.reverse()
	return points

def runSequence( pin1, pin2, pin3, pin4, speed ):
	for seq in sequence:
		pin1.value( seq[ 0 ] )
		pin2.value( seq[ 1 ] )
		pin3.value( seq[ 2 ] )
		pin4.value( seq[ 3 ] )
		sleep( speed );

def cw( pin1, pin2, pin3, pin4, speed ):
	runSequence( pin4, pin3, pin2, pin1, speed )

def ccw( pin1, pin2, pin3, pin4, speed ):
	runSequence( pin1, pin2, pin3, pin4, speed )

def moveMotorLeft( v ):
	if v > 0:
		ccw( left1, left2, left3, left4, speed )
	elif v < 0:
		cw( left1, left2, left3, left4, speed )

def moveMotorRight( v ):
	if v > 0:
		ccw( right1, right2, right3, right4, speed )
	elif v < 0:
		cw( right1, right2, right3, right4, speed )

def move( x, y ):
	points = get_line( (0, 0), (x, y) )
	for index, point in enumerate( points ):
		if index > 0:
			d = ( point[0] - points[index-1][0], point[1] - points[index-1][1] )
			if d == up: # UP
				moveMotorRight(-1);
				moveMotorLeft(-1);
			elif d == down: # DOWN
				moveMotorRight(1);
				moveMotorLeft(1);
			elif d == right: # RIGHT
				moveMotorRight(-1);
				moveMotorLeft(1);
			elif d == left: # LEFT
				moveMotorRight(1);
				moveMotorLeft(-1);
			elif d == upRight: # UP RIGHT
				moveMotorRight(-1);
				moveMotorLeft(-1);
				moveMotorRight(-1);
				moveMotorLeft(1);
			elif d == upLeft: # UP LEFT
				moveMotorRight(-1);
				moveMotorLeft(-1);
				moveMotorRight(1);
				moveMotorLeft(-1);
			elif d == downRight: # DOWN RIGHT
				moveMotorRight(1);
				moveMotorLeft(1);
				moveMotorRight(-1);
				moveMotorLeft(1);
			elif d == downLeft: # DOWN LEFT
				moveMotorRight(1);
				moveMotorLeft(1);
				moveMotorRight(1);
				moveMotorLeft(-1);

def draw():
	with open( 'path.txt', 'r' ) as file:
		total = sum( 1 for line in open('path.txt') )
		for i, line in enumerate( file ):
			p = [ int(line.split(',')[0]), int(line.split(',')[1]) ]
			print( i, total, p )
			move( p[0]*scale, p[1]*scale )

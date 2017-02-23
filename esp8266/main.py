import machine
import time
import math

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

left1 = machine.Pin( 16, machine.Pin.OUT )
left2 = machine.Pin( 5, machine.Pin.OUT )
left3 = machine.Pin( 4, machine.Pin.OUT )
left4 = machine.Pin( 0, machine.Pin.OUT )
right1 = machine.Pin( 14, machine.Pin.OUT )
right2 = machine.Pin( 12, machine.Pin.OUT )
right3 = machine.Pin( 13, machine.Pin.OUT )
right4 = machine.Pin( 15, machine.Pin.OUT )

speed = 0.01

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
		time.sleep( speed );

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
			if d == ( 0, 1 ): # UP
				moveMotorRight(-1);
				moveMotorLeft(-1);
			elif d == ( 0, -1 ): # DOWN
				moveMotorRight(1);
				moveMotorLeft(1);
			elif d == ( 1, 0 ): # RIGHT
				moveMotorRight(-1);
				moveMotorLeft(1);
			elif d == ( -1, 0 ): # LEFT
				moveMotorRight(1);
				moveMotorLeft(-1);
			elif d == ( 1, 1 ): # UP RIGHT
				moveMotorRight(-1);
				moveMotorLeft(-1);
				moveMotorRight(-1);
				moveMotorLeft(1);
			elif d == ( -1, 1 ): # UP LEFT
				moveMotorRight(-1);
				moveMotorLeft(-1);
				moveMotorRight(1);
				moveMotorLeft(-1);
			elif d == ( 1, -1 ): # DOWN RIGHT
				moveMotorRight(1);
				moveMotorLeft(1);
				moveMotorRight(-1);
				moveMotorLeft(1);
			elif d == ( -1, -1 ): # DOWN LEFT
				moveMotorRight(1);
				moveMotorLeft(1);
				moveMotorRight(1);
				moveMotorLeft(-1);

def drawPath( path ):
	for p in path:
		move( p[0], p[1] )
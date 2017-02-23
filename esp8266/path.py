step = 25
while True:
	move( -step, step )
	move( -step, 0 )
	move( -step, -step )
	move( 0, -step )
	move( 3*step, -2*step )
	# half
	move( 3*step, 2*step )
	move( 0, step )
	move( -step, step )
	move( -step, 0 )
	move( -step, -step )

	move( 6*step, 0 )

while True:
	move( 10, 0 )
	move( 0, 10 )
	move( -10, 0 )
	move( 0, -10 )
	move( 20, 20 )
	move( 0, -10 )

while True:
move( 50, 0 )
move( 0, 50 )
move( -50, 0 )
move( 0, -50 )
move( 50, 50 )
move( 0, -50 )


pixelSize = 20

def drawPixel( fill, size ):
	n = size / fill
	for index in range( 0, n ):
		move( size*2, -fill )
		move( -size*2, -fill )

for y in range( 1, 5 ) :
	for x in range( 1, 5 ) :
		drawPixel( y*2, pixelSize )
	move( size*2, 0 )

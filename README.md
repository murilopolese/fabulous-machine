# Fabulous Machine

This is a project I have been working for long time now but finally got a nice
enough result. It's basically a [polargraph](http://www.polargraph.co.uk/)/[Makeangelo](http://www.makelangelo.com/)
machine that uses those [cheap 5V 28BYJ-48](http://www.ebay.com/itm/172406532344?_trksid=p2057872.m2749.l2649&ssPageName=STRK%3AMEBIDX%3AIT)
stepper motors and a [NodeMCU](http://www.ebay.com/itm/NodeMcu-Lua-WIFI-Internet-of-Things-development-board-based-ESP8266-/171907569391?hash=item28067d56ef:g:aYwAAOSwgkRVSiBa)
board with [MicroPython](https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/flash-firmware) running on it.

Well it's looking like this right now:
![](https://i.imgur.com/LL8bGl5.jpg)

## Building structure

This machine is pretty freestyle. I don't think it will look like this for longer
than a few weeks and the only part that is really tricky is the "gondola" (that
one holding the pen). Query this big library of knowledge named internet for
inspiration on how to build your own "polargraph", "makeangelo", "drawing machine"
gondola / pen holder.

The best instructions are written in your heart and you can watch them in your
dreams.

Boom!

## Flashing the flash-firmware

I love this expression. In fact, after you have ~flashing the MicroPython firmware~
(so hacker now) you just need to transfer the `boot.py`, `main.py` and just if you
want the `port_config.py`.

Set the wifi configuration on `boot.py` and the `port_config.py` for the webrepl
password.

## Tooling

Visit this [Fabulous Machine Website](http://fabulous-machine.herokuapp.com) to
draw your ideas and get the machine instructions!

## How to operate the machine

Make sure you have all the security equipment you will need, connect to your
ESP8266 through usb cable or webrepl (query how to do it on your favorite search
engine), and now you will can type `move(x, y)` replacing `x` and `y` by the
coordinates you want to move. Note that the origin (`0, 0`) is where the pen is.

You can also define a variable called `path` with an array of coordinates such as
`[[10.0], [-5,5], [5,5]]` and call `drawPath(path)`. It would look something like
this:

```
# Move the pen to 100 units up and 50 right, for example
move(100,50)
# Define your path
path = [[10.0], [-5,5], [5,5]]
# Draw the path, duh
drawPath(path)
```

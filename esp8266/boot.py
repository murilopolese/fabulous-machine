import network
import webrepl
import machine

machine.Pin( 2, machine.Pin.OUT ).low()
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
	print('connecting to network...')
	sta_if.active(True)
	sta_if.connect('wifiname', 'password')
	while not sta_if.isconnected():
		pass
print('network config:', sta_if.ifconfig())

webrepl.start()
machine.Pin( 2, machine.Pin.OUT ).high()

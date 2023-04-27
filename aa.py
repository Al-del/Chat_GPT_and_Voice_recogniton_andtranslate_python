
import serial
import time


# Reset the Arduino's line. This is key to getting the write to work.
# Without it, the first few writes don't work.
# Clear DTR, wait one second, flush input, then set DTR.
# Without this, the first write fails.
# This trick was learned from:
# https://github.com/miguelasd688/4-legged-robot-model
def ley():
	ser = serial.Serial("/dev/ttyACM0", 38400, timeout=1)
	ser.setDTR(False)
	time.sleep(1)
	ser.flushInput()
	ser.setDTR(True)
	time.sleep(2)

	while True:
		ser.write(b'1')

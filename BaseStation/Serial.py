__author__ = 'Stephen'
import serial
import io

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

count = 0
while True:
    msg = ser.readline()
    if 'ping' in msg:
        ser.write('pong')

    print(ser.readline())
    ser.write(b'asdf')

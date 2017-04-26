__author__ = 'Stephen'
import serial.tools.list_ports
import io
import time
import json
# from MLIotLibrary.Shared.Messages import Message

# ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
#
# count = 0
# while True:
#     msg = ser.readline()
#     if 'ping' in msg:
#         ser.write('pong')
#
#     print(ser.readline())
#     ser.write(b'asdf')
def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)

    return binary

input('Press key to begin')
print('checking current serial devices')
bports = {x.device: x for x in list(serial.tools.list_ports.comports())}
print('please plug in device')
time.sleep(3)
print('looking for device...')
aports = {x.device: x for x in list(serial.tools.list_ports.comports())}
ind = -1
available = set(aports.keys()) - set(bports.keys())
print(aports.keys())
if len(available) == 0:
    print('no device found')
elif len(available) == 1:
    ind = available.pop()
    print('using', ind, 'port')
else:
    print('There are {} devices available'.format(len(available)))
    print('\n'.join(available))
    i = input('please enter the index of device')
    ind = list(available)[i]

#msg = Message('asdf', 'asdf', 'adsf', 'adsf',[1,2,3], 0)

print('connecting to serial...')
ser = serial.Serial(ind, 57600)

print('fetching config')
j = dict_to_binary({'something':'hey'})
input('Execute config write? <Press Enter>')
print('writing to serial', j.encode('ascii'))
ser.write(str({'something':'hey'}).encode('ascii'))
ser.flush()
print('kill code')
# print(b'\x\r')
ser.write(b'\r')
ser.flush()


print('killing stream', str(b'4'))
# ser.write(b'4')
while True:
    line = ser.readline().strip()
    print(line)
    #if line != b'I received:':
        #print(line)
        #print(chr(int(line)))


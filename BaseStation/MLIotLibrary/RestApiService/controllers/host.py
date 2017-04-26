__author__ = 'Stephen'
from MLIotLibrary.RestApiService import app
from bottle import request, response
from json import dumps
from MLIotLibrary.Shared.Services.AuthService import authentication_wrapper as authenticate
from MLIotLibrary.Shared.Entities.NodeTelemetry import NodeTelemetry
from . import Lio
from . import SSEMsgs
from gevent.queue import Queue

import sys
import glob
import serial
import serial.tools.list_ports
import time





@app.get('/api/host/program')





def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print('before')
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)


    time.sleep(5)
    print('\n\nafter')
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)

   # print(serial_ports())





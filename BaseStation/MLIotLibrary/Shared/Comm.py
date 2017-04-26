__author__ = 'Stephen Strickland'
from .XBee import XBeeRadioManager
import threading
import multiprocessing
import queue
import multiprocessing as mp
import gevent.queue as gqueue
from enum import Enum

class COMM_TYPE(Enum):
    Thread = 0
    Process = 1
    Queue = 2


def setup_client_comm_method(comm):
    """ This method is used by the Lio init dunder
        This method sets the comm method used by the client
        There are 5 main types of comm methods clases that inherit Thread, Process
        and objects that are a queue.Queue, multiprocess.Queue, or gevent.Queue
    """
    xbee = XBeeRadioManager()
    xbee.setComm(get_comm_type(comm), comm)





def get_comm_type(comm):
    types = {
        type(threading.Thread): 0,
        type(mp.Process): 1,
        type(mp.Queue): 2,
        type(mp.Pipe): 3,
        type(queue.Queue): 4,
        type(gqueue.Queue): 5
    }

    return types.get(type(comm))
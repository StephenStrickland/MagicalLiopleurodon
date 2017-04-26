__author__ = 'Stephen'

import os
import glob
from ...Lio import Lio
from ..XBeeConsumer import XBeeMessageConsumer
from multiprocessing import Queue
SSEMsgs = Queue()
MessageQueue = Queue()
Lio = Lio()
Lio.setup(message_queue=MessageQueue)
__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

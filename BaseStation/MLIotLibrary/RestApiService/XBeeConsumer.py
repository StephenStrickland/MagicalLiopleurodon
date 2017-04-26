__author__ = 'Stephen'
import threading


# SSE "protocol" is described here: http://mzl.la/UPFyxY
class ServerSentEvent(object):
    def __init__(self, data):
        self.data = data
        self.event = None
        self.id = None
        self.desc_map = {
            self.data: "data",
            self.event: "event",
            self.id: "id"
        }

    def encode(self):
        if not self.data:
            return ""
        lines = ["%s: %s" % (v, k)
                 for k, v in self.desc_map.items() if k]

        return "%s\n\n" % "\n".join(lines)


class XBeeMessageConsumer(threading.Thread):
    def __init__(self, msgq, sseq):
        threading.Thread.__init__(self)
        self._msgq = msgq
        self._sseq = sseq



    def run(self):
        while True:
            msg = self._msgq.get()
            # do something with the message

            if isinstance(msg, str) and str == 'quit':
                # we are finished
                break
            self._sseq.put(msg)

        print('Closing XBee Message Consumer')


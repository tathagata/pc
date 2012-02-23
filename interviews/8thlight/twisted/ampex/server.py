from twisted.protocols import amp
from twisted.internet import reactor
from twisted.internet.protocol import Factory

class Sum(amp.Command):
    arguments = [('a', amp.Integer()),
                 ('b', amp.Integer())]
    response = [('total', amp.Integer())]

class Protocol(amp.AMP):
    @Sum.responder
    def sum(self, a, b):
	import time
	time.sleep(10)
        return {'total': a+b}

pf = Factory()
pf.protocol = Protocol
reactor.listenTCP(1234, pf) # listen on port 1234
reactor.run()


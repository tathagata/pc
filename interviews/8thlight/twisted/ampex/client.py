from twisted.internet import reactor
from twisted.internet.protocol import ClientCreator
from twisted.protocols import amp

class Sum(amp.Command):
    # normally shared by client and server code
    arguments = [('a', amp.Integer()),
                 ('b', amp.Integer())]
    response = [('total', amp.Integer())]

def connected(protocol):
    return protocol.callRemote(Sum, a=13, b=81
        ).addCallback(gotResult)

def gotResult(result):
    print 'total:', result['total']
    reactor.stop()

def error(reason):
    print "Something went wrong"
    print reason
    reactor.stop()

ClientCreator(reactor, amp.AMP).connectTCP(
    '127.0.0.1', 1234).addCallback(connected).addErrback(error)

reactor.run()


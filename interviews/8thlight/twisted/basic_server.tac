from twisted.protocols.amp import AMP
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.application.service import Application
from twisted.application.internet import StreamServerEndpointService

from twisted.protocols.amp import CommandLocator
from twisted.python.filepath import FilePath
from twisted.protocols.amp import Integer, String, Unicode, Command

class UsernameUnavailable(Exception):
	pass

class RegisterUser(Command):
    arguments = [('username', Unicode()),
                 ('publickey', String())]

    response = [('uid', Integer())]

    errors = {UsernameUnavailable: 'username-unavailable'}


class UserRegistration(CommandLocator):
	uidCounter = 0
	
	@RegisterUser.responder
	def register(self,username,publickey):
		path = FilePath(username)
		if path.exists():	
			raise UsernameUnavailable()
		self.uidCounter +=1
		path.setContent('%d %s\n' %(self.uidCounter, publickey))
		return self.uidCounter



application = Application("basic AMP server")

endpoint = TCP4ServerEndpoint(reactor, 8750)
factory = Factory()
factory.protocol = lambda: AMP(locator=UserRegistration())
service = StreamServerEndpointService(endpoint, factory)
service.setServiceParent(application)


from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class Echo(Protocol):

    def dataReceived(self, data):
        message = str(data)
        self.transport.write(message[::-1])
        
print ('Start my first hello world twisted application...')
print ('Use Ctrl+C for exit!')
reactor.run()
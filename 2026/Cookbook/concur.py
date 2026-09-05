from threading import Thread 

class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
    # sock is a socket
        sock.settimeout(5) # set timeout period
        while self._running:
            # Perform a blocking I/O operation w/timeout
            try:
                data = sock.recv(8192)
                break
            except sock.timeout:
                continue
            # Continued processing
        return

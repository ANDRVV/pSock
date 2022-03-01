# pSock

pSock is a socket / threading module that helps developers and students to approach Server-Client creation and much more.

Developed by Andrea Vaccaro from ANDRVV (c) 2022

# Installing

Linux, MacOS = ```pip3 install pSock```

Windows = ```pip install pSock```

# How To Create a Server

```python
from pSock_lib import pSock

def ToRunOnlyInConnection(conn):
    print("This is a server!")
    print(f"Active connections {sock.getactiveconnections}")
    while True:
        reiceved = sock.take(conn, codify = "utf-8", buffer = 2048)
        # The take function receives the entire message in a loop
        print(reiceved)
    sock.quit()


ip, port = "localhost", 80

sock = pSock.pSock(pSock.AF_INET, pSock.SOCK_STREAM)
sock.createserver([ip, port])
sock.listen(ToListen = 1)
while True:
    conn, addr = sock.accept()
    sock.start(ToRunOnlyInConnection(conn), [conn, addr])
```

# How To Create a Client

```python
from pSock_lib import pSock

ip, port = "localhost", 80

sock = pSock.pSock(pSock.AF_INET, pSock.SOCK_STREAM)
sock.connect([ip, port])

print("This is a client!")
while True:
    tosend = input("> ")
    sock.send(tosend, codify = "utf-8")
sock.quit()
```

# Other Commands And Methods

Receive host, address and active connections

```python
from pSock_lib import pSock

ip, port = "localhost", 80

sock = pSock.pSock(pSock.AF_INET, pSock.SOCK_STREAM)
sock.createserver([ip, port])

host = sock.gethost
addr = sock.getaddr
active_connections = sock.getactiveconnections
```

Sending without connections

```python
from pSock_lib import pSock

ip, port = "localhost", 80

sock = pSock.pSock(pSock.AF_INET, pSock.SOCK_STREAM)

tosend = input("> ")

sock.sendto(tosend, codify = "utf-8", ["localhost", 80])
```

Setting a temporary addr

```python
from pSock_lib import pSock

ip, port = "localhost", 80

sock = pSock.pSock(pSock.AF_INET, pSock.SOCK_STREAM)

tosend = input("> ")

sock.setaddr(["localhost", 80])
sock.sendto(tosend, codify = "utf-8")

tosend = input("> ")

sock.setaddr(["localhost", 334])
sock.sendto(tosend, codify = "utf-8")

sock.setaddr(["localhost", 334])
sock.createserver()

sock.cancelsets() # To delete the IP and ports set
```

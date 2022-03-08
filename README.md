# pSock

pSock is a socket / threading module that helps developers and students to approach Server-Client creation and much more.

Developed by Andrea Vaccaro from ANDRVV (c) 2022

# Installing

Linux, MacOS = ```pip3 install pSock --user```

Windows = ```pip install pSock --user```

# How To Create a Server

```python
import pSock

def ToRunOnlyInConnection(conn):
    print("This is a server!")
    print(f"Active connections {sock.getactiveconnections}")
    while True:
        received = sock.take(conn, codify = "utf-8", buffer = 2048)
        if received == "!quit":
            break
        print(received)
    sock.quit()


ip, port = "localhost", 80

sock = pSock.Net(pSock.AF_INET, pSock.SOCK_STREAM)
sock.createserver([ip, port])
sock.listen(ToListen = 1)
while True:
    conn, addr = sock.accept()
    sock.start(ToRunOnlyInConnection(conn), [conn, addr])
```

# How To Create a Client

```python
import pSock

ip, port = "localhost", 80

sock = pSock.Net(pSock.AF_INET, pSock.SOCK_STREAM)
sock.connect([ip, port])

print("This is a client!")
while True:
    tosend = input("> ")
    if tosend = "!quit":
        break
    sock.send(tosend, codify = "utf-8")
sock.quit()
```

# Web Scraping

```python
import pSock

pSock.Web.getresponsetext() 

json_data = pSock.Web.getresponsedata()
name = json_data[name]

to_find = {"class": "python-logo"}

to_research = pSock.Web.responsesearch("www.python.org", to_find)

```

# Other Commands And Methods

Receive info, local and remote

```python
from pSock_lib import pSock

ip, port = "localhost", 80

sock = pSock.Net(pSock.AF_INET, pSock.SOCK_STREAM)
sock.createserver([ip, port])

protocol_name = "udp"

host = sock.gethost
address = sock.getaddr
active_connections = sock.getactiveconnections # Output: int
active_connection_data = sock.getactiveconnectionsdata # Output: list/tuple

my_host_name = pSock.gethostname()
fully_domain_name = pSock.getfdname()
get_proto = pSock.getproto(protocol_name)
get_service = pSock.getservice(port) # Insert name or port
get_host_remote = pSock.gethost(ip) # Insert IP or name
```

Sending without connections

```python
import pSock

ip, port = "localhost", 80

sock = pSock.Net(pSock.AF_INET, pSock.SOCK_STREAM)

tosend = input("> ")

sock.sendto(tosend, codify = "utf-8", [ip, port])
```

Setting a temporary addr

```python
import pSock

ip, port = "localhost", 80

sock = pSock.Net(pSock.AF_INET, pSock.SOCK_STREAM)

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



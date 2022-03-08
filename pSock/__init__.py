__all__ = ["pSock"]
__version__ = "1.2.8"

# -*- coding: utf-8 -*-

# Copyright (c) 2022, Andrea Vaccaro. All rights reserved.
#BSD 3-Clause License
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#* Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
## * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the pSock authors nor the names of its contributors
#   may be used to endorse or promote products derived from this software without
#   specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""pSock is a socket / threading / web module that helps developers and students to approach Server-Client creation and much more."""

from . import _utils
from ._utils import *
import socket, threading, requests, json, bs4

# FAMILY ADDRESS

LIST_OF_FAMILY_ADDRESS = ["AF_UNIX", "AF_INET", "AF_INET6", "AF_APPLETALK", "AF_BLUETOOTH", "AF_IPX", "AF_IRDA", "AF_LINK", "AF_SNA", "AF_UNSPEC"]

AF_UNIX = socket.AddressFamily.AF_INET
AF_INET = socket.AddressFamily.AF_INET
AF_INET6 = socket.AddressFamily.AF_INET6
AF_APPLETALK = socket.AddressFamily.AF_APPLETALK
AF_BLUETOOTH = socket.AddressFamily.AF_BLUETOOTH
AF_IPX = socket.AddressFamily.AF_IPX
AF_IRDA = socket.AddressFamily.AF_IRDA
AF_LINK = socket.AddressFamily.AF_LINK
AF_SNA = socket.AddressFamily.AF_SNA
AF_UNSPEC = socket.AddressFamily.AF_UNSPEC
    
# SOCK TYPE

LIST_OF_SOCK_TYPE = ["SOCK_STREAM", "SOCK_DGRAM", "SOCK_RAW", "SOCK_RDM", "SOCK_SEQPACKET"]

SOCK_STREAM = socket.SocketKind.SOCK_STREAM 
SOCK_DGRAM = socket.SocketKind.SOCK_DGRAM
SOCK_RAW = socket.SocketKind.SOCK_RAW
SOCK_RDM = socket.SocketKind.SOCK_RDM
SOCK_SEQPACKET = socket.SocketKind.SOCK_SEQPACKET

class LocalFunction:
        def SelfData_Format(data):
            if str(data).find("AddressFamily.") != -1:
                newdata = str(data).replace("AddressFamily.", "")
                if newdata in LIST_OF_FAMILY_ADDRESS:
                    return True
                else:
                    return False
            elif str(data).find("SocketKind.") != -1:
                newdata = str(data).replace("SocketKind.", "")
                if newdata in LIST_OF_SOCK_TYPE:
                    return True
                else:
                    return False
            else:
                return False
  
class Web:
    def responsesearch(url, classandid = None):
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        elements = ["!DOCTYPE","html","body","h1","h2","h3","h4","h5","h6","p","br","hr","acronym","abbr","address","b","bdo","big","blockquote","center","cite","code","del","dfn","em","font","i","ins","kbd","pre","q","s","samp","small","strike","strong","sub","sup","tt","u","var","xmp","form","input","textarea","button","select","optgroup","option","label","fieldset","legend","isindex","frame","frameset","noframe","iframe","img","map","area","a","link","ul","ol","li","dir","dl","dt","dd","table","caption","th","tr","td","thead","tbody","tfoot","col","colgroup","style","div","span","head","title","meta","base","basefont","script","noscript","applet","object","param"]
        if classandid == None:
            for element in elements:
                try:
                    finded = soup.find(element)
                except:
                    pass
            return finded
        elif type(classandid) == dict:
            for element in elements:
                try:
                    finded = soup.find(element, classandid)
                except:
                    pass
            return finded
        else:
            raise SyntaxError(f"dict expected, not {type(classandid)}")

        
    def getresponsedata(url):
        response = response = requests.get(url).text
        responsedata = json.loads(response)
        return responsedata

    def getresponsetext(url):
        response = response = requests.get(url)
        return response.text

class Net:
    def __init__(self, AddressFamily = AF_INET, Sock = SOCK_STREAM, Address = [None, None]):
        """SOCKET = pSock.Net(ADDR-FAMILY, SOCK-TYPE, ADDRESS = [IP, PORT])"""
        if Address != [None, None]:
                if type(Address[0]) == str: 
                    if type(Address[1]) == int: 
                        self.ip, self.port = Address[0], Address[1]
                        self.netargs = True
                    else:
                        type1 = str(type(Address[1])).replace("<class '", "").replace("'>", "")
                        raise TypeError(f"int expected, not {type1}")
                else:
                    type2 = str(type(Address[0])).replace("<class '", "").replace("'>", "")
                    raise TypeError(f"str expected, not {type2}") 
        self.accepted = False
        self.netargs = False
        self.threadstarted = False    
        self.connection = False
        if LocalFunction.SelfData_Format(AddressFamily) == False:
            raise SyntaxError(f'Unknown topic "{AddressFamily}"') 
        elif LocalFunction.SelfData_Format(Sock) == False:
            raise SyntaxError(f'Unknown topic "{Sock}"') 
        self.sock = socket.socket(AddressFamily, Sock)

    def connect(self, Address = ["localhost", 80]):
        if self.netargs:
            self.sock.connect((str(self.ip), int(self.port)))
        else:
            self.ip, self.port = Address[0], Address[1]
            print((str(self.ip)+ str(self.port)))
            self.sock.connect((str(self.ip), int(self.port)))
        self.connection = True
        self.netargs = True

    def createserver(self, Address = ["localhost", 80]):
        if self.netargs:
            self.sock.bind((str(self.ip), int(self.port)))
        else:
            self.ip, self.port = Address[0], Address[1]
            self.sock.bind((str(self.ip), int(self.port)))
        self.connection = True
        self.netargs = True

    def setaddr(self, Address = ["localhost", 80]):
        self.ip, self.port = Address[0], Address[1]
        self.netargs = True

    def listen(self, ToListen = 1):
        if self.connection == True:
            self.sock.listen(ToListen)
        else:
            raise OSError("Unable to start an unestablished connection.")
    def accept(self):
        if self.connection == True:
            while True:
                try:
                    connection, address = self.sock.accept()
                    self.accepted = True
                    self.connectiondata, self.addressdata = connection, address
                    return connection, address
                except:
                            pass
        else:
            raise OSError("Unable to start an unestablished connection.")

    def start(self, FunctionName, Arguments):
        thread = threading.Thread(target = FunctionName, args=(Arguments))
        self.threadstarted = True
        thread.start()

    def take(self, connection, codify = "utf-8", buffer = 2048):
        if connection == None:
            connection = self.sock
        if self.connection and self.netargs:
            received = self.sock.recv(buffer) 
            return received.decode(codify) 
        else: 
            raise OSError("Unable to take an unestablished connection.") 

    def sendto(self, content, connection = None, codify = "utf-8", address = ["localhost", 80]):
        if connection == None:
            connection = self.sock
        tosend = str(content).encode(str(codify))
        ip, port = address[0], address[1]
        connection.sendto(tosend, ip, port)

    def send(self, content, connection = None, codify = "utf-8"):
        if connection == None:
            connection = self.sock
        if self.connection and self.netargs:
            tosend = str(content).encode(str(codify))
            connection.sendall(tosend)
        else:
            raise OSError("Unable to send an unestablished connection.")

    def cancelsets(self):
        self.ip = None
        self.port = None
        self.netargs = False     

    def quit(self):
        if self.connection == False:
            raise OSError("Unable to close an unestablished connection.")
        self.sock.close()
        self.connection = False
    
    @property
    def getactiveconnectionsdata(self):
        if self.accepted:
            return self.connectiondata, self.addressdata
        else:
            raise OSError("Unable to get active connection without accept().")
    @property
    def getactiveconnections(self):
        if self.threadstarted:
            return threading.active_count()
        else:
            raise OSError("Unable to get active connection without start().")
    @property
    def getaddr(self):
        return [x[4][0] for x in socket.getaddrinfo(self.ip, self.port)] if self.netargs == True else None
    @property
    def gethost(self):
        return socket.gethostbyaddr(self.ip) if self.netargs == True else None
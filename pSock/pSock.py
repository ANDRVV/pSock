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
# * Neither the name of the psutil authors nor the names of its contributors
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

"""pSock is a socket / threading module that helps developers and students to approach Server-Client creation and much more."""

import socket, threading, pSock

# FAMILY ADDRESS

global LIST_OF_FAMILY_ADDRESS
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

global LIST_OF_SOCK_TYPE
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
            
class pSock:

    def __init__(self, AddressFamily = pSock.AF_INET, Sock = pSock.SOCK_STREAM, Address = [None, None]):
        """SOCKET = pSock.pSock(ADDR-FAMILY, SOCK-TYPE, ADDRESS = [IP, PORT])"""
        if Address != [None, None]:
                if type(Address[0]) == str: 
                    if type(Address[1]) == int: 
                        self.ip, self.port = Address[0], Address[1]
                        self.netargs = False
                    else:
                        type1 = str(type(Address[1])).replace("<class '", "").replace("'>", "")
                        raise TypeError(f"int expected, not {type1}")
                else:
                    type2 = str(type(Address[0])).replace("<class '", "").replace("'>", "")
                    raise TypeError(f"str expected, not {type2}") 
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

    def start(self, FunctionName, ToListen = 1):
        if self.connection == True:
            self.sock.listen(ToListen)
            while True:
                connection, address = self.sock.accept()
                thread = threading.Thread(target = FunctionName, args=(connection, address))
                self.threadstarted = True
                thread.start() 
                return connection, address 
        else:
            raise OSError("Unable to start an unestablished connection.")

    def take(self, codify = "utf-8", buffer = 16):
        if self.connection and self.netargs:
            taked = ""
            while True:
                takeon16 = self.sock.recv(buffer)
                if len(takeon16) <= 0:
                    break
                taked += takeon16.decode(codify)
            if len(taked) > 0:
                return taked

    def sendto(self, content, codify = "utf-8", address = ["localhost", 80]):
        tosend = str(content).encode(str(codify))
        ip, port = address[0], address[1]
        self.sock.sendto(tosend, (ip, port))

    def send(self, content, codify = "utf-8"):
        if self.connection and self.netargs:
            tosend = str(content).encode(str(codify))
            self.sock.sendall(tosend)
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
    def getactiveconnections(self):
        return threading.active_count() - 1

    @property
    def getaddr(self):
        return [x[4][0] for x in socket.getaddrinfo(self.ip, self.port)] if self.netargs == True else None

    @property
    def gethost(self):
        return socket.gethostbyaddr(self.ip) if self.netargs == True else None
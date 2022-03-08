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

"""pSock is a socket / threading module that helps developers and students to approach Server-Client creation and much more."""

import socket, psutil, json, requests, string

def getipconfig():
    af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
    }
    n = 0
    data = {}
    response = json.loads(requests.get("https://www.ipinfo.io").text)
    data.update({"Address": [response["ip"], response["hostname"], [response["country"], response["region"], response["city"], response["loc"]], response["org"]]})
    for nick, addrs in psutil.net_if_addrs().items():
        if n == 0:
            nick = "Ethernet"
        elif n == 1:
            nick = "LAN"
        elif n == 2:
            nick = "LAN* 1"
        elif n == 3:
            nick = "LAN* 2"
        elif n == 4:
            nick = "Ethernet 2"
        elif n == 5:
            nick = "Wi-Fi"
        elif n == 6:
            nick = "Pseudo Interface"
        else:
            pass
        listofaddr = []
        for addr in addrs:
            listofaddr.append(addr.address)
        data.update({nick: listofaddr})
        del listofaddr
        n += 1
    return data

def getipconfigmap():
    af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
    }
    n = 0
    response = json.loads(requests.get("https://www.ipinfo.io").text)
    print("Address:")
    print("    IPv4 address   : "+response["ip"])
    print("    Hostname       : "+response["hostname"])     
    print("    Location       : "+response["country"]+", "+response["region"]+", "+response["city"]+" | "+response["loc"])   
    print("    Company        : "+response["org"])
    for nick, addrs in psutil.net_if_addrs().items():
        if n == 0:
            print("Ethernet:")
        elif n == 1:
            print("LAN:")
        elif n == 2:
            print("LAN* 1:")
        elif n == 3:
            print("LAN* 2:")
        elif n == 4:
            print("Ethernet 2:")
        elif n == 5:
            print("Wi-Fi:")
        elif n == 6:
            print("Pseudo Interface:")
        else:
            pass
        for addr in addrs:
            print("    %-4s" % af_map.get(addr.family, addr.family), end="")
            print(" address   : %s" % addr.address)
        n += 1
def gethostname():
    return socket.gethostname()

def getfdname():
    return socket.getfqdn(socket.gethostname())

def getproto(protocolname):
    return socket.getprotobyname(protocolname)
    
def getservice(nameorport):
    if type(nameorport) == str:
        return socket.getservbyname(nameorport)
    elif type(nameorport) == int:
        return socket.getservbyport(nameorport)
    else:
        raise AttributeError(f"str or int expected, not {type(nameorport)}")

def gethost(nameorip):
    try:
        host = socket.gethostbyaddr(nameorip)
        return host
    except:
        host = socket.gethostbyname(nameorip)
        return host
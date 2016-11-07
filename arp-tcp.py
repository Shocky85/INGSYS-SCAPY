#!/usr/bin/env python
 
import sys
from scapy.all import *
 

try:
	alive,dead=sr( IP(dst="192.168.43.45")/TCP(dport=80,flags="S") )

	alive.summary( lambda(s,r) : r.sprintf("%IP.src% is alive") )
except:
	pass
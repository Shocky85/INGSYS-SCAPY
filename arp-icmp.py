#!/usr/bin/env python
 
import sys
from scapy.all import *
 


try:
	alive,dead=sr(IP(dst="192.168.43.35-35")/ICMP())
	print "MAC - IP"

	alive.summary( lambda(s,r) : r.sprintf("%IP.src% is alive") )
except:
	pass
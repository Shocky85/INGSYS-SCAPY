#!/usr/bin/env python
 
import sys
from scapy.all import *
 
try:

	alive,dead= sr( IP(dst="192.168.43.218")/TCP(flags="S", dport=(1,1024)) )

	alive.nsummary( lfilter=lambda (s,r): (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )
except:
	pass
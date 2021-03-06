# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

import nmap
from lib import *

def p11211(portdic):
	p11211list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "11211":
			p11211list.append(do_nmap(ip[0]))
	return p11211list

def do_nmap(host_list):
	try:
		nm = nmap.PortScanner()
		b = nm.scan(hosts=host_list, arguments='-p 11211  -script memcached-info.nse')
		#a = nm[host_list]["tcp"][11211]["script"]['memcached-info']
		if  "memcached-info" and "Architecture" and "CPU" in str(b) :
			print(str(host_list)+'\t存在Memcached未授权访问漏洞')
			a = host_list+":11211:存在Memcached未授权访问漏洞"
			return a
	except:
		pass
# This script shows interfaces on the routers

from nornir_netmiko.connections import netmiko
from netmiko import ConnectHandler
from getpass import getpass

devices = [
	{
		'device_type': 'cisco_ios',
		'host'	     : '192.168.124.1',
		'username'   : 'cisco',
		'password'   : getpass()
	},
	{
		'device_type': 'juniper_junos',
		'host'       : '192.168.121.1',
		'username'   : 'ansible',
		'password'   : getpass()
	}
]

for device in devices:
	if device['device_type'] == 'cisco_ios':
		net_connect = ConnectHandler(**device)
		interfaces = net_connect.send_command('show ip int br')
		print(interfaces)
	elif device['device_type'] == 'juniper_junos':
		net_connect = ConnectHandler(**device)
		interfaces = net_connect.send_command('show interfaces terse')
		print(interfaces)





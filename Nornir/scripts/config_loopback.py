# This script configures a loopback interface on the routers if there is not one already

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

cisco_commands = ["interface loopback 0", "ip add 1.1.1.1 255.255.255.255"]
juniper_commands = ["set interfaces lo0 unit 0 family inet address 2.2.2.2/32"]

for device in devices:
	if device['device_type'] == 'cisco_ios':
		net_connect = ConnectHandler(**device)
		loopback_interface = net_connect.send_config_set(cisco_commands)
		loopback_interface += net_connect.save_config()
		print(loopback_interface)
	elif device['device_type'] == 'juniper_junos':
		net_connect = ConnectHandler(**device)
		loopback_interface = net_connect.send_config_set(juniper_commands)
		loopback_interface += net_connect.commit()
		print(loopback_interface)

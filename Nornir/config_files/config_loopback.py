# This script configures a loopback interface on the routers

from nornir import InitNornir
from nornir_utils.plugins.inventory import yaml_inventory
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config

nrn = InitNornir(config_file="config.yaml")

cisco_router = nrn.filter(name="Cisco")
juniper_router = nrn.filter(name="Juniper")

devices = [cisco_router, juniper_router]

for device in devices:
	if device == cisco_router:
		config_loopback = cisco_router.run(
			task=netmiko_send_config,
			config_commands=["int loopback0", "ip add 1.1.1.1 255.255.255.255"])
		print_result(config_loopback)
	elif device == juniper_router:
		config_loopback = juniper_router.run(
			task=netmiko_send_config,
			config_commands=["set interfaces lo0 unit 0 family inet address 2.2.2.2/32", "commit"])
		print_result(config_loopback)

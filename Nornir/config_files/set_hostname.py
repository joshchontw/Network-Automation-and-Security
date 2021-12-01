# This script configures a loopback interface on the routers

from nornir import InitNornir
from nornir_utils.plugins.inventory import yaml_inventory
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config

nrn = InitNornir(config_file="config.yaml")

arista1 = nrn.filter(name="Arista1")
arista2 = nrn.filter(name="Arista2")

switches = [arista1, arista2]

for i in range(2):
	set_hostname = switches[i].run(
		task=netmiko_send_config,
		config_commands=["hostname arista" + str(i+1)])
	print_result(set_hostname)

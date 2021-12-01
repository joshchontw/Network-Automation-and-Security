# This script shows the interfaces on the routers

from nornir import InitNornir
from nornir_utils.plugins.inventory import yaml_inventory
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

nrn = InitNornir(config_file="config.yaml")

cisco_router = nrn.filter(name="Cisco")
juniper_router = nrn.filter(name="Juniper")

devices = [cisco_router, juniper_router]

for device in devices:
	if device == cisco_router:
		show_interfaces = cisco_router.run(task=napalm_cli, commands=["show ip int br"])
		print_result(show_interfaces)
	elif device == juniper_router:
		show_interfaces = juniper_router.run(task=napalm_cli, commands=["show interfaces terse"])
		print_result(show_interfaces)

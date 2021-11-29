# Network automation using Ansible
Since the start of my schooling, I've known that automation was a big topic, that it was not a fad, and it was here to stay. In my eyes, the most prevalent tool for configuration management in the context of networking devices is and has been Ansible for a while. Join me as I try to become proficient at Ansible.

*NOTE: Details on continuous integration with Github Actions is documented in [ContinuousIntegration.md](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/ContinuousIntegration.md)*

-----------------------------------------------------------------------------------
### Task 1: Retrieving the version of the devices
After running [show_version.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbooks/show_version.yaml):

> In the interest of space, I will be showing snippets of the output, for this and all other tasks to come

![ciscoshowversion](https://user-images.githubusercontent.com/81763406/142037007-f3152ff2-3461-42a8-a89f-10bcf81a22cf.png)
![aristashowversion](https://user-images.githubusercontent.com/81763406/142037081-0b9d1ded-6966-4aaa-9864-2e6cbb9b8d0d.png)
![junipershowversion](https://user-images.githubusercontent.com/81763406/142037092-a54c56e8-cc6a-45af-984a-7b08c0433b4d.png)

Just with one playbook, I am able to connect to multi-vendor devices and retrieve the version they are running. This is admittedly relatively simple, but it shows the power and potential of Ansible.

---------------------------------------------------------------------
### Task 2: Creating VLANs on the switches and configuring Router-on-a-stick for the Cisco router
This task will configure the proper port types on the switch and create sub-interfaces on the Cisco router so that PC1 and PC2 can communicate with each other and the rest of the network.

> Ping (and failure) from PC1 to PC2 before running any VLAN configuration playbooks: 

![image](https://user-images.githubusercontent.com/81763406/143507543-520a9bd3-b36b-458e-b7e0-55d483811ded.png)

After running playbook [vlan_config.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbooks/vlan_config.yaml):
> Ping from PC1 to PC2 . The PC in VLAN100 is able to communicate with VLAN200 thanks to Router-on-a-stick capabilities of the Cisco router:

![image](https://user-images.githubusercontent.com/81763406/143508544-e1ee367c-869c-40b5-9fa0-815dc86da5de.png)

> Ping from PC2 to PC3 (in subnet 192.168.123.0/24):

![image](https://user-images.githubusercontent.com/81763406/143511480-790a8b53-6335-4d71-a07c-f76e67c3db15.png)

> Showing the sub-interfaces on the Cisco router:

![image](https://user-images.githubusercontent.com/81763406/143508564-83eb1155-3d01-4bb0-b8a0-ac88b5cb4263.png)

> Showing the trunk and access ports on the Arista switch:

![image](https://user-images.githubusercontent.com/81763406/143508612-157b9182-4b24-49cc-b6e3-c9ea1a38049f.png)

By running [vlan_config.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbooks/vlan_config.yaml), the control machine is able to SSH into the network devices and apply VLAN configuration all at once.

----------------------------------------
### Task 3: Changing the routing protcol from RIP to OSPF
This task transitions the network from RIP to OSPF.
Attached are the routing tables for the routers, before the switch to OSPF. These routing tables were saved to text files, after running the playbook [save_route_table.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbooks/save_route_table.yaml):
> As we can see from the output, the routing protocol in place is RIP:

![image](https://user-images.githubusercontent.com/81763406/143772688-d6c0e6c6-ee41-4b90-94b0-bc48e829aa47.png)
![image](https://user-images.githubusercontent.com/81763406/143772766-1313c381-bc16-4f84-aeed-0752025e032c.png)

After running the playbooks [ospf_config.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbooks/ospf_config.yaml) and [save_route_table.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbooks/save_route_table.yaml):
> The routers are now learning their routes through OSPF:

![image](https://user-images.githubusercontent.com/81763406/143772798-71f3281a-b9d2-4646-9f0d-4b998fb81a10.png)
![image](https://user-images.githubusercontent.com/81763406/143772825-ca7db1aa-9eda-4b90-ad59-a32383d2cdd3.png)

-----------------------------------------
### Task 4: Controlling traffic on the routers
This task adds ACLs on the Cisco and Juniper routers to deny pings from PC1 and PC2 to PC3. To do this, the Cisco router will deny PC1 traffic outbound and the Juniper router will deny PC2 traffic inbound.

For the ACL on the Cisco router, I will add an entry to permit traffic from PC2 outbound, in addition to the entry denying traffic from PC1. This is because ACLs have an implcity deny all rule by default. 

After running [traffic_control.yaml](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Ansible/playbook_files/traffic_control.yaml):
> Traffic from PC1 to PC3 is denied:

![image](https://user-images.githubusercontent.com/81763406/143799114-8de490e7-7af5-4e22-82fa-51b8c5474e05.png)

> Traffic from PC2 to PC3 is denied:

![image](https://user-images.githubusercontent.com/81763406/143908756-2510b0dd-405f-4f0f-bacb-913311d33149.png)

> Showing the ACL on the Cisco router and it being applied outbound on FastEthernet2/0:

![image](https://user-images.githubusercontent.com/81763406/143799163-3b41db69-e034-4d84-9fcb-8d3951b36486.png)
![image](https://user-images.githubusercontent.com/81763406/143908972-2cb160c7-8c66-4419-8fd1-ee6af3314d76.png)

> Showing the ACL on the Juniper router and it being applied outbound on Ethernet3:

![image](https://user-images.githubusercontent.com/81763406/143909156-63d1fdc0-a16f-4274-90e0-90d8973684eb.png)
![image](https://user-images.githubusercontent.com/81763406/143909313-292036d0-9904-4699-89e5-4f964d7b0a2f.png)

I apply the ACL outbound on Ethernet3 of the Juniper router because I only want to deny traffic from PC2. If I applied the ACL inbound on Ethernet2, I would need to add entries allowing traffic from our control node, which is unnecessary. 

> Ping from PC2 to Ethernet2 of the Juniper router, showing our ACL is applied in the right place:

![image](https://user-images.githubusercontent.com/81763406/143909977-634d59a2-a22c-4196-89e6-254bd11acf18.png)





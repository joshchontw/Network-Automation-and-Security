# Start of the network/infrastructure automation journey
Since the start of my schooling, I've known that automation was a big topic, that it was not a fad, and it was here to stay. In my eyes, the most prevalent tool for configuration management in the context of networking devices is and has been Ansible for a while. Join me as I try to become proficient at Ansible and earn a gold star, which would be my greatest accomplishment in life... :D
##### NOTE 1: Firewall setup is documented in FortiGateFW.md
##### NOTE 2: Details on continuous integration with Github Actions is documented in YAML-Lint.md
## My Lab
![image](https://user-images.githubusercontent.com/81763406/143507462-a1daa6ba-988c-4baa-ab8f-b310cca5a934.png)

In my lab, there is a Cisco and Juniper router, a FortiGate firewall, and three Arista switches. I will be using Ansible to connect to all devices (except the firewall) and perform various commands. I specifically set out to create a multi-vendor environment because while one company may use a Cisco-heavy stack, another company may prefer Juniper, and so on. 

### Task 1: Retrieving the version of the devices
##### After running 'ansible-playbook show_version.yaml'

> In the interest of space, I will be showing snippets of the output, for this and all other tasks to come

![ciscoshowversion](https://user-images.githubusercontent.com/81763406/142037007-f3152ff2-3461-42a8-a89f-10bcf81a22cf.png)
![aristashowversion](https://user-images.githubusercontent.com/81763406/142037081-0b9d1ded-6966-4aaa-9864-2e6cbb9b8d0d.png)
![junipershowversion](https://user-images.githubusercontent.com/81763406/142037092-a54c56e8-cc6a-45af-984a-7b08c0433b4d.png)

#### Just with one playbook, I am able to connect to multiple devices (different vendors also) and retrieve the version they are running. This is admittedly relatively simple, but it shows the power and potential of Ansible.
---------------------------------------------------------------------
### Task 2: Creating VLANs on the switches and configuring Router-on-a-stick for the Cisco router
This task will configure the proper port types on the switch and create sub-interfaces on the Cisco router so that PC1 and PC2 can communicate with each other and the rest of the network.

> Ping (and failure) from PC1 to PC2 before running any VLAN configuration playbooks: 

![image](https://user-images.githubusercontent.com/81763406/143507543-520a9bd3-b36b-458e-b7e0-55d483811ded.png)

> Ping from PC1 to PC2 after running playbook 'vlan_config.yaml'. The PC in VLAN100 is able to communicate with VLAN200 thanks to ROAS:

![image](https://user-images.githubusercontent.com/81763406/143508544-e1ee367c-869c-40b5-9fa0-815dc86da5de.png)

> Ping from PC2 to PC3 (in subnet 192.168.123.0/24):

![image](https://user-images.githubusercontent.com/81763406/143511480-790a8b53-6335-4d71-a07c-f76e67c3db15.png)

> Showing the sub-interfaces on the Cisco router:

![image](https://user-images.githubusercontent.com/81763406/143508564-83eb1155-3d01-4bb0-b8a0-ac88b5cb4263.png)

> Showing the trunk and access ports on the Arista switch:

![image](https://user-images.githubusercontent.com/81763406/143508612-157b9182-4b24-49cc-b6e3-c9ea1a38049f.png)

#### With the 'vlan_config.yaml', the control machine is able to SSH into the network devices and apply VLAN configuration all at once.
----------------------------------------
### Task 3: Changing the routing protcol from RIP to OSPF
This task transitions the network from RIP to OSPF.
Attached are the routing tables for the routers, before the switch to OSPF. These routing tables were saved to text files, after running the command 'ansible-playbook save_route_table.yaml':

![image](https://user-images.githubusercontent.com/81763406/143508748-089d165f-8569-43ac-ad73-890e5df56738.png)
![image](https://user-images.githubusercontent.com/81763406/143508766-75b83f06-68d8-4b77-b0fc-bd4534e9b47d.png)

> As we can see from the output, the routing protocol in place is RIP.

#### After running 'ansible-playbook ospf_config.yaml' and 'save_route_table.yaml'
![image](https://user-images.githubusercontent.com/81763406/143509179-05fa36a1-7d6c-4928-97d0-17f0db284078.png)
![image](https://user-images.githubusercontent.com/81763406/143509201-58d74573-5b09-4b15-8930-87ac422d6d5d.png)

> The routers are now learning their routes through OSPF
-----------------------------------------
### Task 4: Adding access control lists on the routers

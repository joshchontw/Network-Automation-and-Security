# Start of the network/infrastructure automation journey
Since the start of my schooling, I've known that automation was a big topic, that it was not a fad, and it was here to stay. In my eyes, the most prevalent tool for configuration management in the context of networking devices is and has been Ansible for a while. Join me as I try to become proficient at Ansible and earn a gold star, which would be my greatest accomplishment in life... :D
##### NOTE: Firewall setup will be documented in FortigateFW.md
## My Lab
![image](https://user-images.githubusercontent.com/81763406/143357359-0d3b9952-06a9-46cb-8a1c-3a5dd1579aea.png)

In my lab, there is a Cisco and Juniper router, a FortiGate firewall, and three Arista switches. I will be using Ansible to connect to all devices and perform various commands. I specifically set out to create a multi-vendor environment because while one company may use a Cisco-heavy stack, another company may prefer Juniper, and so on. 

### Task 1: Retrieving the version of the devices
##### After running 'ansible-playbook show_version.yaml'

> In the interest of space, I will be showing snippets of the output, for this and all other tasks to come

![ciscoshowversion](https://user-images.githubusercontent.com/81763406/142037007-f3152ff2-3461-42a8-a89f-10bcf81a22cf.png)
![aristashowversion](https://user-images.githubusercontent.com/81763406/142037081-0b9d1ded-6966-4aaa-9864-2e6cbb9b8d0d.png)
![junipershowversion](https://user-images.githubusercontent.com/81763406/142037092-a54c56e8-cc6a-45af-984a-7b08c0433b4d.png)

Just with one playbook, I am able to connect to multiple devices (different vendors also) and retrieve the version they are running. This is admittedly relatively simple, but it shows the power and potential of Ansible.

### Task 2: Changing the routing protcol from RIP to OSPF
With Ansible, I will transition the network from RIP to OSPF.
Attached are the routing tables for the routers, before the switch to OSPF. These routing tables were saved to text files, after running the command 'ansible-playbook show_route_table.yaml'.

![routetablecisco](https://user-images.githubusercontent.com/81763406/142063444-375c68e6-4e9b-427d-baa0-380df4283d36.png)
![routetablejuniper](https://user-images.githubusercontent.com/81763406/142063457-7a8bf1f5-53a7-4994-8c8b-75b95a0ae52f.png)

> As we can see from the output, the routing protocol in place is RIP.

#### After running 'ansible-playbook ospf_config.yaml' and 'show_route_table.yaml'
![image](https://user-images.githubusercontent.com/81763406/143314284-d215610e-2fd9-4e3a-8418-a1e2292ac3d1.png)
![image](https://user-images.githubusercontent.com/81763406/143314369-dbe9569a-2990-4eb3-86ca-c65f3d83b0e1.png)

> The routers are now learning their routes through OSPF


# S144HomeLab
## Start of the network/infrastructure automation journey

![LabTopology](https://user-images.githubusercontent.com/81763406/142034957-8396695a-9d2b-435e-99ef-abcc7c951b6f.png)

Since the start of my schooling, I've known that automation was a big topic, that it was not a fad, and it was here to stay. In my eyes, the most prevalent tool for configuration management in the context of networking devices is and has been Ansible for a while. Join me as I try to become proficient at Ansible and earn a gold star, which would be my greatest accomplishment in life... :D
## My Lab
In my lab, there is a Cisco and Juniper router, along with three Arista switches. I will be using Ansible to connect to all devices and perform various commands. I specifically set out to create a multi-vendor environment because while one company may use a Cisco-heavy stack, another company may prefer Juniper, and so on. 

### Task 1: Retrieving the version of the devices
##### After running 'ansible-playbook show_version.yaml'

> In the interest of space, I will be showing snippets of the output, for this and all other tasks to come

![ciscoshowversion](https://user-images.githubusercontent.com/81763406/142037007-f3152ff2-3461-42a8-a89f-10bcf81a22cf.png)
![aristashowversion](https://user-images.githubusercontent.com/81763406/142037081-0b9d1ded-6966-4aaa-9864-2e6cbb9b8d0d.png)
![junipershowversion](https://user-images.githubusercontent.com/81763406/142037092-a54c56e8-cc6a-45af-984a-7b08c0433b4d.png)

Just with one playbook, I am able to connect to multiple devices (different vendors also) and retrieve the version they are running. This is admittedly relatively simple, but it shows the power of Ansible.

### Task 2: Changing the routing protcol from RIP to OSPF


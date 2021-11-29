# Start of the network/infrastructure automation journey
This repository contains details on automating a network using [Ansible](https://github.com/joshchontw/NetworkAutomationSecurityLab/tree/main/Ansible) and [Nornir](https://github.com/joshchontw/NetworkAutomationSecurityLab/tree/main/Nornir) (a Python library).

## My Lab
![image](https://user-images.githubusercontent.com/81763406/143507462-a1daa6ba-988c-4baa-ab8f-b310cca5a934.png)

In my lab, there is a Cisco and Juniper router, a FortiGate firewall, and two Arista switches. I specifically set out to create a multi-vendor environment because while one company may use a Cisco-heavy stack, another company may prefer Juniper, and so on. 

I am able to interact with Git and make changes to this repository with the ControlNode via the NAT node. The NAT node gives the ControlNode internet connectivity. 

---------------------------------------------------------
# Fortigate Firewall setup

> Main dashboard of the GUI:

![image](https://user-images.githubusercontent.com/81763406/143358495-179c92a8-79d6-4816-8fb7-c28d98eef744.png)

> Firewall interfaces:

![image](https://user-images.githubusercontent.com/81763406/143498973-7fbd2848-1dc3-498a-916e-02c44c27c96f.png)
------------------------------------------------------

## Rule to allow the control node to SSH into the devices and perform commands
![image](https://user-images.githubusercontent.com/81763406/143372911-0c958854-deb6-4e9d-bf28-0fa0b1ae0c3f.png)
In our case, the service has to be set to 'ALL'. Ansible remotely logs into Juniper devices not through the SSH port of 22, but rather port 830 for Netconf. This FortiGate firewall is unable to specify port 830/Netconf as a service, hence the need to set the service to all allowed.

> Details of the source and destination parameters:

![image](https://user-images.githubusercontent.com/81763406/143490466-08da7a44-caa4-429a-a5dc-bf77cc7b0669.png)
![image](https://user-images.githubusercontent.com/81763406/143372978-54e627a1-b599-4929-922d-9807beded2b4.png)

Just enabling this rule will not allow our control node to remotely access our network devices. For that, we have to enable OSPF on the FortiGate firewall, to learn and share routes with the whole network.

------------------------------------------------

## OSPF configuration on the firewall
![image](https://user-images.githubusercontent.com/81763406/143462999-40b651ad-80b9-4797-9c06-ec6752649ba8.png)

> Output showing that the Cisco router learned the route to 192.168.125.0/24 via OSPF:

![image](https://user-images.githubusercontent.com/81763406/143498731-c3ec7fb2-9a26-4ae8-9c82-8f7f22abc376.png)

> Output showing that the control node can ping our Cisco router:

![image](https://user-images.githubusercontent.com/81763406/143498833-6fc5930c-1ca4-4a13-b035-b386ec37966f.png)

> Output showing that the control node CANNOT ping PC5 (by design). We only need the control node to SSH into network devices:

![image](https://user-images.githubusercontent.com/81763406/143499109-0d92ef7f-4f70-4bb7-b3e8-50683a8d806a.png)

All of this shows that the firewall is not preventing our control node from accessing our network. For our purposes, the firewall serves its purpose. I am well aware that in a real production network, there would be far more stringent controls needed to be applied.

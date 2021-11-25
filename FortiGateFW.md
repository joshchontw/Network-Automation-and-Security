# Fortigate Firewall setup

> Main dashboard of the GUI

![image](https://user-images.githubusercontent.com/81763406/143358495-179c92a8-79d6-4816-8fb7-c28d98eef744.png)

## Rule to allow the control node to SSH into the devices and perform commands
![image](https://user-images.githubusercontent.com/81763406/143372911-0c958854-deb6-4e9d-bf28-0fa0b1ae0c3f.png)
In our case, the service has to be set to 'ALL'. Ansible remotely logs into Juniper devices not through the SSH port of 22, but rather port 830 for Netconf. This FortiGate firewall is unable to specify port 830/Netconf as a service, hence the need to set the service to all allowed.

> Details of the source and destination parameters

![image](https://user-images.githubusercontent.com/81763406/143490466-08da7a44-caa4-429a-a5dc-bf77cc7b0669.png)
![image](https://user-images.githubusercontent.com/81763406/143372978-54e627a1-b599-4929-922d-9807beded2b4.png)

Just enabling this rule will not allow our control node to remotely access our network devices. For that, we have to enable OSPF on the FortiGate firewall, to learn and share routes with the whole network.
## OSPF configuration on the router
![image](https://user-images.githubusercontent.com/81763406/143462999-40b651ad-80b9-4797-9c06-ec6752649ba8.png)

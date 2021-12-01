# Network Automating using Nornir
Nornir, like Ansible, is a configuration management tool. Where Nornir differs from Ansible is it is a Python library, as and it offers concurrency. 
Where Ansible logs into one device at a time, Nornir logs into all devices specified at once and performs changes
My lab won't benefit as I am at most performing changes on four devices, but in a production network with hundreds or thousands of devices, Nornir blows Ansible out of the water for speed and efficiency.
As there are pros and cons to both, there is no need to 'pick' one over the other; it is beneficial to use both for different scenarios.

---------------------------------------------------------------
### Task 1: Showing the interfaces on the routers
After running [show_interfaces.py](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Nornir/scripts/show_interfaces.py):

![image](https://user-images.githubusercontent.com/81763406/144261150-94e2e238-7290-4f02-8848-1defd0ddf4b2.png)

I've set up the script to ask for the passwords of the two respective routers, instead of hardcoding it. Compared to doing this task on Ansible, Nornir does it much quicker.

### Task 2: Configuring a loopback interface on the routers
After running [config_loopback.py](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Nornir/scripts/config_loopback.py):

![image](https://user-images.githubusercontent.com/81763406/144262203-e03007d7-0801-4063-b354-c38900f1d6e9.png)
![image](https://user-images.githubusercontent.com/81763406/144262296-b8d7f254-cbd6-448a-ad30-8e6afd8d5a09.png)


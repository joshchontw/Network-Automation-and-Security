# Network Automating using Nornir
Nornir, like Ansible, is a configuration management tool. Nornir is a Python library and it offers concurrency, unlike Ansible. 
Where Ansible logs into one device at a time, Nornir logs into all devices specified at once and performs changes.
My lab won't benefit as I am at most performing changes on four devices, but in a production network with hundreds or thousands of devices, Nornir blows Ansible out of the water for speed and efficiency.
As there are pros and cons to both, there is no need to 'pick' one over the other; it is beneficial to use both for different scenarios.

---------------------------------------------------------------
### Task 1: Showing the interfaces on the routers
After running [show_interfaces.py](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Nornir/config_files/show_interfaces.py):
> In the interest of space, I will be showing snippets of the output, for this and all other tasks to come

![image](https://user-images.githubusercontent.com/81763406/144286978-63e997e2-06a9-4151-98d0-76232dc0e44e.png)
![image](https://user-images.githubusercontent.com/81763406/144287061-93b5c5a7-f021-49d9-a5ca-e3c2c2e8e864.png)

### Task 2: Configuring a loopback interface on the routers
After running [config_loopback.py](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Nornir/config_files/config_loopback.py):

![image](https://user-images.githubusercontent.com/81763406/144287256-ce511f60-34a2-4178-8d51-f6af48feb03e.png)

### Task 3: Setting hostnames on the Arista switches
After running [set_hostname.py](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Nornir/config_files/set_hostname.py):

![image](https://user-images.githubusercontent.com/81763406/144306256-1c4227ab-4c77-4777-aa07-092566236a56.png)



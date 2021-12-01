# Network Automating using Nornir
Nornir, like Ansible, is a configuration management tool. Where Nornir differs from Ansible is it is a Python library, as and it offers concurrency. 
Where Ansible logs into one device at a time, Nornir logs into all devices specified at once and performs changes
My lab won't benefit as I am at most performing changes on four devices, but in a production network with hundreds or thousands of devices, Nornir blows Ansible out of the water for speed and efficiency.
As there are pros and cons to both, there is no need to 'pick' one over the other; it is beneficial to use both for different scenarios.

---------------------------------------------------------------
### Task 1: Showing the interfaces on the routers
After running [show_interfaces.py](https://github.com/joshchontw/NetworkAutomationSecurityLab/blob/main/Nornir/scripts/show_interfaces.py)

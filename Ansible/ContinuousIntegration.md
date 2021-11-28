# Continuos Integration, Continuous Deployment/Delivery
A lot of modern workplaces have fully adopted and embraced the concept of DevOps, where the development team and IT operations team are no longer separated from each other. It is imperative that the development team can make consistent and seamless pushes of code to production. 

To do this, DevOps engineers are tasked with making sure the CI/CD process is smooth, meaning code is properly tested before it is integrated into the 'main' production version. This is obviously crucial. Without a good CI/CD pipeline, there would be many bugs and faults in the production version of an application. It would be akin to displaying cuts of beef on the main display without first checking and trimming the pieces.

For my project, I have enlisted a module in GitHub Actions called yaml-lint to help examine the YAML Ansible playbooks for correct syntax. This project only ticks off the CI requirement of the CI/CD pipeline, the CD part is a work-in-progress. 

Lint tests can be initiated with a commit or pull request. Since I am the sole contributor to my project, I will trigger the test by pushing a commit to the main branch.
> Kicking off a lint test with a commit:

![image](https://user-images.githubusercontent.com/81763406/143791152-28a2f88f-07d3-4726-bde7-4e7af82b0d6d.png)

As we can see in lines 24 and 25, there are syntax errors in the 'ospf_config.yaml' file. The two errors are trailing spaces and too many blank lines. What's nice with this module is that it tells you the lines where the syntax errors have occurred. I will go and fix those syntax errors and push the updated changes, which will kick off another lint test.

> And voila, there aren't any syntax errors:

![image](https://user-images.githubusercontent.com/81763406/143791126-c310cbe7-65ed-4265-9b1b-37cd5c388c81.png)

This short example shows that a good CI/CD pipeline is of the utmost importance. It will give developers the peace of mind that any mistakes will be caught, and the IT operations can rest assured that there is another set of eyes helping to deploy and integrate code.

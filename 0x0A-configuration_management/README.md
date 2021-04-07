## **0x0A-configuration_management**
The tasks on this folder are based on Puppet code.
Puppet helps to restore  infrastructure to normal operation without having to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs

This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet

### **0-create_a_file.pp**
Using Puppet, create a file in /tmp.

Requirements:

    File path is /tmp/holberton
    File permission is 0744
    File owner is www-data
    File group is www-data
    File contains I love Puppet


### **1-install_a_package.pp**
Using Puppet, install puppet-lint.

Requirements:

    Install puppet-lint
    Version must be 2.1.1

### **2-execute_a_command.pp**
Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

    Must use the exec Puppet resource
    Must use pkill

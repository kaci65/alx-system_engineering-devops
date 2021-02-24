## **0x08-networking_basics_2**
Resources:

    What is localhost
    What is 0.0.0.0
    What is the hosts file
    Netcat examples

man or help:

    ifconfig
    telnet
    nc
    cut

### ** 2-change_your_home_IP**
Bash script that configures an Ubuntu server with the below requirements

Requirements:

    localhost resolves to 127.0.0.2
    facebook.com resolves to 8.8.8.8.
    The checker is running on Docker, so make sure to read this

### **3-show_attached_IPs**
Bash script that displays all active IPv4 IPs on the machine it’s executed on

NB. the IPs displayed may be different depending on which machine you are running the script on

### **4-port_listening_on_localhost** - advanced task
Bash script that listens on port 98 on localhost
Terminal 0

Starting script:
```
xyz@ubuntu$ sudo ./4-port_listening_on_localhost
```

Terminal 1

Connecting to localhost on port 98 using telnet. Type some text
```
xyz@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

Terminal 0

Receiving the text on the other side
```
xyz@ubuntu$ sudo ./4-port_listening_on_localhost
Hello world
test
```

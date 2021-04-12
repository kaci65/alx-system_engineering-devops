## 880x0F-load_balancer**
Load Balancers help handle huge amounts of web traffic by distributing it to multiple servers

### **Resources**

    Introduction to load-balancing and HAproxy<https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts>
    HTTP header<https://www.techopedia.com/definition/27178/http-header>
    Debian/Ubuntu HAProxy packages<https://haproxy.debian.net/>

### **Tasks**
### **0-custom_http_response_header**
Requirements:

    Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
        The name of the custom HTTP header must be X-Served-By
        The value of the custom HTTP header must be the hostname of the server Nginx is running on
    Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task 

### **1-install_load_balancer**
Install and configure HAproxy on your lb-01 server.

Requirements:

    Configure HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
    Distribute requests using a roundrobin algorithm
    Make sure that HAproxy can be managed via an init script
    Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this tutorial.
    For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

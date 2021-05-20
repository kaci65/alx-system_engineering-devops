## **0x18-webstack_monitoring**
Web stack monitoring can be broken down into 2 categories:

    Application monitoring: getting data about your running software and making sure it is behaving as expected
    Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

### **Resources**

    What is server monitoring<https://www.sumologic.com/glossary/server-monitoring/>
    What is application monitoring<https://en.wikipedia.org/wiki/Application_performance_management>
    System monitoring by Google<https://sre.google/sre-book/monitoring-distributed-systems/>
    Nginx logging and monitoring<https://docs.nginx.com/nginx/admin-guide/monitoring/logging/>

### **Learning Outcomes**

    Why is monitoring needed
    What are the 2 main area of monitoring
    What are access logs for a web server (such as Nginx)
    What are error logs for a web server (such as Nginx)

### **Tasks**
#### **0x18-webstack_monitoring**

    Sign up for Datadog - Please make sure you are using the US website of Datagog (.com)
    Install datadog-agent on web-01
    Create an application key
    Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
    Your server web-01 should be visible in Datadog under the host name XX-web-01
        You can validate it by using this API
        If needed, you will need to update the hostname of your server

#### **0x18-webstack_monitoring**
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check<https://docs.datadoghq.com/integrations/system/>

    Set up a monitor that checks the number of read requests issued to the device per second.
    Set up a monitor that checks the number of write requests issued to the device per second.

#### **2-setup_datadog**
create a dashboard with different metrics displayed in order to get a few different visualizations.

    Create a new dashboard
    Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
    Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API<https://docs.datadoghq.com/api/latest/dashboards/#get-all-dashboards>


**Description**
This is a a secured and monitored distributed web infrastructure design with three servers that host a website with the alias www.foobar.com at the ip address 8.8.8.8. Each component of this infrastructure uses the same resource.

**Secured and Monitored web infrastructure**

**Specifics about this web infrastructure**


    For every additional element, why you are adding it
	We added 3 firewalls and 3 monitoring systems and 1 SSL certificate for the infrastructure. The firewall is for protecting the network from unwanted and unauthorized user by blocking network traffic with certain criteria. The monitoring clients are used to analyze the performance and health of the server and report to the admin if the servers are not functioning properly. The SSL certificate is for encrypting the traffic between the web servers and the external network to prevent man-in-the-middle attacks (MITM) and network sniffers from sniffing the traffic which could expose valuable information. The SSL certificates ensure privacy, integrity, and identification.

    What are firewalls for?
	The firewall is for protecting the network from unwanted and unauthorized user by blocking network traffic with certain criteria.

    Why is the traffic served over HTTPS?
	Serving traffic over HTTPS (HyperText Transfer Protocol Secure) is essential for ensuring the security, privacy, and integrity of data exchanged between a user's browser and a web server. HTTPS is an encrypted version of HTTP.

    What monitoring is used for?
	The monitoring clients are used to analyze the performance and health of the server and report to the admin if the servers are not functioning properly.

    How the monitoring tool is collecting data?
	The monitoring tool collects data in the web infrastructure through a combination of agents, probes, APIs, and protocols. It gathers information from various components such as servers, networks, applications, databases, and services to provide insights into the performance, availability, and health of the system.

    Explain what to do if you want to monitor your web server QPS
	I will have to select a monitoring tool like datadog. By setting specific metrics I can be able to use datadog to capture data about incoming requests, responses, and their frequency on my server. I will then use data aggregation and create visualization to display QPS trends, spikes, and patterns.

**Issues with this infrastructure**


    Why terminating SSL at the load balancer level is an issue?
	When SSL termination occurs at the load balancer, the communication between the load balancer and backend servers is unencrypted making the data transering vulnarable to attacks.

    Why having only one MySQL server capable of accepting writes is an issue?
	With only one MySQL server handling write operations, the entire system becomes vulnerable to a single point of failure. If the server goes down or experiences issues, all write operations come to a halt, leading to service downtime and data unavailability. As write traffic increases, the single MySQL server may experience high latency as it struggles to keep up with incoming requests. This can lead to delayed transaction processing and poor application responsiveness. Write-heavy workloads might cause the single MySQL server to become a performance bottleneck. Load distribution and load balancing become impossible without additional servers.

    Why having servers with all the same components (database, web server and application server) might be a problem?
	Maintaining an all same component infrastructure(monolithic application) can be complex and time-consuming. Debugging issues might involve tracing through multiple layers of code, making it harder to identify the root cause of problems. In a monolithic architecture, scaling the application can be challenging. If one component (e.g. the database) requires more resources due to increased load, we might need to scale all components, even if they don't need additional resources. This can lead to inefficiencies in resource allocation.

**Description**
This is a distributed web infrastructure design server with three servers that host a website with the alias www.foobar.com at the ip address 8.8.8.8. Each component of this infrastructure uses the same resource.

**Three server web infrastructure**

**Specifics about this web infrastructure**
	
    For every additional element, why you are adding it
	The additional elements are HAPROXY Load balancer and one more server. The load balancer runs an algorithm that detects network traffic and directs it to a specific server. The new server can now ease the load for the old server.

    What distribution algorithm your load balancer is configured with and how it works?
	The HAPROXY load balancer is configured with Round Robin distribution algorithm. This algorithm works by directing each server request to the next available server in a circular order.

    Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
	Our load-balancer is enabling active-passive setup. Since we have only one load balancer, we manage the traffic with that load balancer only. The active-active load balancing setup enables multiple load balancers running simultaneously to manage traffic to multiple servers.

    How a database Primary-Replica (Master-Slave) cluster works?
	The Primary-Replica (Master-Slave) database cluster works by assigning one Primary(Master) node and one Replica(Slave) node to write and read and read data from the database respectively. Data sycronization occures between the primary and replica nodes whenever the primary node runs a write process.

    What is the difference between the Primary node and the Replica node in regard to the application?
	The primary node, also known as the master node, is the central and authoritative source of data in the database cluster. It handles write operations and is responsible for maintaining data consistency and integrity. The replica node, also known as a slave node or secondary node, is a read-only copy of the data from the primary node. It's used to offload read traffic from the primary node and improve read scalability.

**Issues with this web infrastructure**

	This infrastructure has many SPOF(Single point of failure). If the mysql databse fails or is being maintained, the client has no option of updating or receiving information from the databse.
	The infrastructure is vulnarable to attacks becuase it is not secured with SSL certificate and has no firewalls.
	We can not manage the servers properly as we have no monitoring system.

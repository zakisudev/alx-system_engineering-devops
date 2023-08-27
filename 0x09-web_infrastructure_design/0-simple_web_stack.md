**Description**
This is a single server of one server web infrastructure design that host a website with the alias www.foobar.com at the ip address 8.8.8.8. Each component of this infrastructure uses the same resource.

**One server web infrasctructure**

**Specifics about this web infrastructure**

    What is a server?
        A server is a hardware or software that manages access to a cetralized service or resource on a network.

    What is the role of the domain name?
        The domain name is human readable address for a specific website. In our case foobar.com is the domain name configured with www for the ip address 8.8.8.8

    What type of DNS record www is in www.foobar.com?
	The "www" is a CNAME record "Canonical Name" that is technically called subdomain, and its primary use is to differentiate web services from other services that might be associated with the same domain, such as email servers, FTP servers, and more.

    What is the role of the web server?
	It plays a crucial role in serving content, processing requests, and facilitating communication between clients and the website or application backend.

    What is the role of the application server?
	The application server is the server that hosts applications or software that delivers contents or application through a communication protocol.

    What is the role of the database?
	The role of the database is to provide data management system for the client.

    What is the server using to communicate with the computer of the user requesting the website?
	The server is using HyperText Transfer Protocol (HTTP) through the internet network.

**Issues with the single server web infrastructure**
	The single server web infrastructure has many single point of failure(SPOF). If we look at the databse, if the database is down or in maintenance, the whole webserver fails.
	The webserver is not accessable when there is a maintenance. Since the server is only one, the server will be down when maintenance is in progress.
	This webserver can not be scaled since it has only one server. There is also no load balancing available.

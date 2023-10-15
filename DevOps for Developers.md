# https://www.educative.io/path/devops-for-developers

# Modules
1. Networking Fundamentals
2. Git and Github
3. Docker for Developers
4. Docker compose for Developers
5. A practical guide to Kubernetes
6. Kubernetes Monitoring, Logging and Auto Scaling
7. Jenkins X with Kubernetes
8. Kubernetes Chaos Engineering
9. Terraform: From Beginner to Advanced with example in AWS
10. Ansible

# 1. Networking Fundamentals
1. Before we Begin
    1. What is the internet. 
        A network of networks.
    2. Layered architectures & protocol stacks.
        seperate layers of abstraction.
    3. Encapculation and decapsulation.
        Encapsulation is the process of adding headers to the data. Decapsulation is the process of removing headers from the data.
    4. The OSI Model.
        1. Application Layer
            1. These applications or protocols are always implemented in software.
            2. End user interacts with an application layer.
            3. Examples: HTTP, FTP, SMTP, DNS, DHCP, SSH, Telnet, etc.
            4. The application layer is where an outgoing message starts it journey so it provides data for the layer below.
        2. Presentation Layer
            1. Presents data in a way that can be easily understood and displayed by the application layer.
            2. Examples: Encryption, Compression, ASCII, EBCDIC, etc.
        3. Session Layer
            1. The session layer's responsiblility is to take the services of the transport layer and build a service on top of it that manages user sessions.
            2. A session is an exchange of information between local applications and remote services on other end systems.
            3. for example, one session spans a customer's interaction with ecommerce site whereby they search, browse and select products, then make the payment and logout.
            4. abstracts: the session layer assumes that connections establishment and packet transportation is handled by transport layer.
        4. Transport Layer
            1. The transport layer also has protocols that are implemented in software.
            2. since the application, presentation and session layers may be handling off large chunks of data, the transport layer segments it into smaller chunks. they are called datagrams or segments depending on the protocol.
            3. the transport layer also provides flow control and error checking. e.g checksum. when additional information is added to the start of the segment its is called header. when appended to the end of the segment its called trailer.
        5. Network Layer
            1. The network layer is responsible for the delivery of individual packets from the source host to the destination host.
            2. Routing protocols are applications that run on the network layer and exchange information with others to determine the best path for the packet to take.
        6. Data Link Layer
            1. Allows directly connected hosts to communicate with each other. 
            2. encapsulates packets for transmission across a single link.
            3. Multiplexing and demultiplexing.
        7. Physical Layer
            1. consists largely hardware.
            2. responsible for the transmission and reception of the unstructured raw bit stream over a physical medium.
2. Internet and the OSI Model
3. The application Layer
4. The Transport Layer
5. An introductory to socket programming with Python
6. The Network Layer
7. The Data Link Layer
8. Conclusion
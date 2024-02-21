The developement of http/3 was based on QUIC, which is Quick **UDP** Internet connections protocol, which was design to counter the limitation and drwaback of TCP. HTTP/3 was formally standardized by the IEFT in August 2021.

# Drawbacks of HTTP/2
HTTP/2 relied on TCP on the transport layer, TCP has its own cetain limitations in high latency areas.
- Head-of-Line Blocking,  if a packet is lost or delayed, it can cause head-of-line blocking, where subsequent packets must wait for retransmission or delivery of the lost packet, delaying the overall processing.
- The Initial setup of TCP connection incures latency, in busy networks
- Long-Lived connections, maintaining these can impose overhead.
- TCP used technics like slow start fpoor congestion control, which was not optimized for the modern network.

# Improvements

- The use of QUIC instead of the TCP
    - QUIC provided a much lower Latency for HTTP connections.
    - QUIC —— Quick UDP Internet Connections instead of TCP
    - UDP ——— means it provides features like connection multiplexing , encryption and congestion control.
    - HTTP/3’s QUIC-based approach reduces connection establishment latency by combining the handshake and encryption setup into a single step. This is especially beneficial for mobile devices and high-latency networks.
    - HTTP/3’s QUIC includes built-in error correction mechanisms, making it more resilient to packet loss and network disruptions.

## In Conclution
The aim for developing HTTP/3 was to overcome the http/2 limitations and imporve from them, this included solving issues like Head-of-line blocking, high latency, slow congestion Control and Handshake Overhead. HTTP/3 was developed based on QUIC protocol whoch operates over UDP instead of http/2's TCP. QUIC offers features like better congestion control, connection multiplexing(UDP).
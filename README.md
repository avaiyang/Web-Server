Web Server
=======
This is a simple socket programming for TCP connections in Python. The web server will accept and parse one HTTP request at a time, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. In case the requested file is not present in the server, then the server will send an HTTP “404 Not Found” message back to the client. 

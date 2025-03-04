#!/usr/bin/env ruby

require 'socket'
include Socket::Constants


def test_socket
  s = Socket.new( Socket::AF_INET6, Socket::SOCK_STREAM, 0 )

  sockaddr = Socket.pack_sockaddr_in(80,'www.google.com')

  s.connect(sockaddr)

  s.write("GET / HTTP/1.0\r\n\r\n")

  results = s.read
  p results
end

def main
  test_socket
  
end

main

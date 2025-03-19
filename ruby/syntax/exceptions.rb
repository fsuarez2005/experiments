#!/usr/bin/env ruby

# Exceptions

begin
  raise(StandardError)
rescue => e
  puts "Caught exception: #{$!}"
  
end
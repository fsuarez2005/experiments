#!/usr/bin/env ruby


class Thing
  def ===(other)
    puts "Case Equality"
    
    return false
  end
  
  
end


a = Thing.new
b = Thing.new

c = a === b
puts c

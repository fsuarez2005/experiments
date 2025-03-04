#!/usr/bin/env ruby


# Singleton class test

class MySingle
  class << self
    def initialize
      @value = 0
    
    end
    
    
    def value
      return @value
    
    end
    
    def value=(n)
      @value = n
    end
  end
end



s1 = MySingle.new
pp s1
p "s1.value = #{s1.value}"


s2 = MySingle.new
pp s2

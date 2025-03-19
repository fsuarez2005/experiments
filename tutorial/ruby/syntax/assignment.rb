#!/usr/bin/env ruby

# =========================================
# local variable

var1 = 10
var2 = "hello"
var1 = "world"

puts "var1 is #{var1}"

# =========================================
# instance variable

class Banana
  def initialize(size)
    @size = size
  end
  
  def size
    @size
  end
end


b1 = Banana.new(10)

puts "Banana size is #{b1.size}"


# =========================================
# class variable


class Apple
  @@total = 0
  
  def self.get_total
    @@total
  end
  
  
  
  def initialize
    @@total += 1
  end
  
end


a1 = Apple.new
a2 = Apple.new

puts "Total apples is #{Apple.get_total}"

# =========================================
# global
# starts with $
$global_var1 = "hello"

# assignment method
class Fruit
  def color=(value)
    puts "Fruit color set to #{value}."
    @fruitcolor = value
  end

  def color
    puts "Getting fruit color."
    @fruitcolor
  end

end


fruit1 = Fruit.new
fruit1.color = "Red"
puts "Current fruit color = #{fruit1.color}"

# 
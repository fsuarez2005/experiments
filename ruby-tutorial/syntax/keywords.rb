#!/usr/bin/env ruby

def sectop(name="")
  
  puts ".-------------------------------------------,"
  puts "| SECTION: #{name}"
  
end
def secbot(name="")
  puts "`-------------------------------------------'"
end
# The following keywords are used by Ruby.
# 
# __ENCODING__: The script encoding of the current file. See Encoding.


sectop("__ENCODING__")

def varencoding
  puts "__ENCODING__ = #{__ENCODING__}"
end
varencoding
secbot("__ENCODING__")


# 
# __LINE__: The line number of this keyword in the current file.
sectop("__LINE__")
def varline
  puts "__LINE__ = #{__LINE__}"
end 
varline
secbot("__LINE__")
# 
# __FILE__: The path to the current file.

sectop("__FILE__")

def varfile
  puts "__FILE__ = #{__FILE__}"
end
varfile

secbot("__FILE__")

# 
# BEGIN: Runs before any other code in the current file. See miscellaneous syntax
# 
sectop("BEGIN")
BEGIN {
  puts "BEGIN"
  puts "This is happening at the beginning."
  
}
secbot("BEGIN")

# END: Runs after any other code in the current file. See miscellaneous syntax
# 
sectop("END")
END {
  puts "END"
  puts "This is happening at the end."
}
secbot("END")


# alias: Creates an alias between two methods (and other things). See modules and classes syntax
# 
sectop("alias")
class TestClass
  def sayhello
    puts "Hello"
  end
end

class TestClass
  alias sayhi sayhello
end

tc = TestClass.new

tc.sayhi
secbot("alias")

# and: Short-circuit Boolean and with lower precedence than &&
# 
# XXX


sectop("and")



$andvar = 0

def change_andvar
  $andvar = 1
  return true
end

puts "Before: #{$andvar}"

false and change_andvar

puts "After: #{$andvar}"





secbot("and")

# begin: Starts an exception handling block. See exceptions syntax
# 



# break: Leaves a block early. See control expressions syntax

sectop("break")
$break_n = 0
while true
  puts "$break_n = #{$break_n}"
  
  if ($break_n > 10)
    break
  
  end

  $break_n += 1
end
secbot("break")


# 
# case: Starts a case expression. See control expressions syntax

# case + when
sectop("case + when")

$case_w1 = 0


case
when $case_w1 == 1
  puts "$case_w1 == 1"
else
  puts "$case_w1 is something else"
end
secbot("case + when")



# case + in

sectop("case + in")

# used for pattern matching
# https://ruby-doc.org/3.4.1/syntax/pattern_matching_rdoc.html





secbot("case + in")

# 
# class: Creates or opens a class. See modules and classes syntax
# 

class Fruit
  # class variable
  @@total_count = 0
  
  def initialize
    @@total_count += 1
  end
  
  def self.total_count
    return @@total_count
  end
  
  def self.total_count=(n)
    @@total_count = n
  end
end

puts "There are #{Fruit.total_count}."
apple = Fruit.new
puts "There are #{Fruit.total_count}."



# def: Defines a method. See methods syntax
# 

def anothermethod
  puts "This is another method"
end

# defined?: Returns a string describing its argument. See defined?

if (defined? anothermethod) 
  puts "anothermethod has been defined"
end


# 
# do: Starts a block.
# Creates a Proc that is passed to a method
def callblock(&block)
  block.call
end


callblock do 
  puts "hello block"
end


# 
# else: The unhandled condition in case, if and unless expressions. See control expressions
# 

if (false)
  puts "Free money"
else
  puts "No money"
end

# elsif: An alternate condition for an if expression. See control expressions
# 
# end: The end of a syntax block. Used by classes, modules, methods, exception handling and control expressions.
# 
# ensure: Starts a section of code that is always run when an exception is raised. See exception handling
# 
# false: Boolean false. See literals
# 
# for: A loop that is similar to using the each method. See control expressions
# 
# if: Used for if and modifier if statements. See control expressions
# 
# in: Used to separate the iterable object and iterator variable in a for loop. See control expressions
# 
# module: Creates or opens a module. See modules and classes syntax

module MyModule
end


# 
# next: Skips the rest of the block. See control expressions
# 
# nil: A false value usually indicating “no value” or “unknown”. See literals
# 
# not: Inverts the following boolean expression. Has a lower precedence than !
# 
# or: Boolean or with lower precedence than ||
# 
# redo: Restarts execution in the current block. See control expressions
# 
# rescue: Starts an exception section of code in a begin block. See exception handling
# 
# retry: Retries an exception block. See exception handling
# 
# return: Exits a method. See methods. If met in top-level scope, immediately stops interpretation of the current file.
# 
# self: The object the current method is attached to. See methods
# 
# super: Calls the current method in a superclass. See methods
# 
# then: Indicates the end of conditional blocks in control structures. See control expressions
# 
# true: Boolean true. See literals
# 
# undef: Prevents a class or module from responding to a method call. See modules and classes
# 
# unless: Used for unless and modifier unless statements. See control expressions
# 
# until: Creates a loop that executes until the condition is true. See control expressions
# 
# when: A condition in a case expression. See control expressions
# 
# while: Creates a loop that executes while the condition is true. See control expressions
# 
# yield: Starts execution of the block sent to the current method. See methods

def yielding_method
  yield
end


yielding_method do 
  puts "Hello"
end



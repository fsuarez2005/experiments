#!/usr/bin/env ruby

# ##################################
# ##################################
# ##################################

# literals

# boolean
# nil and false evaluate to false

if not nil then
  puts "Nil is equivalent to false."
end

if not false then
  puts "false is false"
end

# ==================================

# decimal - 0d
if 0d100 == 100 then
  puts "0d100 equals 100"
end


# hexadecimal - 0x
if 0xff == 255 then
  puts "0xff equals 255"
end

# octal - 0o
if 0o77 == 63 then
  puts "0o77 equals 63"
end

# binary - 0b
if 0b1000 == 8 then
  puts "0b1000 equals 8"
end

# ==================================

# float
if 314E-2 == 3.14 then
  puts "314E-2 equals 3.14"
end

# ==================================

# imaginary
# 2+3i

# ==================================

# Strings
# %q and %Q can be used instead of ' and "

"One plus one is #{1+1}"

'One plus one is #{1+1}'

# HEREDOC

heredoc_string = <<HEREDOC
Hello there

Everybody.
HEREDOC

puts heredoc_string

# Symbol
# A Symbol represents a name inside the ruby interpreter. 

:my_symbol

:"string used as symbol"


# Array

array_1 = [1,2,3,4]

puts "array_1 = #{array_1}"

# Hash
# Key and value may be any object.

hash_1 = { "a" => 1 }
hash_2 = { a: 1 }
puts "hash_2 = #{hash_2}"



# Ranges

# inclusive
(1..10) 

#exclusive
(1...10)

# Regexp

regexp_1 = /regexp string/


# Lambda (Proc)

-> { 1 + 2 }
->(x) { x + 1 }





# ##################################


#!/usr/bin/env ruby

# checks domains to see if they are available

charlist = ('a'..'z').to_a + (0..9).to_a.map {|x| x.to_s}


def permutations_with_repetition(characters, length)
  return [] if length <= 0
  characters.repeated_permutation(length)
end

c = permutations_with_repetition(charlist,4)

domains = c.map {|x| (x.join)+".com"}




p domains

puts "Length = #{domains.length}"
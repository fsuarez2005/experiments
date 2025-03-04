#!/usr/bin/env ruby

#
# Number Guessing Game
#

$DEBUG = true

def dputs(obj)
  if $DEBUG
    puts "DEBUG: #{obj}"
  end
end



puts "Number Guessing Game"

# set configuration options
$minimum_number = 1
$maximum_number = 100
$maximum_tries = 10

# generate random integer
# using a integer range from minimum to maximum
$secret_number = rand($minimum_number..$maximum_number)
#dputs("Secret number = #{$secret_number}")

def guessing_game(
  minimum_number,
  maximum_number,
  maximum_tries,
  secret_number)
  winner = false

  for current_try in (1..maximum_tries)
    puts "Current Try: #{current_try}"
    
    # get user input
    puts "Enter a guess: "
    user_input = gets

    # convert input to integer
    user_input_integer = user_input.to_i

    # compare input to secret integer
    # if input equals secret integer, declare winner
    if user_input_integer == secret_number then
      puts "You found the secret number."
      return
    else
      puts "Incorrect guess."
    end
    # else repeat loop
  
  end
  
  if (not winner) then
    puts "No more tries."
  end
  
  
end


def main
  guessing_game(
    $minimum_number,
    $maximum_number,
    $maximum_tries,
    $secret_number)
end


main



#!/usr/bin/env ruby

# ANSI test

require "io/console"

$ANSI_COLOR_RANGE = (0..255)


def place_char(con = IO.console,char,color)

  # change color
  con.print "\e[48;5;#{color}m"

  con.print char
  
  # reset
  con.print "\e[0m"

end

def place_random_char(con = IO.console)
  
  (lines,columns) = con.winsize
  
  line = rand(0..lines)
  column = rand(0..columns)
  
  con.goto(line,column)
  
  
  place_char(" ",rand($ANSI_COLOR_RANGE))
  
end



def main
  con = IO.console
  con.erase_screen(2)
  loop {
    place_random_char(con)
    sleep 0.001
  }
  
end

main
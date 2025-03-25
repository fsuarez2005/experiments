#!/usr/bin/env ruby


# ANSI library


$ESCAPE_CODE = "\e"


#Control Sequence Introducer


def cursor_up()
  "\e[5A"
  
end


puts cursor_up()




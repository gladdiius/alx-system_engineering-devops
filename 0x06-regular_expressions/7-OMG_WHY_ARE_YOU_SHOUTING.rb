#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  list = ARGV[0].split()
  puts list
  united = list.join(',')
  puts united
  disunited = united.split('')
  puts "x"
  puts disunited
  
  for cap in disunited 
    if cap.match(/[A-Z]/)
     print "#{cap}"
    end
    next
  end
end
regexp

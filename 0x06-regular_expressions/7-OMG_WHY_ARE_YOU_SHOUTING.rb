#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  list = ARGV[0].split()
  united = list.join(',')
  disunited = united.split('')

  for cap in disunited 
    if cap.match(/[A-Z]/)
     print "#{cap}"
    end
  end
end
regexp

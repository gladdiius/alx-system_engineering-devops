#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  list = ARGV[0].split()
  for check in list do
    if check.match(/School/)
        print "School"
    end
  end
end
regexp

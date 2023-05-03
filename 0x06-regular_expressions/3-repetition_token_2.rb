#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  if ARGV[0].match(/hb*t{1,4}n/)
    puts ARGV[0]
  end
end
regexp

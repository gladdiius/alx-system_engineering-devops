#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  if ARGV[0].match(/hb{2,5}tn/)
    puts ARGV[0]
  end
end
regexp

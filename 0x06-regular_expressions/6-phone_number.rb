#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  if ARGV[0].match(/\S\d{10}/)
    print "#{ARGV[0]}"
  end
end
regexp

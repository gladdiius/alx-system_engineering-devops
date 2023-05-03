#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  if ARGV[0].match(/\d{10}/)
    puts ARGV[0]
  end
end
regexp

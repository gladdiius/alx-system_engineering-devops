#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  if ARGV[0].match(/hbt{2,5}n/)
    return true
  end
end
regexp

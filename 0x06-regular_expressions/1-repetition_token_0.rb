#!/usr/bin/env ruby
def regexp
  if ARGV[0] == nil
         return
  end
  puts ARGV[0].scan(/hbt{2,5}n/)
end

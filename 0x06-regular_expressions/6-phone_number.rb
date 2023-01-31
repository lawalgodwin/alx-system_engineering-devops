#!/usr/bin/env ruby

# A regex that matches only 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join

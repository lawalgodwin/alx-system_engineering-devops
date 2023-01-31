#!/usr/bin/env ruby

# A regex that matches only capital letter

puts ARGV[0].scan(/[A-Z]+/).join

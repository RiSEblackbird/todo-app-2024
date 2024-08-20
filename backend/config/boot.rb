ENV["BUNDLE_GEMFILE"] ||= File.expand_path("../Gemfile", __dir__)

require "bundler/setup" # Set up gems listed in the Gemfile.
require "bootsnap/setup" # Speed up boot time by caching expensive operations.

# Add these lines for debugging
require 'mysql2'
puts "Attempting to connect to MySQL..."
begin
  client = Mysql2::Client.new(host: ENV['DB_HOST'] || 'db', username: 'root', password: 'rootpassword')
  puts "Successfully connected to MySQL"
rescue => e
  puts "Failed to connect to MySQL: #{e.message}"
end
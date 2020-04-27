this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'thread'
require_relative 'lib/match_services_pb'
require_relative 'lib/match_pb'

def subscribe_to_tournament(stub, tournament, frequency)
    responses = stub.subscribe_to_tournament(SubscribeRequest.new(tournament: tournament, frequency: frequency))
    responses.each do |resp|
        if resp.first_team.is_ct
            first_team_site = "CT"
            second_team_site = "TT"
        else
            first_team_site = "TT"
            second_team_site = "CT"
        end
        print_results(resp, tournament, first_team_site, second_team_site)
    end
end

def print_results(resp, tournament, first_team_site, second_team_site)
    puts ""
    puts "Situation at: #{resp.datetime}"
    puts "Tournament: #{tournament}"
    puts "#{resp.first_team.name} (#{first_team_site}) VS #{resp.second_team.name} (#{second_team_site})"
    puts "#{resp.score}"
    puts "Last win condition: #{resp.win_condition}"

    print "#{resp.first_team.name} alive members: "
    resp.first_team.alive_members.each do |member|
        print "#{member} "
    end

    puts ""
    print "#{resp.second_team.name} alive members: "
    resp.second_team.alive_members.each do |member|
        print "#{member} "
    end
    puts "\n"
end

def connect_to_server(tournament, frequency)
    puts "Subscribing to #{tournament} with frequency #{frequency}"
    stub = ScoreNotifications::Stub.new('localhost:50051', :this_channel_is_insecure)
    subscribe_to_tournament(stub, tournament, frequency)
end

def shut_down
    puts "\nShutting down gracefully..."
    sleep 1
end

Signal.trap("INT") { 
    shut_down 
    exit
}

def main
    tournament = ARGV.size > 0 ? ARGV[0] : 'DreamHack'
    frequency = ARGV.size > 1 ? ARGV[1].to_i : 5
    begin
        connect_to_server(tournament, frequency)
    rescue GRPC::BadStatus => err
        if err.code == GRPC::Core::StatusCodes::INVALID_ARGUMENT
            puts "Wrong tournament, closing"
            exit(false)
        else
            puts "\nConnection failed, trying again..."
            retry
        end
    end
end

main
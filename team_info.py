#Begin Imports
import tbapy
from pytba import api as tba
#End Imports

#Begin API Key Verification
tba = tbapy.TBA('INSERT TBA API KEY HERE')
#End API Key Verification

team_number_provided = input("Input Team Number: ")
team_number = team_number_provided
team_number_appended = str('frc') + str(team_number_provided)
team = tba.team(team_number_appended)
events = tba.team_events(team_number_appended, 2019)

if team_number_appended == str("frc") + (team_number_provided): # Check whether string for Team Number is formatted properly
    print(("Team ") + team_number + "'s", "Info:") # Print Title
    print('Team ' + team_number + ' is from %s in %s, %s.' % (team.city, team.state_prov, team.country)) # Print Team Location
    print('In 2019, Team ' + team_number + ' participated at %d events: %s.' % (len(events), ', '.join(event.event_code for event in events))) # Print Team Events

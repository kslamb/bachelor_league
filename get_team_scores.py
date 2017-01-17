from bachelor_league import FantasyLeague, FantasyTeam

caseyTeam = FantasyTeam(manager="Casey",
						team_name="The Mesa Verde",
						contestants=['Vanessa, Special Education Teacher','Astrid, Plastic Surgery Office Manager','Jaimi, Chef'])
janakiTeam = FantasyTeam(manager="Janaki",
						 team_name="Here to make friends",
						 contestants=['Danielle M., Neonatal NUrse','Taylor, Mental Health Counselor','Whitney, Pilates Instructor'])
brendanTeam = FantasyTeam(manager="Brendan",
						  team_name="On Mondays I work late",
						  contestants=['Corrine, Business Owner','Raven, Fashion Boutique Owner','Lacey, Digital Marketing Manager'])
suzyTeam = FantasyTeam(manager="Suzy",
					   team_name="Where's my frog prince",
					   contestants=['Christen, Wedding Videographer','Elizabeth ("Liz"), Doula','Sarah, Grade School Teacher'])
keelyTeam = FantasyTeam(manager="Keely",
					   	team_name="Keely",
					   	contestants=['Hailey, Photographer','Danielle L., Small Business Owner','Kristina, Dental Hygienist'])
jordynTeam = FantasyTeam(manager="Jordyn", 
						 team_name="Ashley S for Prez", 
						 contestants=['Rachel, Attorney','Alexis, Aspiring Dolphin Trainer','Josephine, Unemployed Nurse'])
karenTeam = FantasyTeam(manager="Karen",
						team_name="Team Sex Panther",
						contestants=['Dominique, Restaurant Server','Jasmine G., Pro Basketball Dancer','Elizabeth, Marketing Manager'])

fl = FantasyLeague(name="Breadan, will you accept this rose?", teams=[caseyTeam, janakiTeam, brendanTeam, suzyTeam, jordynTeam, karenTeam])
fl.printTeamScores()
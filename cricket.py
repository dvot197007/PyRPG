# Cricket simulation

########################################################################
# Data

bradman = {'name' : 'bradman',
           'batting' : 10,
           'bowling' : 0
          }

ponting = {'name' : 'ponting',
           'batting' : 9,
           'bowling' : 0
          }

lillee = {'name' : 'lillee',
           'bowling' : 9
          }

holding = {'name' : 'holding',
           'bowling' : 9
          }

marsh = {'name' : 'marsh',
           'keeping' : 9,
           'bowling' : 0
          }

team_1 = {'name' : 'invincibles',
             'lineup': [bradman, ponting, marsh, lillee, holding]
            }

sachin = {'name' : 'sachin',
           'batting' : 10,
           'bowling' : 0
          }

hadlee = {'name' : 'hadlee',
           'bowling' : 9
          }

richards = {'name' : 'richards',
           'batting' : 9,
           'bowling' : 0
          }

garner = {'name' : 'garner',
           'bowling' : 9
          }

murray = {'name' : 'murray',
           'keeping' : 9,
           'bowling' : 0
          }

team_2 = {'name' : 'rest of world',
             'lineup': [sachin, richards, murray, garner, hadlee]
            }

limited_overs = True
nOvers = 10

waitForKeyPress = 1

delay = 1000 # /1000 seconds for score display
displayScoreCard = True

nInningsPerTeam = 2

teams = {"home" : team_2,
         "away" : team_1
        }
# probability distributions
pOut = 0.1        
outcomes = [(0.95, 'runs'), (0.01, 'leg byes'), (0.01, 'byes'), (0.01, 'no ball'), (0.01, 'wide')]
runs = [(0.3, 0), (0.3, 1), (0.1, 2), (0.05, 3), (0.2, 4), (0.05, 6)]
howOut = [(0.2, 'bowled'), (0.6, 'caught'), (0.1, 'LBW'), (0.05, 'run out'), (0.05, 'stumped')]

##################################################################################################
# Main program

import random

# Coin toss
order = ['home', 'away']
toss = random.randint(0,1)
if toss == 1:
    order = ['away', 'home']

# Set up order of play
orderOfPlay = []
for i in range(nInningsPerTeam):
    orderOfPlay.append(order[0])
    orderOfPlay.append(order[1])

scorecards = []
newInnings = True # need to set up the scorecard
innings  = 0
ball = 0
over = 0
while innings <= 2 * nInningsPerTeam:
    print("Innings ", innings + 1, "\n")
    if waitForKeyPress == 1:
        k = input("Press any key for next delivery - Hit 'c' to simulate to the end"):
        if k == "c":
            waitForKeyPress = 0
            
    if newInnings:
        # Load Batting team
        batting_team = orderOfPlay[innings]
        teamData = teams[batting_team]
        teamName = teamData['name']
        lineup = teamData['lineup']
        if len(lineup) < 2:
            print('There must be at least two players in each team')
            break
        playerScores = []
        for player in lineup:
            row = {'name' : player['name'],
                   'runs' : 0,
                   'how out' : 'yet to bat',
                   'bowler' : '',
                   'total' : 0
                   }
            playerScores.append(row)
        # Load Bowlers
        if batting_team == "home":
            bowling_team = "away"
        else:
            bowling_team = "home"
        lineup = teamData['lineup']
        bowlers = []
        for player in lineup:
            if player['bowling'] > 0:
                row = {'name' : player['name'],
                       'overs' : [0, 0],
                       'runs' : 0,
                       'leg byes' : 0,
                       'no balls' : 0,
                       'wides' : 0,
                       'wickets' : 0
                       }
                bowlers.append(row)
        # Ball by ball as a list of lists
        BallByBall = []
        # Assemble scorecard
        card = {'Team name' : teamName,
                'Innings' : innings,
                'Player scores' : playerScores,
                'striker' : 0,
                'nonStriker' : 1,
                'currentBowler' : 0,
                'Extras' : 0,
                'Total' : 0,
                'Wickets' : 0,
                'Overs' : 0,
                'Bowling' : bowlers,
                'BallByBall' : BallByBall
                }
        scorecards.append(card)
        newInnings = False
        
    # Start simulation
    while card['Wickets'] < 10:
        if card['Overs'] >= nOvers && limited_overs == True:
            break
        # simulate an over
        over = []
        card['currentBowler'] = chooseBowler(nowBowler = card['currentBowler'], bowlingList = card['Bowling'])
        while legalBalls < 6:
            striker = card['striker']
            nonStriker = card['nonStriker']
            ball = simulateDelivery(batsman = striker, bowler = card['currentBowler'])
            
            
            legalBalls += 1
            if ball == "no ball" || ball == "wide":
                legalBalls -= 1
            
             
        
        BallByBall.append(over)
        
        if displayScoreCard == True:
            wait(delay)
            displayCard()
    
    
    
    
    
    
    newInnings = True # Start new innings 
    
# Add up all innings to determine the result
        
        


def displayCard():
    pass   
    
def simulateDelivery():
    pass
    
def chooseBowler():
    pass
    
















































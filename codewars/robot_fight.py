"""
Rules
>A robot with the most speed attacks first. If they are tied,
 the first robot passed in attacks first.
Robots alternate turns attacking. Tactics are used in order.
>A fight is over when a robot has 0 or less health or
 both robots have run out of tactics.
>A robot who has no tactics left does no more damage,
 but the other robot may use the rest of his tactics.
>If both robots run out of tactics, whoever has the most health wins.
 Return the message "{Name} has won the fight."
>If both robots run out of tactics and are tied for health, the fight is a draw.
 Return "The fight was a draw."
"""

robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}

def chooseWinner():
    if robot_1['health'] > robot_2['health']:
        return "{} has won the fight".format(robot_1['name'])
    elif robot_2['health'] < robot_1['health']:
        return "{} has won the fight".format(robot_2['name'])
    else:
        return "The fight was a draw."

def attack(attacker, defender, turn):
    if turn >= len(attacker['tactics']):
        return
    attack_name = attacker['tactics'][turn]
    defender['health'] -= tactics[attack_name]

def isFightOver(turn):
    return robot_1['health'] <= 0 or robot_2['health'] <= 0 or (turn >= len(robot_1['tactics']) and turn >= len(robot_2['tactics']))

def fight(robot_1, robot_2):
    turn = 0
    firstPlayer = robot_1 if robot_1['speed'] >= robot_2['speed'] else robot_2
    secondPlayer = robot_2 if robot_1['speed'] >= robot_2['speed'] else robot_1
    while not isFightOver(turn):
        attack(firstPlayer, secondPlayer, turn)
        if isFightOver(turn):
            break
        attack(secondPlayer, firstPlayer, turn)
        turn += 1
    return chooseWinner()

print(fight(robot_1, robot_2))

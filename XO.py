# A function to print the game table everytime
def showGame(game_table):
    for row in game_table:
        for item in row:
            print(item,end=" ")
        print()

# A function to play the rule by entering the position of the number
def playRule(rule,game_table):
    while True:
        pos=input("Enter position to play at: ")
        for row in game_table:
            for i, item in enumerate(row):
                if item==pos:
                    row[i]=rule
                    return
        
        print("Invalid move! Try again..")

# A function to swap bettwen rules
def changeRule(rule):
    if rule=="X":
       return "O"
    elif rule=="O":
        return "X"

# A function to check win at every round
def checkWin(rule,game_table):
    # Row Win
    for row in game_table:
        if row==[rule,rule,rule]:
            print(f"{rule} won the game")
            return True
    # Colomn Win
    for col in range(3):
        if game_table[0][col]==game_table[1][col]==game_table[2][col]==rule:
            print(f"{rule} won the game")
            return True
    # Main Diagonal Win
    if game_table[0][0]==game_table[1][1]==game_table[2][2]==rule:
        print(f"{rule} won the game")
        return True
    # Minor Diagonal Win
    if game_table[0][2]==game_table[1][1]==game_table[2][0]==rule:
        print(f"{rule} won the game")
        return True
    
    return False


# main body

# intial state of winning
state=False
# game starts with X rule
rule="X"
# a counter to count the game moves then if it reaches 9, it's a tie
moves=0
# intial game table with nums
game_table=[["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]]
print("Game Starts")
while True:
    showGame(game_table)
    print(f"\nTurn for {rule} to play")
    playRule(rule,game_table)
    
    moves+=1
    state=checkWin(rule,game_table)

    # win condition
    if state==True:
        showGame(game_table)
        break
    # tie condition
    elif moves==9:
        showGame(game_table)
        print("it's a Tie!")
        break
    # changing rule and play
    else:
        rule=changeRule(rule)
print("Game Ends!")
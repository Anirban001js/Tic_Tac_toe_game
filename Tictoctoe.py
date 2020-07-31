from IPython.display import clear_output
row4 = [" "," "," "," "," "," "," "," "," "," "]
def display(row4):
    print(row4[1], "|", row4[2], "|", row4[3])
    print("-", "-", "-","-","-")
    print(row4[4], "|", row4[5], "|", row4[6])
    print("-", "-", "-","-","-")
    print(row4[7], "|", row4[8], "|", row4[9])


def marker_choice():
    player1=" "
    while player1 not in ["X", "O"]:
        player1 = input("Player 1 please enter your marker in [ X, O ]= ")
        if player1 not in ["X", "O"]:
            print ("Please choose a correct marker in [ X , O ]")
        if player1 in ["X", "O"]:
            if player1 == "X":
                player2 = "O"
            else:
                player2 = "X"
    return ((player1, player2))

def take_input(board, marker):
    p=False
    while p==False:
        val=input("please enter a possition between (1,9) :" )
        if val.isdigit():
            val=int(val)
            p=True
        else:
            print("Please enter a correct value ")
        if p==True:
            if board[val]!=" ":
                p=False
                print("Please enter a correct value")
    board[val]=marker
   
def gameon_choice():
    gameon = input("Do you want to play the game  ? enter [Y or N]")
    return gameon == "Y"

    

player=[]
display(row4)
gameon=True
Player1,Player2 = marker_choice()
clear_output()
print(f"Player1's choice is : {Player1}")
print(f"Player2's choice is : {Player2}")
print("Let's Start the game.....")
while gameon==True:
    count=1
    win=False
    marker="l"
    while count<=9 and win==False:
        if count%2==0:
            print("Player 2 It's Your turn...")
            take_input(row4,Player2)
        else:
            print("Player 1 It's Your turn...")
            take_input(row4,Player1)
        clear_output()
        display(row4)
        count=count+1
        if row4[1]==row4[2]==row4[3]=="X" or row4[4]==row4[5]==row4[6]=="X" or row4[7]==row4[8]==row4[9]=="X" or row4[1]==row4[4]==row4[7]=="X" or row4[2]==row4[5]==row4[8]=="X" or row4[3]==row4[6]==row4[9]=="X" or row4[1]==row4[5]==row4[9]=="X" or row4[3]==row4[5]==row4[7]=="X" or row4[1]==row4[2]==row4[3]=="O" or row4[4]==row4[5]==row4[6]=="O" or row4[7]==row4[8]==row4[9]=="O" or row4[1]==row4[4]==row4[7]=="O" or row4[2]==row4[5]==row4[8]=="O" or row4[3]==row4[6]==row4[9]=="O" or row4[1]==row4[5]==row4[9]=="O" or row4[3]==row4[5]==row4[7]=="O":
            if count%2==0:
                print("Player1 wins")
                
            else:
                print("Player2 wins")
            win=True
            if count==10:
                count=count+1
            break
    if count==10:
        print("Its a tie")
    count=1
    row4 = [" "," "," "," "," "," "," "," "," "," "]
    gameon=gameon_choice()
    if gameon==True:
        clear_output()
        display(row4)
    else:
        clear_output()
        print("Thank You! For playing the game....\n I hope you will come back very soon")
        

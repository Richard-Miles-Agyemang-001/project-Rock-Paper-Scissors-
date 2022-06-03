import random

def play ():
    user = input("What is your choice? 'R for Rock, 'P for Paper, 'S for Scissors\n")
    user + user.upper()

    computer = random.choice(['R', 'P', 'S'])
    
    if user == computer:
        return "You and the computer have both chosen {}, It's a tie.",format(computer)

        # R=R, S=S, P=P
        if is_win(user, computer):
            return "you have chosen {} and the computer has chosen{}. You WON!", format(user, computer)

            return "You have {} and the computer has chosen. You LOSE!", format(user, computer)

            def is_win(player, opponent):
                #return true is the player beats the opponent
                #winning condition R>S, S>P, P>R
                
                if (player == 'R' and opponent == 'S') or (player == 'S' and opponent =='P') or (player =='P' and opponent =='R'):
                return True
                return False

                if __name__ == '__main__':
                    print(play())

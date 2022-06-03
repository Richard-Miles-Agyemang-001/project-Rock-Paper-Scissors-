# project-Rock-Paper-Scissors-
import random

def play ():
    Player = input("What is your choice? 'R for Rock, 'P for Paper, 'S for Scissors\n")
    Player + Player.upper()

    CPU = random.choice(['R', 'P', 'S'])
    
    if Player == CPU:
        return "You and the CPU have both chosen {}, It's a tie.",format(CPU)

        # R=R, S=S, P=P
        if is_win(Player, CPU):
            return "you have chosen {} and the CPU has chosen{}. You WON!", format(Player, CPU)

            return "You have {} and the CPU has chosen. You LOSE!", format(Player, CPU)

            def is_win(player, CPU):
                #return true is the player beats the CPU
                #winning condition R>S, S>P, P>R
                if(player == 'R' and CPU == 'S') or (player == 'S' and CPU =='P') or (player =='P' and CPU =='R'):

                return True
                return False

                if __name__ == '__main__':
                    print(play())

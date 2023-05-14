from random import randint
from threading import Thread
def player1():
    dic={1:"Rock",2:"Sheet",3:"Scissors"}
    valeur= input("Please make your choice:\n1-Rock\n2-Sheet\n3-Scissors\n")
    valeur=int(valeur)
    computer_choice=randint(1,3)
    computer_choice=int(computer_choice)
    try:
        if valeur==computer_choice:
            print("None everywhere")
        elif valeur==1 and computer_choice==2:
            print(f"You chose {dic[valeur]}\nI chose Leaf\n{dic[computer_choice]}\nI Won!!!")
        elif valeur==2 and computer_choice==1:
            print(f"You chose {dic[valeur]}\nI chose {dic[computer_choice]}\nYou Won!!!")
        elif valeur==1 and computer_choice==3:
            print(f"You chose {dic[valeur]}\nI chose {dic[computer_choice]}\nYou Won!!!")
        elif valeur==3 and computer_choice==1:
            print(f"You chose {dic[valeur]}\nI chose Leaf\n{dic[computer_choice]}\nI Won!!!")
        elif valeur==2 and computer_choice==3:
            print(f"You chose {dic[valeur]}\nI chose Leaf\n{dic[computer_choice]}\nI Won!!!")
        else:
            print(f"You chose {dic[valeur]}\nI chose {dic[computer_choice]}\nYou Won!!!")
    except KeyError:
        print("Erreur de choix")
thread1=Thread(target=player1)

thread1.start()

thread1.join()
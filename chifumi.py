from random import randint
def play():
    dic={1:"Rock",2:"Sheet",3:"Scissors"}
       try:
        computer_choice=randint(1,3)
        value= input("Please make your choice:\n1-Rock\n2-Sheet\n3-Scissors\n")
        value=int(value)
        if value==computer_choice:
            print("None everywhere")
        elif value==1 and computer_choice==2:
            print(f"You chose {dic[value}\nI chose {dic[computer_choice]}\nI Won!!!")
        elif value==2 and computer_choice==1:
            print(f"You chose {dic[value]}\nI chose {dic[computer_choice]}\nYou Won!!!")
        elif value==1 and computer_choice==3:
            print(f"You chose {dic[value]}\nI chose {dic[computer_choice]}\nYou Won!!!")
        elif value==3 and computer_choice==1:
            print(f"You chose {dic[value]}\nI chose {dic[computer_choice]}\nI Won!!!")
        elif value==2 and computer_choice==3:
            print(f"You chose {dic[value]}\nI chose {dic[computer_choice]}\nI Won!!!")
        else:
            print(f"You chose {dic[value]}\nI chose {dic[computer_choice]}\nYou Won!!!")
    except:
        print("Choice's Error")

#play()                                  

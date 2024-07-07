import random
import sys

times_run = int(input("please enter how many time you want to run "))
options=["rock","paper","scissors"]


while times_run > 0:
    human_input=input("your playing rock paper scissors,and this is squid game so you would die if you lose ")
    human_input = human_input.lower()

    computer_choice=random.choice(options)
#line 14 to 27 - homework
    if len(human_input.split()) != 1:
        print(f"Please enter the correct input you entered \"{human_input}\"")
        # sys.exit(0)              # Stop it here. Dont go any furtther
        continue

    if human_input not in options:
        print(f"Please enter the correct input you entered \"{human_input}\" Enter one of rock, paper or scissors")
        # sys.exit(0)              # Stop it here. Dont go any furtther
        continue


    print(f"Computers choice is {computer_choice}")
    print(f"Humans choice is {human_input}")

    rock="""
        _______
    ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """

    paper ="""
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
        """

    scissors = """
            _______
        ---'   ____)____
                    ______)
                __________)
            (____)
        ---.__(___)
    """

    if computer_choice == "paper" and human_input == "scissors":
        print(f"Human win as scissors {scissors}")
    elif computer_choice == "paper" and human_input == "rock":
        print(f"Computer win as paper {paper}")

    elif computer_choice == "scissors" and human_input == "rock":
        print(f"Human wins as rock {rock}")
    elif computer_choice == "scissors" and human_input == "paper":
        print(f"Computer wins as scissors {scissors}")

    elif computer_choice == "rock" and human_input == "paper":
        print(f"Human wins as paper {paper}")
    elif computer_choice == "rock" and human_input == "scissors":
        print(f"Computer wins as rock {rock}")
    else:
        print("Its a TIE")

    times_run = times_run - 1

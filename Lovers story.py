# runs your Python code
import sys

# script for pauses or delays
import time

# script to clear the terminal screen
import os

# imports only the sleep function from the time module
from time import sleep


def main():
    while True:
        name = input("Enter your name: ")

    # Check for only alphabetic characters (no numbers or punctuation)
        if name.isalpha():
            print("Hello gamer " + name)
            break
        else:
            print("Invalid input! Please enter a name without numbers or punctuation.")

    sleep(5)

    print("\nLeague was created in 2009\nDoes anyone feel old?")
    print(
        "The company who makes League is Riot Games\nLeague is a multiplayer online battle arena."
    )
    print(
        "I have been playing league for six years.\nNow enough about that let me tell you a story."
    )
    sleep(8)
    os.system("cls")
    print("This is a choose your own adventure story.")
    print("This is about two soulmates.\n\nXayah and Rakan")
    print("Your job is to guide their story.\nYou ready?")
    print("Lets go! It will be fun\n\n\n\n")

    sleep(8)
    os.system("cls")


    # //timer to clear screen
    sleep(2)

    # // clears screen
    os.system("cls")
    scene1()

# insert story
def scene1():
    while True:
        sleep(1)
        print("There are moments in life where you need to decide where your passion is")
        print(
            """
            This is a prison break.
            Xayah-Rakan is the worst! I swear he is focusing on his perfect golden feathers. Let's hope he doesn't mess up the plan. 
            Rakan-"Huh? What??"
            Xayah-"The guards. You'll distract the guards away from the western gate. Once that happens I'll throw a feather into the sky"
        """
        )

        print("What do you think Rakan does next?")
        print(
            " 1. Mess up the plan and gets caught\n 2. Distracts the guards and meets up with Xayah\n Type Mess or Distracts"
        )

        while True:
            c1 = input("Enter your choice (1 or 2):")
            if c1.isdigit() and int(c1) in (1, 2):
                choice = int(c1)
                if choice == 1:
                    print(
                        """Xayah-I am watching Rakan from a distance. Alright things are going smooth. Time to move. "NO NO!! PLEASE! RAKAN!!!!!!!!!!!!!!!!!!!!!!"
                        """
                    )
                    layOnGround()
                    return
                elif choice == 2:
                    print(
                        """
                        Rakan-He leaps back and forth between the walls leading the guards away.
                        Xayah-"I knew you could do it <3"
                        Rakan-"I know"
                        Xayah-My god I don't know if I want to slap him, kiss him, or both
                        I shake my head
                        Rakan-He walks over to Xayah "Your soul belongs to me....."
                        Xayah-I touch Rakan face "Lets go"
                        """
                    )
                    return
            else:
                print("Please type a valid choice: 4 or 5")

def layOnGround():
    while True:
        sleep(1)
        print(
            """
            Xayah-I passed out from the trauma of seeing my love being taken away by HUMANS!
            ........ I slowly start to wake up
            What is the first thing Xayah sees when she opens her eyes?
            You continue to lay on the ground with a broken heart\n
            Type your choice: 3
            """
        )
        while True:
            c1 = input("Enter 3: ")
            if c1.isdigit() and int(c1) == 3:
                print(
                    """
                    Xayah-As I continue to lay here. All I can feel is heartbreak. Heartbreak from seeing humans even think of touching him.
                    We are partners!
                    NOOOO we are not just partners.
                    Rakan is my soul mate, my lover, my best friend.
                    My mind begins to race with rage!
                    """
                )
                faceHumansOrRakan()
                return
            else:
                print(
                    """
                    Please choice 3 to continue: 3
                    """
                )

def faceHumansOrRakan():
    while True:
        sleep(1)
        print(
            """
            Xayah- I shoot up from my depression. Dust off my feathers. Get my mind straight and think of how to find Rakan.
            He needs me!
            I dart out of the forest and in front of me is the enemy. HUMANS!
            I stare directly into their soul and without even realizing it. My feathers are entering their bodies.
            More guards are coming from all directions. If I don't find a way out I am going to be surrounded soon.
            Noise from nearby wall-"BOOM"
            Xayah-"Huh"\n
                    
            What is the noise that Xayah heard?\n
            Enter your choice: 4. Rakan or 5. Human
        """
        )
        while True:
            c1 = input("Enter 4. Rakan or 5. Human:")
            if c1.isdigit() and int(c1) in (4, 5):
                choice = int(c1)
                if choice == 4:
                    print(
                        """
                        Xayah- In a fit of rage I kill everyone in sight. Knowing there is nothing left.
                        """
                    )
                    scene2()
                    return            
                elif choice == 5:
                    print(
                        """
                        Xayah-I dream of Rakan. I remember how he tells me to be careful.
                        That was the last time I saw him before we parted ways...........
                        My heart continues to sink
                        """
                    )
                    return            
            else:
                print(
                    """
                    Please type a valid choice: 4 or 5
                    """
                )

            

def scene2():
    sleep(1)
    print(
        """
        Xayah-As I wake up from the horror that my own mind has been reminding me.
        A new day is burning my eyes from all the crying I must have been doing while I was asleep.
        Will I ever see Rakan again? Although it probably has been only moments his absence feels like a life time.
        "Where do I go from here?"
        What does Xayah do now?
        Takes a moment to seek revenge? Or Escape prison like planned without Rakan?
        Type:Revenge or Rakan
    """
    )
    c1 = input()
    sleep(1)
    ans = "incorrect"
    while ans == "incorrect":
        if c1.capitalize() == "Revenge" or "revenge":
            print(
                """
        Xayah-I take a moment to slow down my mind to remember every detail of the humans who took Rakan.
        What did they look like?
        Where did they take Rakan?
        How will I get him back?
        What do I need to pull it off?
        Am I strong enough?
        """
            )
            sleep(4)

            ans = "correct"
            scene3()
        elif c1.capitalize() == "Rakan" or "rakan":
            print(
                """
        Xayah-"Time to get fight"
        """
            )
            ans = "correct"
            goback()
        elif c1.capitalize() != "Revenge" and c1.capitalize() != "Rakan":
            ans = "incorrect"
            print(
                """
            Please type a valid choice: Revenge or Rakan
        """
            )
            # Add try again instead of end program

            exit()

def goback():
    sleep(1)
    print(
        """
        Xayah-The wind is starting to pick up.
        I use this moment to get higher ground. Who knows how long the wind will continue.
        I laugh high into the air. Spreading my wings
        Allowing the air to carry me high above the prison grounds
        
        What happens during Xayah's flight?
        
        Does Xayah get shot down or sees Rakan?
        
        Type your choice: Shot or Rakan
    """
    )

    c1 = input()
    sleep(1)
    ans = "incorrect"
    while ans == "incorrect":
        if c1.capitalize() == "Shot" or "shot":
            print(
                """
        You died
        """
            )
            exit()
        elif c1.capitalize() == "Rakan" or "rakan":
            print(
                """
        Xayah-"There you are"
        I shot down like a storm of furry. Grab Rakan and forget this ever happened.
        """
            )
            ans = "correct"
            exit()
        if c1.capitalize() != "":
            print(
                """
            Please type a valid choice: Shot or Rakan
        """
            )
            # Add try again instead of end program

            exit()

def scene3():
    sleep(1)
    print(
        """
        Xayah-"Alright..
        There was four humans. Two in front of Rakan and two behind him."
        "They took him to the North entrance. How can I get there from here?"
        
        Does Xayah risk it all and go straight to the gate?
        Or
        Make a plan?
        Type:Risk or Plan
    """
    )
    c1 = input()
    sleep(1)
    ans = "incorrect"
    while ans == "incorrect":
        if c1.capitalize() == "Risk" or "risk":
            print(
                """
        Xayah-Knowing nothing matters but Rakan. I take a deep breath. Shake off any dark thoughts and start running directly to the North gate.
        Maybe I am not that far behind and can still save him.
        "Hold on my love! Im coming!"
        """
            )
            sleep(2)

            ans = "correct"
            scene4()
        elif c1.capitalize() == "Plan" or "plan":
            print(
                """
        Xayah-"I've killed more people in this place"
        I start to laugh
        """
            )
            ans = "correct"
            goback()
        if c1.capitalize() != "":
            print(
                """
            Please type a valid choice: Mess, Distracts, or Does
        """
            )
            # Add try again instead of end program

            exit()


def scene4():
    sleep(1)
    print(
        """
        Xayah-As my feathers are falling into all directions with a mind of their own.
        As I get closer to the North gate I can see traces of Rakan's golden feathers on the ground. He is close........
        "He better be ok or ELSE!"
        I stop right in front of two guards. One guard directly in front of me and another holding Rakan by the wrists.
        I smurk
        "Honey you ok?"
        Rakan-"Oh this is nothing, me and the guys were just going for a morning walk"
        Xayah- I roll my eyes. Even in danger he still has something smart to say
        Xayah-I snap my fingers and my quills tear through both guards.. leaving their corpes on the ground I take Rakan into my arms
    """
    )
    love()


def exit():
    sleep(2)
    print("Goodbye!")
    print("copyright:Carisa Saenz-Videtto")
    # Add retry
    sys.exit()


def love():
    sleep(2)
    print("Hoped you enjoyed the story")
    print("copyright:Carisa Saenz-Videtto")
    sys.exit()


if __name__ == "__main__":
    main()

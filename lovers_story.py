# runs your Python code
import sys

# script for pauses or delays
import time

# script to clear the terminal screen
import os

# imports only the sleep function from the time module
from time import sleep

#Introduction
def main():
    clear_screen()

    print("\nCast your mind back to the year 2009, when League of Legends was forged into existence.")
    print("Feel the weight of years, as the game grew, evolved, and etched its mark in the annals of gaming history.")
    print("Riot Games, the architects of this digital battleground, stand as pioneers in the vast world of multiplayer online battle arenas.")

    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            print(f"And you, {name}, have ventured into a League of Legends story.")
            break
        else:
            print("Invalid input! Please enter a name without numbers or punctuation.")
    
    # sleep(5)
    clear_screen()
    print("Yet, today is not about summoner spells or pixelated battles; it's about an adventure untold.")
    print("A choose-your-own odyssey where the destiny of two enchanting soulmates, Xayah and Rakan, lies in your hands.")
    print("Are you prepared to embark on this journey, shaping fate with every decision?")
    print("The stage is set. The tale awaits.")
    print("Let the adventure commence!\n\n\n")

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    


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
            Rakan-"You got it babe"
        """
        )

        print("What do you think Rakan does next?")
        print(
            " 1. Mess up the plan and gets caught\n 2. Distracts the guards and meets up with Xayah\n"
        )

        while True:
            c1 = input("Enter your choice (1 or 2): ")
            if c1.isdigit() and int(c1) in (1, 2):
                choice = int(c1)
                if choice == 1:
                    print(
        """
            Xayah-I am watching Rakan from a distance. Alright things are going smooth. Time to move. "NO NO! PLEASE! RAKAN!"
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
            I shake my head.
            Rakan-He walks over to Xayah "Your soul belongs to me"
            Xayah-I touch Rakan face "Lets go"
                        """
                    )
                    togetherRakan()
                    return
            else:
                print("Please type a valid choice: 1 or 2 ")

def layOnGround():
    while True:
        sleep(1)
        print(
            """
            Xayah-I passed out from the trauma of seeing my love being taken away by HUMANS!
            I slowly start to wake up
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
def togetherRakan():
    while True:
        sleep(1)
        print("""
            Xayah - The wind starts to pick up, and I take advantage of the opportunity to climb higher.
            Not knowing how long this favorable breeze will persist, I laugh aloud, my laughter resonating across the atmosphere as I expand my wings.
            I'm lifted above the jail premises by the currents, giving me a higher view of the landscape.
            My gaze focuses on Rakan as I soar; he is quick and nimble, leading the guards on a risky chase between the walls.
            I feel a mixture of pride and frustration as I watch his acrobatics below.
            I descend softly and land close to Rakan as he gathers his breath.
            Xayah- "I knew you could do it <3"
            Rakan: "I am know."
            Xayah - My conflicting emotions manifest, unsure whether to slap him, kiss him, or perhaps a combination of both.
            Shaking my head, I approach Rakan.
            Rakan strides over, a mischievous grin on his face.
            Rakan - "Your soul belongs to me."
            Xayah gently touches Rakan's face, a mixture of affection and determination in her eyes."
            Xayah - "Let's go."
        """
        )
        goChoice()
        return

def faceHumansOrRakan():
    while True:
        sleep(1)
        print(
            """
            Xayah moves in the direction of the gate. She takes a moment to step back,
            preparing to wreak havoc on those who have imprisoned her and taken Rakan.
            Xayah laughs out loud as she is carried effortlessly by the wind across the jail grounds,
            enjoying the freedom of flight and the vast space. Gazing downward from this perspective,
            she witnesses Rakan deftly dodging the approaching guards.
            Suddenly, there's danger as I float through the air. Crossbow-wielding enforcers in the air arrive on magical gliders.
            Xayah is in their sights.
            She floats through the air, suddenly overcome with a sense of threat.
            Enforcement on magical gliders bearing crossbows draw near. Their sights are set on Rakan.
            Now is the crucial moment for Xayah to decide:\n
Choice 4: As she continues to fly in the direction of Rakan, Xayah makes evasive maneuvers in an effort to dodge the incoming arrows.
Choice 5: Driven by fury, Xayah makes the decision to confront the enforcers directly in an effort to remove the threat and safeguard Rakan.      
            
        """
        )
        while True:
            c1 = input("Enter 4 or 5: ")
            if c1.isdigit() and int(c1) in (4, 5):
                choice = int(c1)
                if choice == 4:
                    print(
                        """
            Xayah- In a fit of rage I kill everyone in sight. Knowing there is nothing left.
                        """
                    )
                    RevPlan()
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

def RevPlan():
    while True:
        sleep(1)
        print(
            """
            Xayah-As I wake up from the horror that my own mind has been reminding me.
            A new day is burning my eyes from all the crying I must have been doing while I was asleep.
            Will I ever see Rakan again? Although it probably has been only moments his absence feels like a life time.
            "Where do I go from here?"
            What does Xayah do now?
            Takes a moment to seek revenge? Or Escape prison like planned without Rakan?
            Type: 6. Revenge or 7. Rakan
        """
        )
    
        sleep(1)

        while True:
            c1= input("Enter your choice (6 or 7): ") 
            if c1.isdigit() and int(c1) in (6, 7):
                choice = int(c1)
                if choice == 6:
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
                    sleep(1)
                    goChoice()
                    return
                elif choice == 7:
                    print(
                        """
                        Xayah-"Time to get fight"
                        """
                    )
                    return
            
            else:
                print(
                    """
                Please type a valid choice: 6 or 7
            """
                )



def goChoice():
    while True:
        sleep(1)
        print(
            """
            Xayah-The wind is starting to pick up.
            I use this moment to get higher ground. Who knows how long the wind will continue.
            I laugh high into the air. Spreading my wings.
            Allowing the air to carry me high above the prison grounds.
            I see Rakan
            
            What happens during Xayah's flight?
            
            Does Xayah get shot down or goes to Rakan?
            
            Type your choice: 8. Shoot or  9. Rakan
        """
        )

        while True:
            c1 = input("Enter your choice (8 or 9): ") 
            if c1.isdigit() and int(c1) in (8, 9):
                choice = int(c1)
                if choice == 8:
                    print(
                        """
            You died
                """
                    )
                    exit()
                elif choice == 9:
                    print(
                        """
                Xayah-"There you are"
                """
                    )
                    PlanRak()
                    return
            
            else:
                print(
                    """
                ("Please type a valid choice: 8 or 9")
            """
                )


def PlanRak():
    while True:
        sleep(1)
        print(
            """
            Xayah-"Alright..
            There was four humans. Two in front of Rakan and two behind him."
            "They took him to the North entrance. How can I get there from here?"
            
            Does Xayah risk it all and go straight to the gate?
            Or
            Make a plan?
            Type:10. Risk or 11. Plan
        """
        )
    
        while True:
            c1 = input("Enter your choice (10 or 11):")
            if c1.isdigit() and int(c1) in (10, 11):
                choice = int(c1)
                if choice == 10:
                    print(
                        """
                Xayah-Knowing nothing matters but Rakan. I take a deep breath. Shake off any dark thoughts and start running directly to the North gate.
                Maybe I am not that far behind and can still save him.
                "Hold on my love! Im coming!"
                """
                    )
                    sleep(1)            
                    Lastscene()
                    return
                elif choice == 11:
                    print(
                        """
                Xayah-"Take out two of the guards while Rakan deals with the other two guards."
                "Good enough for me let's save him"    
                """
                    )
                    return
            else:
                print("Please type a valid choice: 10 or 11")

            
def Lastscene2():
    while True:
        sleep(1)
        print("""
        Rakan-While I lay on the ground pretending to be dead I hear Xayah getting closer
        Xayah-"Can you stop playing around I saw you take out those guards than lay down."
        Rakan-"Hubba hubba. Someone was watching."
        Xayah- "Of course I am. Such a dork let's go home." I start to walk away.
        Rakan-"Wait for me!"
        
              """)
        love()

def Lastscene():
    while True:
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
    print("copyright: Carisa Saenz-Videtto")
    # Add retry
    sys.exit()


def love():
    sleep(2)
    print("Hoped you enjoyed the story")
    print("copyright:Carisa Saenz-Videtto")
    sys.exit()


if __name__ == "__main__":
    main()
    scene1()

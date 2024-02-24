import time

print('''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
''')
def slow_print(message, delay=0.035):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def slow_input(prompt, delay=0.035):
    slow_print(prompt, delay)
    return input()

slow_print("Welcome to Treasure Island.")
time.sleep(1)
slow_print("Your mission is to find the treasure.")
time.sleep(1)

def play_game():
    while True:
        left_or_right = slow_input("You wake up on an island, not knowing where you are. There is nothing but ocean in front of you, and a massive cliff behind you. You see skeletons and cracked skulls to the right, and seagulls flying overhead off in the distance to the left. Which way would you like to go? (left or right)\n").lower()
        time.sleep(1)
        if left_or_right == "right":
            slow_print("Against your better judgement, you follow the skeletons along the shoreline to the right. The ocean waves crash against the rocky beach. You hear a howling noise, and a ghostly voice above you saying 'YoU sHoUlD nOt HaVe CoMe HeRe!!'. You turn to look towards the voice, and the last thing you see is a ghastly pirate captain running you through with his sword.")
            death_message()
        elif left_or_right == "left":
            slow_print("Deciding to avoid the path of skeletons was probably your best idea ever. After giving yourself a high five and doing a heel click to celebrate your cleverness, you make your way to the left along the coast.")
            slow_print("As you get closer to where the birds are flocking, you notice a large tide pool filling with water beneath the seagulls with a sign that says 'NO RUNNING'. Far beyond the tide pool you see a small cave opening that seems to be lit.")
            run_or_wait = slow_input("You believe that you could walk across the tide pool if the water were to subside, but that could take hours. If you ran for it right now, the water might get too high before you reach the other end. What would you like to do? (run or wait)\n").lower()
            time.sleep(1)
            if run_or_wait == "run":
                slow_print("You decide that you can outrun the rising water and start sprinting as fast as you can, completely ignoring the 'NO RUNNING' sign.")
                slow_print("You look down and realize that the water is rising faster, and you hear a whistling sound behind you. Checking back where the sound came from, you see an octopus in a lifeguard uniform coming out of the water. You see its deep red eyes pierce your soul and you freeze, unable to move a muscle.")
                slow_print("The water raises past your calves, and up your thighs, it almost feels like you are sinking into the rock. As the beast breathes in and rushes towards you, you fall over into the water. The last thing you see is the octopus holding an identical 'NO RUNNING' sign as it forces you under. Your lungs fill up with water and you black out.")
                death_message()
            elif run_or_wait == "wait":
                slow_print("You decide to honor the 'NO RUNNING' sign, and wait out the tidepool. Within 30 minutes, you are able to safely cross.")
                slow_print("You come to the entrance of a small cave, you can see a few torches line the walls. Inside, there appear to be 3 doors, a red one, a yellow one, and a blue one.")
                door_choice = handle_doors()
                if door_choice != "yellow":
                    death_message()
                else:
                    slow_print("With a hopeful heart, you open the yellow door, and sunlight floods your senses. Before you lies a valley, lush and vibrant, filled with flowers of every imaginable color. The air is sweet with the scent of blooming life, and in the distance, a magnificent palace of gold and jewels sparkles under the sun. You step forward, and the ground seems to bless every step you take towards the treasure you've sought. As you enter the palace, rooms filled with gold, gems, and artifacts of incredible power await you. The voice of the island speaks, gentle and rewarding, 'Welcome, brave soul, to Paradise Found. Here lies the treasure of a thousand worlds, yours to claim.' You realize you've not just found wealth but a realm of wonders, a testament to the adventure of a lifetime. Your journey ends with you seated upon a throne, not of dominion, but of discovery, surrounded by the infinite treasure of knowledge and beauty.")
                    slow_print("Congratulations!! You win!!")
        if not play_again_prompt():
            slow_print("Thank you for playing, this window will close in a few seconds. Goodbye!")
            time.sleep (5)
            break  # Exit the while loop if player doesn't want to play again.

def death_message():
    slow_print("You have met a grim fate. You are dead.")

def play_again_prompt():
    play_again = slow_input("Would you like to try again? (y/n)\n").lower()
    time.sleep(1)
    return play_again == "y"

def handle_doors():
    door_choice = slow_input("Which door would you like to try first? (red, yellow, or blue)\n").lower()
    time.sleep(1)
    if door_choice == "red":
        slow_print("You approach the red door, its surface pulsing as if it's breathing. With a deep breath, you push the door open and step inside. The room is filled with a blinding light, and as your eyes adjust, you realize you're standing on a glass floor, beneath which is a sea of fire and molten lava. The door slams shut behind you, and the glass beneath your feet begins to crack. Panic sets in as you hear a voice, deep and sinister, echoing around you, 'Welcome to the Inferno's embrace.' The glass shatters, and you fall into the flames, your screams drowned out by the roar of the fire. Your journey ends in the scorching embrace of the underworld, where every moment stretches into an eternity of agony.")
    elif door_choice == "blue":
        slow_print("The blue door seems to hum with a cold energy as you approach. It swings open to reveal a room encased in ice, the air so cold it burns your lungs. In the center, a frozen throne sits, and on it, a figure with eyes that pierce your soul. 'Come forward,' it commands. As you step closer, the ground beneath you turns to ice, snaring your feet. The figure rises, its form blurring into a storm of snow and ice, swirling around you, cutting and chilling to the bone. 'You shall be my companion in this eternal winter,' the figure whispers as you feel your warmth slipping away, your body freezing solid. Your final thoughts are filled with a biting cold that consumes you, leaving you a frozen statue in the ice-bound dominion.")
    return door_choice

play_game()

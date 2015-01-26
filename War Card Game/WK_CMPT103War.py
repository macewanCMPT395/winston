# Course Project
# Name: Winston Kouch

# CMPUT 103 Project War Game
# Description: main() runs the game. Graphics done through graphics.py.
#              The majority of the game is run through mouse clicks on the window.
#              I have used the class Cards, splash screen, show cards, win screen,
#              high scores, ability to set rounds, animated decks, win piles
#              and the game is Player vs Computer.
#
# Syntax: main()
# Parameters: None
# Return Value: None

from graphics import *
import random
import time

# used as conditions to test for the drawing of deck states
# each card drawn represent 10 cards
cflag5 = 0
cflag4 = 0
cflag3 = 0
cflag2 = 0
cflag1 = 0
pflag5 = 0
pflag4 = 0
pflag3 = 0
pflag2 = 0
pflag1 = 0

# initializes battles remaining per round
battles_remaining = 26

# Description: Compares two cards to find out which value of card is higher and returns computer, player or tie wins
# Syntax: compare_cards(card1,card2)
# Parameters: card1 - computer card, card2 - player's card
# Return Value: c, p or 1 (meaning a tie)
def compare_cards(card1,card2):
    global t_Score, b_Score, round_counter, war_Pile,comp_stack, play_stack, player_Stack, comp_Card_Stack, play_Win_Pile, comp_Win_Pile, top_Card_Played, bot_Card_Played
    war_Text = Text(Point(640,40), "")
    war_Text.setSize(28)
    value = "23456789TJQKA"
    c1 = value.find(card1[1].upper())
    c2 = value.find(card2[1].upper())    
    # If top(computer) card is larger, give cards to computer win pile
    if c1 > c2:
        # move winnings to computer's win pile
        comp_Win_Pile.append(comp_Card_Stack.pop())
        comp_Win_Pile.append(player_Stack.pop())
        if len(war_Pile) > 0:
            war_Text.setText('Computer wins war')
        for i in range(len(war_Pile)):
            comp_Win_Pile.append(war_Pile.pop())        
        # move top and bot card played to computer's win pile
        # used 75 steps to make it look fluid
        for x in range(75):
            top_Card_Played.move(0, +5)
            bot_Card_Played.move(0, +2)
            time.sleep(0.005)                    
        for x in range(75):
            top_Card_Played.move(-5, 0)
            bot_Card_Played.move(-4, 0)
            time.sleep(0.005)
        for x in range(10):
            top_Card_Played.move(1, -2)
        for x in range(10):
            bot_Card_Played.move(-5, 2)
            time.sleep(0.005)
        # Set the winning computer pile count
        t_Score.setText(len(comp_Win_Pile))
        time.sleep(0.1)
        # Undraw the animation elements
        top_Card_Played.undraw()
        bot_Card_Played.undraw()
        
    # If bot player card is larger, give cards to bot
    if c1 < c2:
        # move winnings to player's win pile
        play_Win_Pile.append(player_Stack.pop())
        play_Win_Pile.append(comp_Card_Stack.pop())
        if len(war_Pile) > 0:
            war_Text.setText('Player wins war!')
        for i in range(len(war_Pile)):
            play_Win_Pile.append(war_Pile.pop())
        # move top and bot card played to player's win pile
        for x in range(75):
            top_Card_Played.move(0, +5)
            bot_Card_Played.move(0, +2)
            time.sleep(0.005)                    
        for x in range(75):
            top_Card_Played.move(-2, 0)
            bot_Card_Played.move(-2, 0)
            time.sleep(0.005)
        for x in range(10):
            top_Card_Played.move(1, -2)
        for x in range(10):
            bot_Card_Played.move(-5, 2)
            time.sleep(0.005)        
        # set the winning player's pile count
        b_Score.setText(len(play_Win_Pile))
        time.sleep(0.1)
        # Undraw the animation elements
        top_Card_Played.undraw()
        bot_Card_Played.undraw()        
    # If cards are the same value, go to War
    if c1 == c2:
        announce_tie = Text(Point(450, 100), "WAR!")
        announce_tie.setSize(30)
        announce_tie.setStyle('bold')
        announce_tie.draw(win)
        for x in range(80):
            announce_tie.move(0, 5)
            time.sleep(0.01)
        time.sleep(0.2)
        announce_tie.undraw()
        #Stick the cards being played into the war Pile to await next war
        war_Pile.append(comp_Card_Stack.pop())
        war_Pile.append(player_Stack.pop())            
        top_Card_Played.undraw()
        bot_Card_Played.undraw()            
        time.sleep(0.2)
        # Go to War
        war_Text.draw(win)
        war_Text.setText('Wage War!')
        time.sleep(0.2)
        # in the occurrence that the ties end up being ties,
        # both players get their cards back from the war pile
        if len(comp_Card_Stack) == 0 and len(player_Stack) == 0:
            # in each iteration, each player grabs their card back
            for i in range(len(war_Pile)//2):
                comp_Card_Stack.append(war_pile.pop())
                player_Stack.append(war_pile.pop())
    war_Text.undraw()        

# Description: Main function of the game. Makes the deck, creates the card table layout, shows the splash screen, draws the text elements, compares the cards, and writes and loads the highscore table at the end of the game.
# Syntax: main()
# Parameters: None
# Return Value: None
def main():         
    global win, war_Pile, t_Score, b_Score, battles_remaining, round_counter, battle_counter,comp_stack, play_stack, player_Stack, comp_Card_Stack, top_Card_Played, bot_Card_Played, comp_Win_Pile, play_Win_Pile, cflag5, cflag4, cflag3, cflag2, cflag1, pflag5, pflag4, pflag3, pflag2, pflag1
    
    # Use the class Cards to make a deck, shuffle and deal them
    make_cards = Cards()
    make_cards.shuffle()
    make_cards.deal()
    # make_cards.hands[0] is the computer's hand
    # make_cards.hands[1] is the player's hand
    
    # Create graphics window win and set background color to dark green
    win = GraphWin("Wild Warzone", 800, 600) 
    win.setBackground('darkgreen')
    
    # Display splash screen and return rounds user inputted
    rounds = splash_Screen()
    
    # Draw game elements and texts
    computer_title = Text(Point(150,120), "Computer Player: ")
    player_title = Text(Point(150,310), "Human Player: ")
    computer_title.draw(win)
    player_title.draw(win)
    game_Title = Text(Point(350, 30), 'Wild Warzone!')
    game_Title.setSize(32)
    game_Title.setFace('helvetica')
    game_Title.setStyle('bold italic')
    game_Title.draw(win)
    round_counter = Text(Point(250, 220), "Number of rounds: " + str(rounds))
    round_counter.draw(win)
    battle_counter = Text(Point(500, 220), "Battles remaining: " + str(battles_remaining))
    battle_counter.draw(win)
    
    # Draw the battle wins count of the players
    # Computer's score
    t_Score = Text(Point(50, 480), "0")
    t_Score.setSize(32)
    # Player's score
    b_Score = Text(Point(410, 480), "0")    
    b_Score.setSize(32)
    t_Score.draw(win)
    b_Score.draw(win)
    
    # initialize the stacks for drawing stack animation of win piles
    play_stack = []
    comp_stack = []
    
    # Draw the Win piles text
    comp_win_pile = Text(Point(130, 550), "Computer Win Pile")
    player_win_pile = Text(Point(330, 550), "Player Win Pile")
    comp_win_pile.draw(win)
    player_win_pile.draw(win)
    # set the two player hands
    comp_Card_Stack = make_cards.hands[0]
    player_Stack = make_cards.hands[1]
    # initializes the win piles and war pile
    comp_Win_Pile = []
    play_Win_Pile = []
    war_Pile = []
    game_running = True
    while game_running:
        win.getMouse()
        # Update battles remaining to one less
        battles_remaining = battles_remaining - 1      
        # check if battles end, are rounds done too?
        # if not done rounds, update rounds and reset battles_remaining
        if battles_remaining == 0 and rounds != 0:
            rounds = rounds - 1
            round_counter.setText("Number of rounds: " + str(rounds))
            battles_remaining = 26
            # Set the win piles to the decks of each player
            comp_Card_Stack = comp_Win_Pile
            player_Stack = play_Win_Pile
            comp_Win_Pile = []
            play_Win_Pile = []
            t_Score.setText('0')
            b_Score.setText('0')
            show_cards()
            top_Card_Played.undraw()
            bot_Card_Played.undraw()
            battles_remaining = battles_remaining - 1
            # Need to add a check if someone has all the cards
            battle_counter.setText("Battles remaining: " + str(battles_remaining))
        
        # Check if battles remaining = -1 and no more rounds to play, then the game is over
        # Show win screen, add who won to high score, then show the high score
        if rounds == 0:
            # comparison check between scores of computer and player
            comp_score = len(comp_Card_Stack) + len(comp_Win_Pile)
            play_score = len(player_Stack) + len(play_Win_Pile)
            if comp_score > play_score:
                winner = "Computer Wins"
            elif comp_score < play_score:
                winner = "Player Wins"
            else:
                winner = "Tie Game"
            # adds the winner to the high scores list showing 5 most recent games won
            add_high_score(winner)
            # creates win2 as the Winner Screen that shows the winner
            win2 = GraphWin("Winner Screen", 500, 500)
            win2.setBackground('red')
            winner_Text = Text(Point(200,200), winner)
            winner_Text.setSize(30)
            winner_Text.setStyle('bold')
            winner_Text.draw(win2)
            win2.getMouse()
            win2.close()
            # calls the high scores function which draws canvas and 5 recent high scores onto window
            high_Scores()
            win.getMouse()
            win.close()
            
        # Calls show_cards() to show Cards to show the flipping of cards from both players
        show_cards()
        # Updates message showing how many battles remaining
        battle_counter.setText("Battles remaining: " + str(battles_remaining))  
        
        # Compare the shown cards to see which is higher or a tie
        # if there is more cards left
        # Updates the win pile drawing for stack animation
        if len(comp_Card_Stack) and len(player_Stack) > 0:
            compare_cards(comp_Card_Stack[-1], player_Stack[-1])
            build_stack_play(play_stack, 330, 480)
            build_stack_comp(comp_stack, 130, 480)
            stack_draw_play(play_stack)
            stack_draw_comp(comp_stack)                    
        time.sleep(0.2)

# Description: Shows the cards graphically and shrinks as the stack diminishes
# Syntax: show_cards()
# Parameters: None
# Return Value: None
def show_cards():
    global win, comp_Card_Stack, player_Stack, top_Card_Played, bot_Card_Played, cflag5, cflag4, cflag3, cflag2, cflag1, pflag5, pflag4, pflag3, pflag2, pflag1
    global comp_stack_five, comp_stack_four, comp_stack_three, comp_stack_two, comp_stack_one, player_stack_one, player_stack_two, player_stack_three, player_stack_four, player_stack_five
    comp_vert_pos = 120
    player_vert_pos = 320
# Computer Deck Stack status drawer  
# # cflag1 = 10 cards, cflag2 = 20 cards, cflag3 = 30 cards, cflag4 = 40 cards, cflag5 = 50 cards
    if len(comp_Card_Stack) >= 10 and cflag1 == 0:
        comp_stack_one = Image(Point(260, comp_vert_pos), ("b1fv.gif"))
        comp_stack_one.draw(win)
        cflag1 = 1
    if len(comp_Card_Stack) >= 20 and cflag2 == 0:
        comp_stack_two = Image(Point(270, comp_vert_pos), ("b1fv.gif"))
        comp_stack_two.draw(win)
        cflag2 = 1
    if len(comp_Card_Stack) >= 30 and cflag3 == 0:
        comp_stack_three = Image(Point(280, comp_vert_pos), ("b1fv.gif"))
        comp_stack_three.draw(win)
        cflag3 = 1        
    if len(comp_Card_Stack) >= 40 and cflag4 == 0:
        comp_stack_four = Image(Point(290, comp_vert_pos), ("b1fv.gif"))
        comp_stack_four.draw(win)
        cflag4 = 1                
    if len(comp_Card_Stack) >= 50 and cflag5 == 0:
        comp_stack_five = Image(Point(300,comp_vert_pos), ("b1fv.gif"))
        comp_stack_five.draw(win)
        cflag5 = 1
    
# Undraws as cards diminish
    if cflag1 == 1 and len(comp_Card_Stack) < 10:
        comp_stack_one.undraw()
        cflag1 = 0
    if cflag2 == 1 and len(comp_Card_Stack) < 20:
        comp_stack_two.undraw()
        cflag4 = 0
    if cflag3 == 1 and len(comp_Card_Stack) < 30:
        comp_stack_three.undraw()
        cflag3 = 0
    if cflag4 == 1 and len(comp_Card_Stack) < 40:
        comp_stack_four.undraw()
        cflag4 = 0
    if cflag5 == 1 and len (comp_Card_Stack) < 50:
        comp_stack_five.undraw()
        cflag5 = 0
        
# Player Deck Stack Drawer
# pflag1 = 10 cards, pflag2 = 20 cards, pflag3 = 30 cards, pflag4 = 40 cards, pflag5 = 50 cards
    if len(player_Stack) >= 10 and pflag1 == 0:
        player_stack_one = Image(Point(260, player_vert_pos), ("b1fv.gif"))
        player_stack_one.draw(win)
        pflag1 = 1
    if len(player_Stack) >= 20 and pflag2 == 0:
        player_stack_two = Image(Point(270,player_vert_pos), ("b1fv.gif"))
        player_stack_two.draw(win)
        pflag2 = 1
    if len(player_Stack) >= 30 and pflag3 == 0:
        player_stack_three = Image(Point(280,player_vert_pos), ("b1fv.gif"))
        player_stack_three.draw(win)
        pflag3 = 1        
    if len(player_Stack) >= 40 and pflag4 == 0:
        player_stack_four = Image(Point(290,player_vert_pos), ("b1fv.gif"))
        player_stack_four.draw(win)
        pflag4 = 1                
    if len(player_Stack) >= 50 and pflag5 == 0:
        player_stack_five = Image(Point(300,player_vert_pos), ("b1fv.gif"))
        player_stack_five.draw(win)
        pflag5 = 1        

# Undraws as cards diminish
    if pflag1 == 1 and len(player_Stack) < 10:
        player_stack_one.undraw()
        pflag1 = 0
    if pflag2 == 1 and len(player_Stack) < 20:
        player_stack_two.undraw()
        pflag4 = 0
    if pflag3 == 1 and len(player_Stack) < 30:
        player_stack_three.undraw()
        pflag3 = 0
    if pflag4 == 1 and len(player_Stack) < 40:
        player_stack_four.undraw()
        pflag4 = 0
    if pflag5 == 1 and len (player_Stack) < 50:
        player_stack_five.undraw()
        pflag5 = 0    
      
# If there are cards in both player stack and comp stack,
# Flip 2 Cards from their deck stacks
    if len(comp_Card_Stack) and len(player_Stack) > 0:
        # Draw Computer and Player Deck
        comp_deck = Image(Point(290, 120), ("b1fv.gif"))
        player_deck = Image(Point(290, 320), ("b1fv.gif"))
        comp_deck.draw(win)
        player_deck.draw(win)        
        # Animation portion images to animate flipping cards
        top_deck_drawstack = Image(Point(290, 120), ("b1fv.gif"))
        bot_deck_drawstack = Image(Point(290, 320), ("b1fv.gif"))
        top_deck_drawstack.draw(win)
        bot_deck_drawstack.draw(win)
        # Animation for flipping cards action
        for x in range(20):
            top_deck_drawstack.move(0, -3)
            bot_deck_drawstack.move(0, +3)
            time.sleep(0.005)                    
        for x in range(40):
            top_deck_drawstack.move(5, 0)
            bot_deck_drawstack.move(5, 0)
            time.sleep(0.005)        
        for x in range(20):
            top_deck_drawstack.move(0, +3)
            bot_deck_drawstack.move(0, -3)
            time.sleep(0.005)
        top_deck_drawstack.undraw()
        bot_deck_drawstack.undraw()
        #Display's the top and bottom card currently in battle
        top_Card_Played = Image(Point(490, 120), (comp_Card_Stack[-1].lower() + ".gif"))
        top_Card_Played.draw(win)
        bot_Card_Played = Image(Point(490, 320), (player_Stack[-1].lower() + ".gif"))
        bot_Card_Played.draw(win)    
    
# Description: Display Splash screen, stays up for 5 seconds and then asks user for number of rounds to play
# After that, user can click anywhere in window to start the game. (Default: 1)
# Syntax: rounds = splash_Screen()
# Parameters: None
# Return Value: Number of rounds user specifies to play
def splash_Screen():
    closing = ""
    intro = """
    Hi! Welcome to Wild Warzone. It is a remake of the card game War.
    There are two players, top and bottom. Using a standard deck of 52 
    cards, the cards rank from high to low, A K Q J 10 9 8 7 6 5 4 3 2.    
    Suit has no role. The objective of the game is to win all the cards.      
    By placing a higher card than your opponent, you receive the card.    
    """    
    # Draws the rectangle splash box
    rect = Rectangle(Point(100, 50), Point(700, 500))
    rect.setFill('brown')
    rect.draw(win)
    
    # Draw Splash Title of Game and set constraints for text style.
    banner_Text = Text(Point(400, 100), 'Wild Warzone!')
    banner_Text.setSize(32)
    banner_Text.setFace('helvetica')
    banner_Text.setStyle('bold italic')
    intro_Text = Text(Point(380, 200), intro)
    intro_Text.setSize(14)
    closing_Text = Text(Point(640, 470), closing)
    closing_Text.draw(win)
    intro_Text.draw(win)
    banner_Text.draw(win)
    
    # Keeps splash screen on screen using 1 second sleeps for a total of 5 secs.
    for i in range(5):
        closing = "Closing in " + str(5-i) + " . . ."
        closing_Text.setText(closing)
        time.sleep(1)
    closing_Text.undraw()
    
    # Display text asking how many rounds you would like to play    
    ask_rounds=Text(Point(375,350),"How many rounds would you like to play?")
    ask_rounds.draw(win)
    
    # Shows user where to input the number of games
    start_num = Text(Point(350,400), "Number of games:")
    start_num.draw(win)
    
    # Create entry box to get input    
    user_input = Entry(Point(460,400), 3)
    user_input.setText("1")
    user_input.draw(win)
    # Tell the user to click the start button to start the game
    start_info = Text(Point(375,450),"Please set the number of rounds and then click anywhere to start the game")
    start_info.draw(win)    
    # Assigns user input to a variable and clears the splash screen on mouse click
    win.getMouse()
    rounds = eval(user_input.getText())    
        
    # Undraws splash screen elements in preparation to load game play.
    ask_rounds.undraw()
    user_input.undraw()
    start_info.undraw()
    start_num.undraw()
    banner_Text.undraw()
    intro_Text.undraw()
    rect.undraw()
    
    #Return inputted number of rounds the user would like to play
    return rounds

# High Scores portion of the bonus
# Description: Reads the last 5 recent games of who won
# Syntax: high_Scores()
# Parameters: None
# Return Value: None
def high_Scores():
    # Store 5 recent games of who won, player or computer
    highscore_list = []
    try:
        file = open('hst.txt', 'r')
    except FileNotFoundError:
        print("The file", file, "does not exist.")
        return None
    #Read in the high scores table from hst.txt
    lines = file.readlines()
    file.close()
    #Draw a canvas for the high score screen listing
    draw_rect = Rectangle(Point(20,50), Point(780,580))
    draw_rect.setOutline("black")
    draw_rect.setFill("red")
    draw_rect.draw(win)
    # y is 50 pixels lower for each score
    y = 50
    # Organizes the 5 scores to be listed 50 pixels below each other
    # the str(i+1) + "." creates the number listing behind each so it outputs
    # ie. 1. Player Wins
    #     2. Tie Game
    #     3. Tie Game
    for i in range(len(lines)):
        highscore_list.append(Text(Point(380, 200+i*y), str((i+1)) + ". " + lines[i]))
    for i in range(5):
        highscore_list[i].setSize(14)
        highscore_list[i].setStyle('bold')
        highscore_list[i].draw(win)    

# Description: Adds high score at the end of your game when battles reaches 0
# Syntax: add_high_score()
# Parameters: winner
# Return Value: None
def add_high_score(winner):
    #Store 5 recent games of who won, player or computer
    try:
        file = open('hst.txt', 'r')
        #win.getMouse()
    except FileNotFoundError:
        print("The file", file, "does not exist.")
    file = open('hst.txt', 'r')    
    lines = file.readlines()    
    file.close()
    lines.insert(0, str(winner+"\n"))
    file = open('hst.txt', 'w')
    for x in range(5):
        file.write(lines.pop(0))
    file.close()
        
# Classes portion of the bonus
# Description: Creates class Cards which generates a deck of cards, shuffles them and then deals 2 hands, one for computer and one for player
#              make_cards.hands[0] = computer's hand and make_cards.hands[1] = player's hand
# Syntax: make_cards = Cards()
# Methods: shuffle(deck) - shuffles deck and deal() deals 2 hands

class Cards:
    def __init__(self):
        #initialize the deck
        self.deck = []
        # card and suit list to create the 52 cards
        card_List = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suit_List = ['H', 'C', 'S', 'D']
        # creates the deck and appends the combinations to make a deck
        for card in card_List:
            for suit in suit_List:
                self.deck.append(suit + card)
                
# Shuffles the deck                        
    def shuffle(self):
        random.shuffle(self.deck)
        
# 2 player game so it deals the deck to 2 hands, 26 cards each
    def deal(self):
        self.hands = [self.deck[i::2] for i in range(0, 2)]
        
# Build stacks for Win Piles - Computer
# Description: Builds the stack images to be used for draw stacks
# Syntax: build_stack_comp(stack, x, y)
# Parameters: stack - stack to be used, x - coord, y - y coord
# Return Value: None
def build_stack_comp(stack, x, y):
    global comp_Win_Pile
    for card in range(52):
        stack.append(Image(Point(x, y), "b1fh.gif"))
        # down an extra 2 pixels for each card
        y += -2
        
# Build stacks for Win Piles - Player
# Description: Builds the stack images to be used for draw stacks
# Syntax: build_stack_play(stack, x, y)
# Parameters: stack - stack to be used, x - coord, y - y coord
# Return Value: None
def build_stack_play(stack, x, y):
    global play_Win_Pile
    for card in range(52):
        stack.append(Image(Point(x, y), "b1fh.gif"))
        y += -2   
        
# Draw stacks for Win Piles
# Description: Draws and undraws the stack in accordance to the size of the win pile, top being the computer's
# Syntax: stack_draw_comp(stack)
# Parameters: stack - the computer's stack of win cards
# Return Value: None
def stack_draw_comp(stack):
    for i in stack:
        i.undraw()
    for i in range(len(comp_Win_Pile)):
        stack[i].draw(win)

# Description: Draws and undraws the stack in accordance to the size of the win pile, bot being the player's
# Syntax: stack_draw_play(stack)
# Parameters: stack - the player's stack of win cards
# Return Value: None
def stack_draw_play(stack):
    for i in stack:
        i.undraw()
    for i in range(len(play_Win_Pile)):
        stack[i].draw(win)
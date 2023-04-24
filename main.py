import pygame
from pygame import *
# import function to randomize title and draw text
from text import random_title, draw_text
# Contains all the assets required for canvas
from assets import ore_image, window, WHITE, BLACK, AQUA, RED, MAGENTA, GREEN, YELLOW, pickaxe_image
# import ore class
from ore import Ore
# import picaxe class
from pickaxe import Pickaxe
# import score class
from score import Score
# import tools class
from tool import tool_list, calculate_ops, tool_buttons

# Creating base screen for pygame.
clock = pygame.time.Clock()
pygame.init()

# Set desktop icon
pygame.display.set_icon(ore_image)
# sets title font
arial_title = font.SysFont('arial', 48)
# set normal arial font
arial = font.SysFont('arial', 18)

mouse_click = False
tools = tool_list

def main():
    '''Screen for main menu, can enter the game screen or help manual from this screen.'''
    main_running = True
    # sequence of keyboard inputs required to trigger event
    secret_code = [
        # K_s # <-- uncomment this and comment below if you want to have an easier code for
        K_s, K_e, K_d, K_i, K_r, K_o, K_l, K_h, K_c, K_SPACE, K_m, K_u, K_i, K_d, K_o, K_s
    ]
    # track amount for event
    secret_index = 0
    # Set title for pygame
    pygame.display.set_caption(random_title)
    # event loop
    while main_running:

        # fill background
        window.fill(AQUA)

        # position for mouse
        x, y = pygame.mouse.get_pos()

        # buttons to enter other screens
        start_game_button = Rect(50, 160, 400, 70)
        help_menu_button = Rect(50, 300, 400, 70)

        # draw buttons for entering screens
        pygame.draw.rect(window, MAGENTA, start_game_button)
        pygame.draw.rect(window, WHITE, help_menu_button)

        # text for buttons
        draw_text('Start Game (ENTER)', arial_title, BLACK, window, 60, 165)
        draw_text('Help Menu (TAB)', arial_title, BLACK, window, 60, 305)

        # event for if mouse hover on button

        # if mouse clicks on start game button, start game
        if start_game_button.collidepoint((x, y)):
            if mouse_click:
                start_game()

        # if mouse button clicks on help menu pull up help menu

        if help_menu_button.collidepoint((x, y)):
            if mouse_click:
                help_menu()

        mouse_click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                main_running = False
            # for keyboard events
            if event.type == KEYDOWN:
                # tracks sequence for secret event
                if event.key == secret_code[secret_index]:
                    secret_index += 1  # add one if key press is in index
                    pygame.display.set_caption(
                        "_ _ _ _ _ _ _ _  _ _ _ _ _ _ ⸮fo pu edam tlas si tahW ")
                    if secret_index == len(secret_code):
                        secret_menu()
                        secret_index = 0
                else:
                    secret_index = 0  # set to zero if key press is not in index
                    pygame.display.set_caption(random_title)
                # if the player presses ESC quit the game
                if event.key == K_ESCAPE:
                    main_running = False
                if event.key == K_RETURN:
                    start_game()
                    main_running = False
                if event.key == K_TAB:
                    help_menu()
            # for mouse events
            if event.type == MOUSEBUTTONDOWN:
                # for left click
                if event.button == 1:
                    mouse_click = True

        # create title on screen
        draw_text('Ore Excavation', arial_title, BLACK, window, 100, 20)

        # set FPS to 60
        clock.tick(60)

        # Update display
        pygame.display.update()

    # quit game
    pygame.quit()


def secret_menu(mouse_click=False):
    '''Screen accessing secrets_menu, the real purpose of this screen is to allow
    testing for certain bonuses such as double and lottery. This menu will
    allow the player to start the game with these certain bonuses The 
    player is not normally supposed to start with this feature. '''
    secret_running = True
    # Set title for pygame
    pygame.display.set_caption("...")
    while secret_running:
        mouse_click = False
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # for mouse events
            if event.type == KEYDOWN:
                if event.key == K_s:
                    pygame.display.set_caption("S is for ...")
                if event.key == K_ESCAPE:
                    main()
            if event.type == MOUSEBUTTONDOWN:
                # for left click
                if event.button == 1:
                    mouse_click = True

        # fill background
        window.fill(AQUA)

        # position for mouse
        x, y = pygame.mouse.get_pos()

        # button to return to game
        proceed_button = Rect(50, 280, 400, 70)
        return_menu = Rect(50, 400, 400, 70)

        # draw buttons for going back to game
        pygame.draw.rect(window, WHITE, return_menu)
        pygame.draw.rect(window, WHITE, proceed_button)

        # collision for buttons
        if proceed_button.collidepoint((x, y)):
            if mouse_click:
                bonus_menu()
        if return_menu.collidepoint((x, y)):
            if mouse_click:
                main()

        # text for buttons
        draw_text('Proceed Anyways', arial_title, BLACK, window, 100, 285)
        draw_text('Return (ESC)', arial_title, BLACK, window, 125, 400)

        # create title on screen
        draw_text('Secrets Menu', arial_title, BLACK, window, 100, 20)

        # draw secrets descriptions
        draw_text('Welcome to the secrets menu, within this menu, users can select ',
                  arial, BLACK, window, 10, 100)
        draw_text('any bonuses that they wish to start the game with. Please take note ',
                  arial, BLACK, window, 10, 140)
        draw_text('that players are not normally supposed to start with these bonuses ',
                  arial, BLACK, window, 10, 180)
        draw_text('which may alter the game experience in unintended ways. ',
                  arial, BLACK, window, 10, 220)

        # set FPS to 60
        clock.tick(60)

        # Update display
        pygame.display.update()

    # quit game
    pygame.quit()


def help_menu(mouse_click=False):
    '''Screen for opening help manual, can go back to main menu from this screen'''
    help_running = True
    # event loop for help menu
    # set title for pygame
    pygame.display.set_caption("Reading about Ore Excavation?")

    while help_running:
        mouse_click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # for keyboard events
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
                if event.key == K_s:
                    pygame.display.set_caption("sʇǝɹɔǝs ɹoɟ sᴉ s")
            # for mouse events
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        # fill background
        window.fill(AQUA)

        # postion for mouse
        x, y = pygame.mouse.get_pos()

        # button to return to main menu
        return_menu = Rect(50, 420, 400, 70)

        # draw buttons for going back to menu
        pygame.draw.rect(window, WHITE, return_menu)

        # text for button
        draw_text('Main Menu (ESC)',
                  arial_title, BLACK, window, 100, 425)

        # draw heading
        draw_text('Help Manual', arial_title, BLACK, window, 125, 20)
        # draw manual
        draw_text('The goal of the game is getting 1 million ores. You will get 1 ore every ',
                  arial, BLACK, window, 10, 100)
        draw_text('time you click on the rock at the center of the screen. You can also ',
                  arial, BLACK, window, 10, 140)
        draw_text('trade in ores for upgrades to your pickaxe or to buy excavation tools. ',
                  arial, BLACK, window, 10, 180)
        draw_text('Upgrading your pickaxe will allow you to earn more ores every time you ',
                  arial, BLACK, window, 10, 220)
        draw_text('click, and the excavation tools will passively generate rocks every ',
                  arial, BLACK, window, 10, 260)
        draw_text('few seconds.', arial, BLACK, window, 10, 300)
        draw_text('Try pressing S, somewhere ...',
                  arial, BLACK, window, 10, 340)

        # statement for tracking clicks for button
        if return_menu.collidepoint((x, y)):
            if mouse_click:
                main()
        # set FPS to 60
        clock.tick(60)

        # Update display
        pygame.display.update()


def start_game(score=None, tools=tools, mouse_click=False):
    '''Screen for playing game, takes an optional argument for score class'''
    game_running = True
    # create instance of ore
    ores = pygame.sprite.Group()
    ore = Ore(ore_image, 125, 70)
    pickaxe = Pickaxe(pickaxe_image, 0, 0)
    ores.add(ore)

    ops = calculate_ops(tools)

    # Set title for pygame
    pygame.display.set_caption("Welcome to Ore Excavation")
    # creates an instance of score if score is none
    if score == None:
        scores = Score()
    else:
        scores = score
    lottery_event = pygame.USEREVENT + 1  # create custom user event
    tool_event = pygame.USEREVENT + 2
    if scores.lottery == True:  # if lottery is true start a timer for lottery pulls
        # occurs every 30 seconds or 30000 miliseconds
        pygame.time.set_timer(lottery_event, 30000)

    # event timer for tool payout occurs every second or 1000 miliseconds
    pygame.time.set_timer(tool_event, 1000)

    # event loop for game
    while game_running:
        mouse_click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == lottery_event:
                # calls the lottery function from scores class
                scores.pull_lottery()
            if event.type == tool_event:
                # goes through list of tools and adds each score's income to the score
                for tool in tools:
                    scores.add_score(tool.income * tool.amount)
            # for keyboard events
            if event.type == KEYDOWN:
                if event.key == K_s:
                    shop_menu(scores, tools)
            # for mouse events
            if event.type == MOUSEBUTTONDOWN:
                # for left click
                if event.button == 1:
                    mouse_click = True

        # fill background
        window.fill(AQUA)

        # position for mouse
        x, y = pygame.mouse.get_pos()

        # Draw the ore in the center of the screen
        ore.draw(window)

        # button for shop
        shop_menu_button = Rect(50, 420, 400, 70)

        # draw buttons for entering screens
        pygame.draw.rect(window, GREEN, shop_menu_button)

        # text for score
        draw_text(
            f'Your current score is: {scores.points} ore.', arial, BLACK, window, 50, 25)
        
        # text for showing current ore gain from tools
        draw_text(f'You are passively gaining {ops} ores per second.', arial, BLACK, window, 50, 50)

        # text for buttons
        draw_text('Enter Shop (S)', arial_title, BLACK, window, 120, 425)

        if ore.rect.collidepoint((x, y)):
            if mouse_click:
                scores.add_score()

        if shop_menu_button.collidepoint((x, y)):
            if mouse_click:
                shop_menu(scores, tools)

        # Checks if the player has reached the win condition
        # If the player has reached it go to the win screen
        if scores.points >= scores.win:
            # if the player has already completed the game don't swap
            if not scores.completed:
                win_menu(scores, tools)

        # set FPS to 60
        clock.tick(60)

        pygame.mouse.set_visible(False)
        # Draw the pickaxe sprite
        pickaxe.draw(window)

        # Updates the position of the pickaxe sprite to the user's cursor
        pickaxe.update_postion(x, y)

        # Update display
        pygame.display.update()

    # quit game
    pygame.quit()


def shop_menu(scores, tools, mouse_click=False):
    '''Screen for buying upgrades, takes an arugment for score class'''
    shop_running = True
    score = scores
    # set title for pygame
    pygame.display.set_caption("Welcome to the Mines! Press ESC if you wish to return.")
    while shop_running:
        mouse_click = False
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # for keyboard events
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    start_game(score, tools)
                if event.key == K_s:
                    pygame.display.set_caption("Nothing here!")
            # for mouse events
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        # fill background
        window.fill(AQUA)

        # postion for mouse
        x, y = pygame.mouse.get_pos()

        # draw heading
        draw_text('The Shop', arial_title, BLACK, window, 150, 5)

        # button to upgrade pickaxe
        upgrade_pickaxe = Rect(275, 70, 200, 50)

        # draw buttons for upgrades
        pygame.draw.rect(window, RED, upgrade_pickaxe)

        # text for canvas
        draw_text(f'Increase your ores per click (OPC)',
                  arial, BLACK, window, 10, 70)
        draw_text(f'Price: {score.price} ore.',
                  arial, BLACK, window, 10, 95)
        # text for buttons
        draw_text(
            f'Upgrade Pick:{score.multiplier} OPC', arial, BLACK, window, 280, 85)
        
        # for loop with zip for looping through tool_list and tool_buttons to draw text and buttons for every button specified
        for button, tool in zip(tool_buttons, tool_list):
            pygame.draw.rect(window, GREEN, button)
            draw_text(
                f'{tool.name}: {round(tool.income * tool.amount, 1)} OPS', arial, BLACK, window, button.x + 5, button.y + 10)
            draw_text(
                tool.description, arial, BLACK, window, button.x - 265, button.y)
            draw_text(
                f'Price: {tool.price} ore. {tool.income} OPS', arial, BLACK, window, button.x - 265, button.y + 25)
        
        # for loop with zip for looping through tool_list and tool_buttons to add clicks to them
        for button, tool in zip(tool_buttons, tool_list):
            if button.collidepoint((x, y)):
                if mouse_click:
                    tool.purchase_tools(score)

        # click for shop items
        if upgrade_pickaxe.collidepoint((x, y)):
            if mouse_click:
                score.increase_multiplier()
        # set FPS to 60
        clock.tick(60)

        # Update display
        pygame.display.update()


def win_menu(scores, tools=None, mouse_click=False):
    '''Screen for if the player has won, takes arugment for score class'''
    win_running = True
    score = scores
    # Set title for pygame
    pygame.display.set_caption("Congratulations you won")
    while win_running:
        mouse_click = False
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # for mouse events
            if event.type == KEYDOWN:
                if event.key == K_s:
                    pygame.display.set_caption(
                        "Waiting for something to happen?")
            if event.type == MOUSEBUTTONDOWN:
                # for left click
                if event.button == 1:
                    mouse_click = True

        # fill background
        window.fill(AQUA)

        # position for mouse
        x, y = pygame.mouse.get_pos()

        # button to return to game
        continue_button = Rect(50, 100, 400, 70)
        bonuses_button = Rect(50, 280, 400, 70)

        # draw buttons for going back to game
        pygame.draw.rect(window, WHITE, continue_button)
        pygame.draw.rect(window, WHITE, bonuses_button)

        # create title on screen
        draw_text('You Win!', arial_title, BLACK, window, 150, 20)
        # text for buttons
        draw_text('Continue?', arial_title, BLACK, window, 125, 105)
        draw_text('New Game+', arial_title, BLACK, window, 125, 285)

        # draw secrets descriptions
        draw_text('If you choose continue you will be able to keep playing the game indefinitely',
                  arial, BLACK, window, 10, 180)
        draw_text('The player will keep their upgrades and tools if they choose this ',
                  arial, BLACK, window, 10, 220)
        draw_text('New Game+ will allow players to select bonuses and restart the game with',
                  arial, BLACK, window, 10, 360)
        draw_text('no upgrades but bonuses. The win condition will be increased from',
                  arial, BLACK, window, 10, 390)
        draw_text('1 million to 100 million to 1 billion. If the player already has all bonuses, ',
                  arial, BLACK, window, 10, 420)
        draw_text('the bonuses button will no longer work. ',
                  arial, BLACK, window, 10, 450)
        
        # event for continue button, sets completed to true so no longer prompts win screen
        if continue_button.collidepoint((x, y)):
            if mouse_click:
                score.completed = True
                # checks if the player has tools or not
                if tools:
                    start_game(score, tools)
                else:
                    start_game(score)

        # button for going to bonus menu
        if bonuses_button.collidepoint((x, y)):
            if mouse_click:
                # checks if player already has both of the bonuses
                if score.lottery and score.double:
                    # if they already have the bonuses increase the win to one quadrillion
                    print("You already have all the bonuses")
                else:
                    bonus_menu(score)
        # set FPS to 60
        clock.tick(60)

        # Update display
        pygame.display.update()

    # quit game
    pygame.quit()


def bonus_menu(scores=None, mouse_click=False):
    '''Screen player can enter from the win-menu, takes scores class as argument
    allows players to receive bonuses after winning the game. There are two
    bonuses at the moment. It will pass a new score class with the new bonuses, allowing
    the player to enter a new game+ with the new bonuses'''
    secret_running = True
    # Set title for pygame
    pygame.display.set_caption("Which one will it be")
    while secret_running:
        mouse_click = False
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # for mouse events
            if event.type == KEYDOWN:
                if event.key == K_s:
                    pygame.display.set_caption("Nothing to see here. ")
            if event.type == MOUSEBUTTONDOWN:
                # for left click
                if event.button == 1:
                    mouse_click = True

        # fill background
        window.fill(AQUA)

        # position for mouse
        x, y = pygame.mouse.get_pos()

        # button to return to game
        lottery_button = Rect(50, 100, 400, 70)
        double_button = Rect(50, 320, 400, 70)

        # draw buttons for going back to game
        pygame.draw.rect(window, YELLOW, lottery_button)
        pygame.draw.rect(window, GREEN, double_button)

        # create title on screen
        draw_text('Bonus Menu', arial_title, BLACK, window, 125, 20)

        # text for buttons
        draw_text('Lottery Bonus', arial_title, BLACK, window, 125, 105)
        draw_text('Double Bonus', arial_title, BLACK, window, 125, 325)

        # click detection onbuttons
        if lottery_button.collidepoint((x, y)):
            if mouse_click:
                if scores and scores.lottery:  # Checks if the player already has lottery bonus
                    print("You already have this bonus")
                    # this screen will only recieve the score class if the player has beaten the game
                    # if the player has beaten the game, the next win will require 1 billion points
                    # this function is like a new game +
                else:
                    win_condition = 100000000 if scores else 1000000
                    if scores and scores.double:  # if the player has beaten the game twice and chosen double bonus
                        # this will set lottery and double bonuses to true
                        # this will also set the win condition to 1 trillion points
                        win_condition = 1000000000
                    score = Score(
                        0, 1, 10, False, scores.double if scores else False, True, win_condition)
                    start_game(score)
        if double_button.collidepoint((x, y)):
            if mouse_click:
                if scores and scores.double:
                    print("You already have this bonus")
                else:
                    win_condition = 100000000 if scores else 1000000
                    if scores and scores.lottery:  # similar to lottery button
                        win_condition = 1000000000
                    score = Score(
                        0, 1, 10, False, True, scores.lottery if scores else False, win_condition)
                    start_game(score)

        # draw bonus descriptions
        draw_text('The lottery is a special bonus that will draw 2 lots. The payout will depend',
                  arial, BLACK, window, 10, 200)
        draw_text('on the result of the lots This event will occur every 30 seconds. ',
                  arial, BLACK, window, 10, 240)
        draw_text('Double is a bonus that will give a 50/50 chance to get double ore every click',
                  arial, BLACK, window, 10, 420)

        # set FPS to 60
        clock.tick(60)

        # Update display
        pygame.display.update()

    # quit game
    pygame.quit()


if __name__ == "__main__":
    main()

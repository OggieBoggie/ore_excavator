import pygame, random

def draw_text(text, font, color, screen, x, y):
    '''Takes multiple arguments for text, font, color, screen and postions.'''
    # rendered text
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.topleft = (x, y)
    # display text in window
    screen.blit(text_render, text_rect)

def generate_title():
    '''Has a list of random titles, appends a random title from the list'''
    titles = {
        "Ore Excavation: Are you ready to mine?",
        "Ore Excavation: The rocks are playing",
        "Ore Excavation: Rise of the Rocks",
        "Ore Excavation: Now in 2D",
        "Ore Excavation: 1+1 = 0",
        "Ore Excavation: Also try Cookie Clicker!",
        "Ore Excavation: Press alt-f4!",
        "Ore Exacavation: Do you notice the title?",
        "Ore Excavation: Divide by zero",
        "Ore Excavation: Also try ESC",
        "Ore Excavation: May the ores be with you",
        "Ore Excavation: I've got a boulder problem that I can't get over",
        "Ore Excavation: Same six stones",
        "ORE EXCAVATION",
        "Ore Excavation: I am always watching",
        "Ore Excavation: WHERE 1 = 1"
    }
    return random.choice(list(titles))

random_title = generate_title()
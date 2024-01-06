# Ore Excavation

## Overview
"Ore Excavation" is an engaging clicker game where your primary goal is to collect 1 million ores. Start by clicking on a rock at the center of the screen to collect ores. You can trade your ores for upgrades to your pickaxe or buy various excavation tools. Upgrading your pickaxe increases the number of ores you get per click, while excavation tools passively generate ores over time.

## Main Features
- **Gameplay**: Click to collect ores and use them to purchase upgrades and tools.
- **Upgrades**: Enhance your pickaxe for increased ore collection on each click.
- **Passive Generation**: Acquire tools that automatically generate ores.

## main.py
This is the main script of the game and includes:

- Declaration of a clock variable.
- Creation of instances for the `Ore`, `Score`, and `Tools` classes.
- Setting the application icon.
- Definition of Arial fonts for titles and texts.
- Mouse click tracking.
- Importing `asset.py` for handling game assets like colors and images, and managing the screen size.
- Importing `text.py` which includes methods for drawing text and generating titles.

## Supported Screens
- **Secret Screen**: Accessible through a special code, offers game-start bonuses.
- **Bonus Screen**: Showcases available bonuses.
- **Win Screen**: Displayed upon achieving the game goal.
- **Help Manual**: Offers gameplay instructions and navigational help.
- **Game Screen**: The main gameplay area.
- **Shop Screen**: For purchasing upgrades and tools.
- **Main Menu**: Starting point of the game.

## Classes
### Ore
- Represents the ore with attributes like image and rectangle.
- Interacts with the Pickaxe class.

### Pickaxe
- The player's sprite with attributes including image, rectangle, and score multiplier.
- Follows the player’s cursor.

### Score
- Manages the player's score with attributes like the current score, multiplier, and upgrade prices.
- Includes methods for scoring mechanics and bonuses.

### Tools
- Represents various tools with attributes like name, amount, and score value.
- Tools generate score passively and have methods for managing and displaying tool amounts.

### Shop
- Allows players to purchase upgrades and tools.
- Provides a graphical interface for transactions.

## Bonuses
- Earn bonuses by completing the game.
- Includes bonuses like a double score chance and a lottery system for extra rewards.

## Installation and Running the Game
1. Clone the repository or download the source code.
2. Ensure Python is installed on your system.
3. Install the dependencies with `pip install -r requirements.txt`
4. Navigate to the game directory and run `python main.py`.


# cse210-cycles
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them. 
Cycle is played according to the following rules:
Players can move up, down, left and right...
Player one moves using the W, S, A and D keys.
Player two moves using the I, K, J and L keys.
Each player's trail grows as they move.
Players try to maneuver so the opponent collides with their trail.
If a player collides with their opponent's trail...
A "game over" message is displayed in the middle of the screen.
The cycles turn white.
Players keep moving and turning but don't run into each other.
The game has 16 classes. Each class performs only its specific function, which supports the principle of abstraction in OOP. The Action and Actor classes contain child classes, which corresponds to the principle of inheritance. For example, the Cycle subclass of the Actor class takes all the attributes of this class and adds its own specific functions, which determine how the Actor (because Cycle is an Actor) will look like and where he will be situated ( in the game -- 2 players of different colors with different starting positions). Subclasses of the Action class (ControlActorsAction, DrawActorsAction, HandleCollisionsAction, MoveActorAction) perform the Execute() function defined in it, but each class overrides it in accordance with its own actions. This fulfills the principle of polymorphism.
#Project Structure
The project files and folders are organized as follows:

root                    (project root folder)
+-- cycles              (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (constant values for teh game)
+-- README.md           (general info)
#Required Technologies
Python 3.8.0
Raylib Python CFFI 3.7
#Author
Marina Kreibring (timarina1997@yahoo.com)
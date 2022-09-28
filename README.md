# Littleships-Minigame
"Small boats fighting modest battles on diminutive bodies of water."

## Overview: 
A single-player game written in python3. The player has 15 shots to sink 5 littleships in a 5x5 grid. The player shoots one shot at a time until the boats are sunk or he runs out of shots.

## Method: 
The game is scripted to be easily adjustable. Only three variables need to be set - pond size, number of shots allowed and number of littleships. Features include randomly generated littleships, a shot tracker to prevent duplicate shots, and a validator to ensure shots are within bounds.

### Potential features to add:
  1. Larger littleships: this will require additional logic to ensure subsequent coordinates are (1) consecutive, (2) randomly horizontal or vertical, and (3) within bounds following the first random coordinate.
  2. 2-Player version: this will require (1) a second shot_tracker function that alternates with the first, and (2) a starting sequence for each player where they choose their ship locations.
  3. A visual display of shots fired: this will require generating an array with Xs and Os after each shot.

deep-die
========

Computer player for the game http://en.wikipedia.org/wiki/Shut_the_Box


Background
----------

My wife and I were evaluating this game as something to play with our daughter. The variant we were playing used the sum of the remaining numbers as the score, lower is better.

During play, she wondered whether it was better to roll 1 or 2 dice given her board. She then calculated the probability of a non-game-ending roll for 1 and 2 die. This led me to think that the game could be played well by a computer. If you can calculate your best probability of a non-game-ending roll for your current board, you could have done all the calculations for your choices in crossing off numbers, and crossed off the best choice.

This was my first stab at it. However the first few rolls, whatever choice you make in crossing off usually has a 100% probability of the next roll being non-game-ending. This led to some bad choices. I improved the code to recursively play the game for each choice, and that is what we have now.

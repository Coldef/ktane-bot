# ktane-bot
A bot to read the bomb defusal instructions for Keep Talking and Nobody Explodes.

Currently implemented solvers for modules button, keypad, maze, simon says, memory and wires. Creating word lists for who's on first and changing them so the speech to text understands them would take ages, so I got stuck on it.

The ```constants.py``` file contains the words the speech to text listens to. This is so that it is easier to modify the bot to understand different languages.

The bot is currently implemented in Finnish, here's an early succesful run with it (if you haven't played KTaNE before, some of the messages sounds nonsense, since they assume the user knows how each module works):
https://youtu.be/_ZHw28KNT7g

Original English manual for KTaNE: https://www.bombmanual.com/
Finnish manual: https://www.bombmanual.com/fi/index.html

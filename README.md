# Country Guesser 🌍

#### Video Demo: (https://youtu.be/8FEky8OT_gc)

#### Description:

Country Guesser is a command-line geography guessing game built entirely 
in Python. The game fetches real country data from the RestCountries API 
and challenges the player to identify a randomly selected country using 
only their knowledge — or a few well-chosen hints. It is fast, fun, and 
surprisingly educational.

The idea came from games like GeoGuessr and Wordle — games that are simple 
to understand but hard to master. I wanted to build something similar but 
purely in Python, as a CLI game that tests geographical knowledge while 
also being genuinely enjoyable to play.

---

## How to Play

Install dependencies first:

pip install -r requirements.txt

Then run the game:

python project.py

When the game starts, you will see a flag emoji for the country you need 
to guess. Your job is to type the correct country name. You start with 
1000 points, and your score decreases every second — so the faster you 
guess, the better your final score will be.

At any point, you can type `hint` to request additional information about 
the country. Each hint costs a different number of points, so use them 
wisely. If you want to give up, type `quit` — but be warned, quitting 
sets your final score to 0.

---

## Scoring System

The scoring system is designed to reward both speed and confidence.

- You start with 1000 points
- Every second that passes costs 10 points
- Each hint you request costs additional points
- Your final score = 1000 minus time penalty minus hint penalty
- Score can never go below 0

The formula is:

score = 1000 - (elapsed_seconds x 10) - (sum of hint costs)

This means a player who guesses correctly in 5 seconds with no hints 
will score around 950 points, while a player who takes 3 hints and 
60 seconds might score around 0. It creates a real tension between 
asking for help and preserving your score.

---

## Hints System

The flag is shown for free at the start of every round — it is your 
first and most important clue. After that, you can request up to three 
additional hints, each at a cost:

| Hint       | Cost        |
|------------|-------------|
| 🚩 Flag    | Free        |
| Population | -100 points |
| Region     | -150 points |
| Capital    | -200 points |

Each hint can only be used once per round. The game will tell you if 
you try to use the same hint twice.

---

## Project Files

### project.py

This is the main file containing the entire game logic. It has the 
following functions:

**`get_country()`**
Fetches the full list of countries from the RestCountries API and returns 
one randomly selected country as a dictionary. The dictionary contains 
the country's name, capital, region, population, and flag emoji. If the 
API request fails for any reason, the program exits with an error message 
rather than crashing silently.

**`give_hint(country, hint_type)`**
Takes the country dictionary and a hint type string as input, and returns 
the corresponding value. For example, passing "capital" returns the 
capital city, and passing "flag" returns the flag emoji. This function 
handles the case where a country has no capital listed by returning "N/A" 
instead of crashing.

**`validate_guess(guess, country)`**
Compares the player's guess to the correct country name. It is fully case 
insensitive and strips extra whitespace, so "france", "France", and 
"  FRANCE  " are all accepted as correct. Returns True if the guess is 
correct, False otherwise.

**`calculate_score(start_time, hints_used)`**
Calculates the player's current score based on how much time has passed 
since the game started and which hints have been used. It uses Python's 
`time.time()` to measure elapsed time. The score is floored at 0 and 
never goes negative.

**`main()`**
The main game loop. It fetches a country, displays the flag, starts the 
timer, and repeatedly prompts the player for input. It handles guesses, 
hint requests, and the quit command, and ends the game when the player 
guesses correctly, quits, or runs out of points.

### test_project.py

Contains three pytest test functions that test the core logic of the game 
without making any real API calls.

**`test_give_hint()`**
Tests that the hint function correctly returns capital, region, and 
population values from a mock country dictionary.

**`test_calculate_score()`**
Tests the scoring function using a simulated start time of 10 seconds ago 
with no hints, and then with one hint used. Uses `pytest.approx` to 
account for tiny timing differences.

**`test_validate_guess()`**
Tests that the validation function correctly accepts lowercase, uppercase, 
and rejects wrong guesses.

### requirements.txt

Lists the two external libraries used:
- `requests` — for making API calls to RestCountries
- `colorama` — for colored terminal output on Windows and other platforms

---

## Design Choices

One decision I thought about carefully was whether to penalize wrong 
guesses directly. In the end, I decided not to — wrong guesses are 
already punished indirectly through time. Every second you spend typing 
wrong answers is costing you 10 points. This felt more fair and more fun 
than adding a direct penalty, since it encourages players to keep trying 
rather than giving up after one wrong guess.

I also chose to make the flag free rather than a paid hint. Flags are 
visually interesting but often not enough to identify a country on their 
own — especially for smaller or less well-known nations. Giving the flag 
for free makes the game feel generous at the start while still leaving 
plenty of challenge.

Another choice was to keep this as a CLI project rather than building a 
GUI. CLI keeps the focus on Python logic, which is what CS50P is about. 
The colorama library adds enough color and personality to make the 
terminal feel alive without overcomplicating the codebase.

---

## What I Learned

Building this project taught me how to work with real external APIs, 
handle JSON data, and structure a Python program with clean, testable 
functions. Writing the pytest tests before finishing the game loop helped 
me think about edge cases early — like countries with no capital city, 
or flags with no emoji. I also got comfortable with Python's `time` 
module and learned how to build a scoring system that feels balanced 
and fair.

Most importantly, I learned that even a simple idea — guess the country 
— can become genuinely fun when the right mechanics are in place.

---

## Acknowledgements

Country data provided by the [RestCountries API](https://restcountries.com).
Built as the final project for CS50P — Introduction to Programming with Python.
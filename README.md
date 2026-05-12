# Country Guesser 🌍

#### Video Demo: https://youtu.be/8FEky8OT_gc

#### Description:

Country Guesser is a CLI geography guessing game written in Python. It pulls real country data from the RestCountries API and asks the player to identify a randomly picked country. You can rely on what you know or ask for hints — but hints cost points and so does time, so there is always a tradeoff.

I got the idea from games like GeoGuessr and Wordle. I wanted something with that same "simple to play but hard to master" feeling but built entirely in Python as a terminal game.

---

## How to Play

Install dependencies:

    pip install -r requirements.txt

Run the game:

    python project.py

When the game starts you will see the country's flag. Type your guess anytime. Type hint if you want a clue. Type quit to end the game early — but your score becomes 0 if you do.

---

## Scoring

You start with 1000 points. Every second costs 10 points. Hints cost extra on top of that. The formula is:

    score = 1000 - (seconds elapsed x 10) - (hint costs used)

Score never goes below 0. Someone who guesses in 5 seconds with no hints walks away with around 950. Someone who burns 60 seconds and takes three hints will probably end up near 0.

---

## Hints

The flag is shown for free when the round starts. After that you can ask for up to three more hints:

| Hint | Cost |
|------|------|
| Flag | Free |
| Population | -100 points |
| Region | -150 points |
| Capital | -200 points |

Each hint can only be used once. The game tells you if you try to use the same one again.

---

## Files

### project.py

This file has all the game logic.

**get_country()** calls the RestCountries API and returns one randomly picked country as a dictionary with its name, capital, region, population and flag. If the request fails the program exits with an error message instead of crashing silently.

**give_hint(country, hint_type)** takes the country data and a hint name and returns the matching value. If a country has no capital on record it returns "N/A" rather than throwing an error.

**validate_guess(guess, country)** checks whether the player's input matches the country name. It ignores case and strips extra spaces so "france" and "FRANCE" and " France " all count as correct.

**calculate_score(start_time, hints_used)** works out the current score from how much time has passed and which hints were used. It uses time.time() to track elapsed seconds and floors the result at 0.

**main()** runs the game loop. It fetches the country, shows the flag, starts the timer and keeps asking for input until the player guesses correctly, quits or runs out of points.

### test_project.py

Three pytest tests that check the core logic without touching the API.

**test_give_hint()** checks that the function returns the right values for capital, region and population from a mock country dictionary.

**test_calculate_score()** simulates a start time 10 seconds in the past and checks the score with no hints and with one hint used. It uses pytest.approx to handle small timing differences.

**test_validate_guess()** checks that lowercase, uppercase and wrong guesses all behave correctly.

### requirements.txt

Two libraries:

- requests — for the API call
- colorama — for colored output in the terminal

---

## Design Choices

I decided not to penalise wrong guesses directly. Time is already doing that job — every second of typing wrong answers drains your score. Adding a separate penalty on top of that felt more frustrating than fun. Keeping it time-based means you can keep guessing freely without being punished twice.

The flag is free because flags alone are rarely enough to identify a country. A lot of smaller or less familiar countries have flags that are easy to confuse. Giving it away at the start makes the game feel fair while still leaving the actual challenge intact.

I kept it as a CLI project because that kept the focus on Python logic. colorama handles the colors and the rest is just clean code.

---

## What I Learned

This project taught me how to work with a real API, parse JSON responses and structure code into testable functions. Writing the tests early pushed me to think about edge cases before they became bugs — things like countries with no listed capital or flags without an emoji. I also got a lot more comfortable with Python's time module than I expected.

---

## Acknowledgements

Country data from the RestCountries API. Built for CS50P — Introduction to Programming with Python by Harvard University.
Country data provided by the [RestCountries API](https://restcountries.com).
Built as the final project for CS50P — Introduction to Programming with Python.

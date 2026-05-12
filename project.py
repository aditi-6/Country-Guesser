import sys
import requests
import random
import time
from colorama import Fore, Style, init
init(autoreset=True)

HINT_COSTS = {
    "population": 100,
    "region": 150,
    "capital": 200
}

# Main Game Functions

# Fetch a random country from the API
def get_country():
    url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,flags,cca2"
    try:
        response= requests.get(url)
        response.raise_for_status()
        countries= response.json()
        return random.choice(countries)
    except requests.RequestException as e:
        print(f"Error fetching country data: {e}")
        sys.exit(1)

    

# Provide hints based on the country data and option user selected to get as a hint
def give_hint(country, hint_type):
    
    if hint_type == "capital":
        return country["capital"][0] if country["capital"] else "N/A"

    elif hint_type == "region":
        return (country["region"])
    elif hint_type == "population":
        return (country["population"])
    elif hint_type == "flag":
        return country["flags"].get("emoji", country["flags"].get("png", "🏳️"))
    


# Validate the user's guess against the correct country name
def validate_guess(guess, country):
    correct = country["name"]["common"]
    return guess.strip().lower() == correct.strip().lower()



# Calculate the score based on time taken and hints used
def calculate_score(start_time, hints_used):
    elapsed = time.time() - start_time  
    time_penalty = elapsed*10  
    hint_penalty = sum(HINT_COSTS[hint] for hint in hints_used)
    score = 1000 - (time_penalty + hint_penalty)
    return max(score, 0)         
    


# Main game loop
def main():
    print(f"{Fore.CYAN}===================================================================\n\nWelcome to Country Guesser! 🌍\n\n===================================================================")
    country = get_country()
   
    print(f"{Fore.YELLOW}🚩 Flag: {country['flags'].get('emoji') or country.get('cca2', '??')}")
    start_time = time.time()
    hint_used = []

    
    # Game continues until user guesses correctly, runs out of points, or quits
    while True:
        
        score = calculate_score(start_time, hint_used)
        print(f"{Fore.GREEN}⭐ Score: {int(score)}")
        if score == 0:
            print(f"{Fore.RED}💀 Out of points! The country was: {country['name']['common']}")
            break
        #type hint or guess the country name
        guess= input("type 'hint' for a hint \n\n Your guess : ")

        if guess.lower() == "hint":
            print(f"{Fore.MAGENTA}Available hints: population, region, capital, flag")
            hint_choice = input("Which hint would you like? ")

            #check if hint already used or valid
            if hint_choice in HINT_COSTS and hint_choice not in hint_used:
                print(f"{Fore.BLUE}Hint: {give_hint(country, hint_choice)}")
                hint_used.append(hint_choice)

            #flag hint doesn't have a cost but can only be used once    
            elif hint_choice == "flag": 
                print(f"{Fore.YELLOW}🚩 Flag: {country['flags'].get('emoji') or country.get('cca2', '??')}")   

            else:
                print("Invalid hint choice or already used.")

        #check if user wants to quit
        elif guess.lower() == "quit":    
            print(f"{Fore.RED}Game over! The country was: {country['name']['common']}")
            print(f"{Fore.RED}Final score: 0 (you quit!)")
            break

        #check if guess is correct
        elif validate_guess(guess, country): 
            score = calculate_score(start_time, hint_used)
            print(f"{Fore.GREEN}Correct! 🎉 The country was {country['name']['common']}. \nYour score: {score:.2f}\n Time: {time.time() - start_time:.2f} seconds")
            break

        #when guess is incorrect
        else:
            print(f"{Fore.RED}Incorrect guess. Try again!")

    pass


if __name__ == "__main__":
    main()

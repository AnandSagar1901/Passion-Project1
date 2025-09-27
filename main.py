from google import genai

# Just put your API key here directly
API_KEY = "AIzaSyBub6LZewuE6Sya8aprw7hNKlr3k5325FU"

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say something funny about guessing numbers"
)

print(response.text)

def get_gemini_roast(client):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Give me a short, funny roast for someone who guessed the wrong number."
    )
    return response.text

def get_gemini_compliment(client):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Give me a short, funny compliment for someone who guessed the wrong number."
    )
    return response.text

import random

from typing import Optional

# A randomly chosen secret number (keeps same value while the program runs)
num = random.randint(1, 100)

guess = int(input("Enter your guess (1-100): "))

def check_guess(num = num, guess = guess):
    if guess < num:
      print("Too low!") 
      print(get_gemini_roast(client))
    elif guess > num:
        print("Too high!")
        print(get_gemini_roast(client))
    else:  
        print("Correct! You've guessed the number.")
        print(get_gemini_compliment(client))

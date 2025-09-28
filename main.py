import random
from google import genai

API_KEY = "Enter Your API key here"
client = genai.Client(api_key=API_KEY)

def get_gemini_roast(client):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Give me one and only short, funny roast for someone who guessed the wrong number."
    )
    return response.text

def get_gemini_compliment(client):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Give me one and only one short, funny compliment for someone who guessed the right number."
    )
    return response.text

difficulty = ""

Chooser = int(input("Choose a difficulty (1 = Easy, 2 = Medium, 3 = Hard): "))
if Chooser == 1:
    num = random.randint(1, 50)
    difficulty = "1-50"
elif Chooser == 2:
    num = random.randint(1, 100)
    difficulty = "1-100"
elif Chooser == 3:
    num = random.randint(1, 500)
    difficulty = "1-500"
else:
    print("Invalid choice, defaulting to Medium (1-100).")
    num = random.randint(1, 100)
    difficulty = "1-100"


def check_guess(num):
    guess = None
    while guess != num:
        guess = int(input(f"Enter your guess ({difficulty}): "))
        if guess < num:
            print("Too low!")
            print(get_gemini_roast(client))
        elif guess > num:
            print("Too high!")
            print(get_gemini_roast(client))
    
    # When loop exits, guess == num
    print("✅ Correct! You guessed the number.")
    print(get_gemini_compliment(client))

check_guess(num)

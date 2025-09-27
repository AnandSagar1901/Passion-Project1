import random
from google import genai

API_KEY = "AIzaSyBub6LZewuE6Sya8aprw7hNKlr3k5325FU"
client = genai.Client(api_key=API_KEY)

def get_gemini_roast(client):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Give me one short, funny roast for someone who guessed the wrong number."
    )
    return response.text

def get_gemini_compliment(client):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Give me one short, funny compliment for someone who guessed the right number."
    )
    return response.text

# Generate random secret number
num = random.randint(1, 100)

def check_guess(num):
    guess = None
    while guess != num:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if guess < num:
            print("Too low!")
            print(get_gemini_roast(client))
        elif guess > num:
            print("Too high!")
            print(get_gemini_roast(client))

    # When loop exits, guess == num
    print("✅ Correct! You guessed the number.")
    print(get_gemini_compliment(client))

# Start the game
check_guess(num)



root = tk.Tk()
root.title("Guess the Number 🎲")

label = tk.Label(root, text="Guess a number between 1 and 100")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit Guess", command=play_game)
button.pack()

root.mainloop()

import random

print("🎮 Welcome to Rock, Paper, Scissor Game!")
print("----------------------------------------")

choices = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

while True:
    print("\nTumhara Score:", user_score, "| Computer ka Score:", computer_score)
    user = input("Tum kya logi? (rock / paper / scissor) ya 'exit' likho band karne ke liye: ").lower()

    if user == "exit":
        print("\nGame Khatam! Final Score - Tum:", user_score, "Computer:", computer_score)
        if user_score > computer_score:
            print("🎉 Tum Jeet Gayi! Maza aa gaya!")
        elif user_score < computer_score:
            print("😢 Computer Jeet Gaya! Fir se try karo!")
        else:
            print("🤝 Draw Ho Gaya!")
        break

    if user not in choices:
        print("Arey! Sahi likho - rock, paper ya scissor")
        continue

    computer = random.choice(choices)
    print(f"Computer ne chuna: {computer}")

    if user == computer:
        print("Draw! Dono ne same chuna")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("🎉 Tum Jeet Gayi is round me!")
        user_score += 1
    else:
        print("😢 Computer Jeet Gaya is round me!")
        computer_score += 1
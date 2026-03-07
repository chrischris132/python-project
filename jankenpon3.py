import random
import os
from time import sleep

# --- Utility for colored text (works in most terminals) ---
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

# --- File to store high scores ---
SCORE_FILE = "rps_highscore.txt"

def load_high_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            return int(file.read().strip())
    return 0

def save_high_score(score):
    with open(SCORE_FILE, "w") as file:
        file.write(str(score))

# --- Main Game ---
print(color("=== ULTIMATE ROCK PAPER SCISSORS ===", "95"))
sleep(0.5)
player_score = 0
computer_score = 0
rounds = 5
choices = ["rock", "paper", "scissors"]

# Load existing high score
high_score = load_high_score()
print(color(f"🏆 Current High Score: {high_score}", "93"))

# Difficulty selection
print("\nChoose difficulty level:")
print("1. Easy (Random computer moves)")
print("2. Hard (Computer predicts your next move)")
difficulty = input("Enter 1 or 2: ")

print(color("\nGame starting... Get ready!", "92"))
sleep(1)

# For storing previous player move (used in hard mode)
prev_move = None

for round_num in range(1, rounds + 1):
    print(color(f"\n--- ROUND {round_num} of {rounds} ---", "96"))
    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in choices:
        print(color("❌ Invalid choice, try again!", "91"))
        continue

    # Computer move logic
    if difficulty == "1":  # Easy mode
        computer = random.choice(choices)
    else:  # Hard mode - tries to counter your previous move
        if prev_move == "rock":
            computer = "paper"
        elif prev_move == "paper":
            computer = "scissors"
        elif prev_move == "scissors":
            computer = "rock"
        else:
            computer = random.choice(choices)
    prev_move = player

    sleep(0.5)
    print(color(f"🤖 Computer chose: {computer}", "94"))

    # Determine winner
    if player == computer:
        print(color("⚖️ It's a tie!", "97"))
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print(color("✅ You win this round!", "92"))
        player_score += 1
    else:
        print(color("💻 Computer wins this round!", "91"))
        computer_score += 1

    print(color(f"Score → You: {player_score} | Computer: {computer_score}", "93"))
    sleep(0.5)

# --- Final results ---
print(color("\n=== FINAL RESULTS ===", "95"))
sleep(0.5)
if player_score > computer_score:
    print(color(f"🏆 You win the match! Final Score {player_score}-{computer_score}", "92"))
    if player_score > high_score:
        print(color("🔥 NEW HIGH SCORE!", "93"))
        save_high_score(player_score)
elif player_score < computer_score:
    print(color(f"💀 Computer wins the match! Final Score {computer_score}-{player_score}", "91"))
else:
    print(color("🤝 It’s a draw overall!", "97"))

print(color("\nThanks for playing! 👋", "96"))

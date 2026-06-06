 🚀 CodeAlpha Tasks - Python Programming

Welcome to my repository! This project showcases the Python applications developed during my internship at CodeAlpha. It features interactive console games, chatbots, and financial tracking utilities.

---

## 🚀 Featured Projects

### 🤖 1. Chatbot Game (`chatbot.py`)
A smart text-based chatbot that interacts with users.
* **Core Features:**
  * Interactive conversation flow.
  * Automated responses to user queries.

#### Source Code
```python
import datetime

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ['hello', 'hi', 'hey']:
        return "Hello! I am your CodeAlpha assistant. How can I help you today?"
    elif user_input in ['how are you', 'how are you doing']:
        return "I'm doing great, thank you! Ready to help you with your tasks."
    elif user_input in ['what is your name', 'name']:
        return "I am a smart rule-based chatbot developed for my CodeAlpha internship."
    elif 'time' in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    elif 'date' in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}."
    elif user_input in ['bye', 'exit', 'quit']:
        return "Goodbye! Have a fantastic day!"
    else:
        return "I am still learning. Try asking me about the time, date, or my name!"

def main():
    print("=" * 50)
    print("🤖 Welcome to the Interactive Chatbot Game!")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("=" * 50)
    
    while True:
        user_text = input("\nYou: ")
        response = chatbot_response(user_text)
        print(f"Chatbot: {response}")
        if user_text.lower().strip() in ['bye', 'exit', 'quit']:
            break

if __name__ == "__main__":
    main()
```

---

### 🎮 2. Hangama Game (`hangama.py`)
A fun word-guessing game played against the computer.
* **Core Features:**
  * Random word selection.
  * Interactive guessing and life/attempt counter.

#### Source Code
```python
import random

def play_hangama():
    word_bank = ['python', 'programming', 'internship', 'developer', 'chatbot', 'computer']
    secret_word = random.choice(word_bank).lower()
    guessed_letters = set()
    incorrect_attempts = 0
    max_lives = 6
    
    print("=" * 50)
    print("🎮 Welcome to the Hangama Word-Guessing Game!")
    print("=" * 50)
    
    while incorrect_attempts < max_lives:
        word_display = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Attempts remaining: {max_lives - incorrect_attempts}")
        
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter exactly one letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            print(f"❌ Incorrect! '{guess}' is not in the word.")
            incorrect_attempts += 1
            
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n🎉 Congratulations! You guessed the word: '{secret_word.upper()}'!")
            return

    print(f"\n💀 Game Over! The correct word was: '{secret_word.upper()}'.")

if __name__ == "__main__":
    play_hangama()
```

---

### 📈 3. Stock Utility (`stock.py`)
A custom script designed to track and analyze stock-related data.
* **Core Features:**
  * Clean and user-friendly interface.
  * Robust logic to handle finance data.

#### Source Code
```python
import os

class Stock:
    def __init__(self, ticker, shares, purchase_price):
        self.ticker = ticker.upper().strip()
        self.shares = int(shares)
        self.purchase_price = float(purchase_price)

    def calculate_value(self, current_price):
        total_cost = self.shares * self.purchase_price
        current_value = self.shares * current_price
        profit_loss = current_value - total_cost
        return total_cost, current_value, profit_loss

class PortfolioTracker:
    def __init__(self, filename="portfolio.txt"):
        self.filename = filename
        self.portfolio = {}
        self.load_portfolio()

    def load_portfolio(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    if line.strip():
                        ticker, shares, price = line.strip().split(",")
                        self.portfolio[ticker] = Stock(ticker, shares, price)
        except Exception:
            print("⚠️ Warning: Error loading portfolio database file.")

    def save_portfolio(self):
        with open(self.filename, "w") as file:
            for stock in self.portfolio.values():
                file.write(f"{stock.ticker},{stock.shares},{stock.purchase_price}\n")

    def add_or_update_stock(self):
        print("\n--- Add / Update Position ---")
        ticker = input("Enter Stock Ticker: ").upper().strip()
        try:
            shares = int(input(f"Enter shares for {ticker}: "))
            price = float(input(f"Enter purchase price: \$"))
            self.portfolio[ticker] = Stock(ticker, shares, price)
            self.save_portfolio()
            print("✅ Portfolio database updated successfully.")
        except ValueError:
            print("❌ Error: Invalid numeric values entered.")

    def display_and_analyze(self):
        if not self.portfolio:
            print("\n📉 Your portfolio is empty.")
            return
        print("\n" + "=" * 60)
        print(f"{'TICKER':<10}{'SHARES':<10}{'BUY PRICE':<12}{'EST. NOW':<12}{'P/L':<12}")
        print("=" * 60)
        for stock in self.portfolio.values():
            current_price = stock.purchase_price * 1.05  # Mock market increase
            cost, val, pnl = stock.calculate_value(current_price)
            print(f"{stock.ticker:<10}{stock.shares:<10}\${stock.purchase_price:<11.2f}\({current_price:<11.2f}\){pnl:<11.2f}")
        print("=" * 60)

def main():
    tracker = PortfolioTracker()
    while True:
        print("\n📈 CodeAlpha Financial Stock Utility")
        print("1. View Portfolio")
        print("2. Add/Update Stock")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            tracker.display_and_analyze()
        elif choice == "2":
            tracker.add_or_update_stock()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
```

---

## 🛠️ Tech Stack & Concepts Used

* **Language:** Python 3.x
* **Core Concepts:** Object-Oriented#code Alpha tasks



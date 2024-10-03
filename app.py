from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Choices for the game
choices = ['rock', 'paper', 'scissors']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

@app.route('/')
def instructions():
    return render_template('instructions.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['user_choice']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
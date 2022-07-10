from flask import render_template, request
from app import app
from models.players_list import players
from models.player import Player
from models.games_list import games
from models.game import Game

@app.route('/')
def index():
    return render_template('index.html', title='Home', players=players, games=games)


@app.route('/<p1_choice>/<p2_choice>')
def play_game(p1_choice, p2_choice):
  
        if p1_choice == 'rock' and p2_choice == 'scissors':
          return 'Rock crashes scissors: Player1 wins.'
        elif p1_choice == 'rock' and p2_choice == 'paper':
          return 'Paper blocks rock: Player2 wins.'
        elif p1_choice == 'rock' and p2_choice == 'rock':
          return None
        elif p1_choice == 'paper' and p2_choice == 'scissors':
          return 'Scissors cut paper: Player2 wins.'
        elif p1_choice == 'paper' and p2_choice == 'paper':
          return None
        elif p1_choice == 'paper' and p2_choice == 'rock':
          return 'Paper blocks rock: Player1 wins.'
        elif p1_choice == 'scissors' and p2_choice == 'paper':
          return 'Scissors cut paper: Player1 wins.'
        elif p1_choice == 'scissors' and p2_choice == 'rock':
          return 'Rock crashes scissors: Player2 wins.'
        elif p1_choice == 'scissors' and p2_choice == 'scissors':
          return None
        else:
          return 'You entered wrong values. Please try again.'
        

@app.route('/<p1_name>/<p2_name>')
def play_by_name(p1_name, p2_name):
  for player in players:
    if p1_name == player.name:
      p1_choice = player.choice
    else:
      return 'You entered a wrong value. Please try again.'
    if p2_name == player.name:
      p2_choice = player.choice
  
    if p1_choice == 'rock' and p2_choice == 'scissors':
      return f'Rock crashes scissors: {p1_name} wins.'
    elif p1_choice == 'rock' and p2_choice == 'paper':
      return f'Paper blocks rock: {p2_name} wins.'
    elif p1_choice == 'rock' and p2_choice == 'rock':
      return None
    elif p1_choice == 'paper' and p2_choice == 'scissors':
      return f'Scissors cut paper: {p2_name} wins.'
    elif p1_choice == 'paper' and p2_choice == 'paper':
      return None
    elif p1_choice == 'paper' and p2_choice == 'rock':
      return f'Paper blocks rock: {p1_name} wins.'
    elif p1_choice == 'scissors' and p2_choice == 'paper':
      return f'Scissors cut paper: {p1_name} wins.'
    elif p1_choice == 'scissors' and p2_choice == 'rock':
      return f'Rock crashes scissors: {p2_name} wins.'
    elif p1_choice == 'scissors' and p2_choice == 'scissors':
      return None
    else:
      return 'You entered wrong values. Please try again.'
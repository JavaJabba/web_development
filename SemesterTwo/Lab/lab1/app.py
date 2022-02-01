from random import choice
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/rps/<player>")
def rps(player):
    rps = ["rock", "paper", "scissors"]
    computer = choice(rps)
    if player == "rock" and computer == "scissors":
        message = "Player Wins!"
        return render_template("rps.html", player=player, computer=computer, message=message)
    elif player == "scissors" and computer == "paper":
        message = "Player Wins!"
        return render_template("rps.html", player=player, computer=computer, message=message)
    elif player == "paper" and computer == "rock":
        message = "Player Wins!"
        return render_template("rps.html", player=player, computer=computer, message=message)
    elif computer == "rock" and player == "scissors":
        message = "Computer Wins!"
        return render_template("rps.html", player=player, computer=computer, message=message)
    elif computer == "scissors" and player == "paper":
        message = "Computer Wins!"
        return render_template("rps.html", player=player, computer=computer, message=message)
    elif computer == "paper" and player == "rock":
        message = "Computer Wins!"
        return render_template("rps.html", player=player, computer=computer, message=message)
    elif computer == player:
        message = "It's a draw"
        return render_template("rps.html", player=player, computer=computer, message=message)
    else:
        message = "It's Rock, Paper Scissors, it's not that hard!"
        return render_template("rps.html", player=player, computer=computer, message=message)



from random import choice, randint
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


@app.route("/could_it_be_me/<num_lines>")
def send_lotto_numbers(num_lines):
    line = []
    num_lines = int(num_lines)
    for num in range(1, num_lines):
        for i in range(0, 6):
            n = randint(1, 47)
            line.append(n)
    return render_template("lotto.html", line=line, num_lines=num_lines)
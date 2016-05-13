from flask import Flask
from flask import jsonify
from flask.ext.cors import CORS
import chess
import game_tools

app = Flask(__name__)
CORS(app)

game = chess.Board()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<int:i>')
def incr(i):
	return str(i + 1)

@app.route('/legal_moves')
def legal_moves_start():
	board = chess.Board()
	moves = board.legal_moves
	l = list()
	for m in moves:
		l.append(m.uci())
	d = dict(enumerate(l))
	return jsonify(d)

@app.route('/move/<m>')
def move(m):
	game.push(chess.Move.from_uci(m))
	print game
	return 'Ok'

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)

from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS
import chess
import game_tools

app = Flask(__name__)
CORS(app)

game = chess.Board()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/legal_moves')
def legal_moves_start():
	moves = game.legal_moves
	l = list()
	for m in moves:
		l.append(m.uci())
	d = dict(enumerate(l))
	d['len'] = len(l)
	return jsonify(d)

@app.route('/move/<m>',methods=['POST'])
def move(m):
	if request.method == 'POST':
		m = str(m)
		game.push(chess.Move.from_uci(m))
		print game
		return 'Ok'

@app.route('/init',methods=['POST'])
def init():
	if request.method == 'POST':
		game.reset()
		return 'ok'

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)

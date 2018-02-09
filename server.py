'''
Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

In order to generate a random number you can use the "random" python module:

import random # import the random module

# The random module has many useful functions. This is one that gives a random number in a range
random.randrange(0, 101) # random number between 0-100

In order to remove something from the session, you must "pop" it off of the session dictionary.

# Set session like so:
session['someKey'] = 50

# Remove something from session like so:
session.pop('someKey')\
'''

from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'GreatNumberGameKey'

@app.route('/')

def index():
  if not 'randomNum' in session:
    session['randomNum'] = random.randrange(0, 101)
  if not 'guess' in session:
    session['guess'] = 'none'
  if not 'color' in session:
    session['color'] = 'white'
  if not 'border' in session:
    session['border'] = 'transparent'
  if not 'count' in session:
    session['count'] = 0

  return render_template("index.html")

@app.route('/guess', methods=['POST'])

def guess():
  session['guess'] = request.form['answer']
  session['border'] = 'black'
  session['count'] += 1

  if int(session['randomNum']) > int(session['guess']):
    session['color'] = 'red'
  elif int(session['randomNum']) < int(session['guess']):
    session['color'] = 'red'
  elif int(session['randomNum']) == int(session['guess']):
    session['color'] = 'green'
  return redirect('/')


@app.route('/reset', methods=['POST'])

def reset():
  session.pop('randomNum')
  session.pop('guess')
  session.pop('color')
  session.pop('count')
  session.pop('border')

  return redirect('/')

app.run(debug=True)
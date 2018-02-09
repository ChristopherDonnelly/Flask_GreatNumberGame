from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'CounterSecretKey'

@app.route('/')

def index():
  if not 'counter' in session:
    session['counter'] = 1
  else:
    session['counter'] += 1

  return render_template("index.html")

@app.route('/countBy2', methods=['POST'])

def counter_ninja1():
  session['counter'] += 1
  return redirect('/')


@app.route('/reset', methods=['POST'])

def reset_ninja2():
  session['counter'] = 0
  return redirect('/')

app.run(debug=True)
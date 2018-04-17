from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def get_money():
    gold = 0
    if request.form['building'] == 'farm':
        session['gold'] = random.randrange(10,20)
        session['log'] = "You gained {} gold!".format(session['gold'])
        gold += gold += session['gold']
    elif request.form['building'] == 'cave':
        session['gold'] = random.randrange(5,10)
        session['log'] = "You gained {} gold!".format(session['gold'])
        gold += session['gold']
    elif request.form['building'] == 'house':
        session['gold'] = random.randrange(2,5)
        session['log'] = "You gained {} gold!".format(session['gold'])
        gold += session['gold']
    elif request.form['building'] == 'casino':
        session['gold'] = random.randrange(-50,50)
        session['log'] = "You gained {} gold!".format(session['gold'])
        gold += session['gold']
    return redirect('/')


app.run(debug=True)


from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'pinkwaterbottle'

def random_number():
	session['random'] = int(random.randrange())	
		
@app.route('/')
def index():
	if 'gold' not in session: 
		session['gold'] = 0
	if 'log' not in session:
		session['log'] = []	
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	print "Currently Processing"
	if request.form['action'] == "farm":
		session['gains'] = random.randrange(10,21)
		session['gold'] += session['gains']
		session['log'].insert(0,"You have humbly harvested crops worth: "+str(session['gains'])+" gold!"+"\n")

	if request.form['action'] == "cave":
		session['gains'] = random.randrange(5,11)
		session['gold'] += session['gains']
		session['log'].insert(0,"You have diligently mined precious jewels worth: "+str(session['gains'])+" gold!")

	if request.form['action'] == "house":
		session['gains'] = random.randrange(2,6)
		session['gold'] += session['gains']
		session['log'].insert(0,"You have guiltily raided a family home worth: "+str(session['gains'])+" gold!")

	if request.form['action'] == "casino":
		session['gains'] = (random.randrange(0, 101)-50)
		session['gold'] += session['gains']
		session['log'].insert(0,"You have tried your luck at slots and left with: "+str(session['gains'])+" gold!")
			
	return redirect('/')	

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')	



app.run(debug=True)

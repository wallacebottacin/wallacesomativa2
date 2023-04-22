from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        if any(char.isdigit() for char in name):
            return render_template('home.html', greeting='', error='Por favor, não insira números no nome!')
        else:
            hour = int(datetime.now().strftime('%H'))
            if hour < 12:
                greeting = 'Bom dia, ' + name + '!'
            elif hour < 18:
                greeting = 'Boa tarde, ' + name + '!'
            else:
                greeting = 'Boa noite, ' + name + '!'
            return render_template('home.html', greeting=greeting, error='')
    else:
        return render_template('home.html', greeting='', error='')

if __name__ == '__main__':
    app.run(debug=True)
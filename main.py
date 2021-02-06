from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(SECRET_KEY='bardzosekretnawartosc',
                       ))

# lista pytań
DANE = [{
    'pytanie': 'Stolica Hiszpanii to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Hiszpania', 'Barcelona'],  # odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedz
    {
    'pytanie': 'Symbol pierwiastka Żelazo, to:',
    'odpowiedzi': ['Ze', 'Fe', 'St'],
    'odpok': 'Fe'},
    {
    'pytanie': 'Objętość sześcianu o boku 5cm wynosi:',
    'odpowiedzi': ['25cm', '125cm', '15cm'],
    'odpok': '125cm'},
]

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('index'))

    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)

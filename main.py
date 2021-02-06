from flask import Flask
from flask import render_template

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
    'odpok': 'Fe' },
    {
    'pytanie': 'Objętość sześcianu o boku 5 wynosi:',
    'odpowiedzi': ['25', '125', '15'],
    'odpok': '125cm'},
]

@app.route('/')
def index():
    return render_template('index.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from data.card import all_cards

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template(
        'custom_card.html',
        all_cards = all_cards
    )


if __name__ == '__main__':
    print(all_cards)
    app.run(debug=True)


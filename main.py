from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'POST':
        quote = get_quote()
    return render_template('index.html', quote=quote)

def get_quote():
    url = 'https://api.quotable.io/random'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

if __name__ == '__main__':
    app.run(debug=True)
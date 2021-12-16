from flask import Flask, render_template
import json
import requests
# from urllib.request import urlopen

app = Flask(__name__)


@app.route('/')
def main():
    poke_api = 'https://pokeapi.co/api/v2/pokemon'
    response_api = requests.get(poke_api)
    api_data = json.loads(response_api.text)

    with open('pokemons.json', 'w') as f:  # upload data to json
        json.dump(api_data, f, indent=2)

    # with open('pokemons.json', 'w') as s:
        pokemons = api_data["results"]
        i = 1
        for poke in pokemons:
            poke["id"] = i
            i += 1

        update_poke = json.loads('pokemons.json')
        update_poke.update(pokemons)
        json.dumps(update_poke)

    return render_template('pokemons_main.html', pokemons=pokemons)


if __name__ == '__main__':
    app.run(debug=True)

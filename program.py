from flask import Flask, jsonify
from Controllers.ProgramController import ProgramController
from Models.Country import Country
from Models.Mapper import mapper
import requests, json


def api_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("bad request")


def create_momdel(country_name):
    countries_data = api_call("https://coronavirus-data.azurewebsites.net/api/countries")
    population_data = api_call("https://restcountries.eu/rest/v2/all")
    try:
        mapp_name = mapper[country_name]
    except KeyError:
        mapp_name = country_name
    for record in population_data:
        if record["name"] == mapp_name:
            model_population = record["population"]
    for record in countries_data:
        if record["country"] == country_name:
            model_name = record["country"]
            model_cases = record["cases"]
    return Country(model_name, model_cases, model_population)


app = Flask(__name__)


@app.route('/')
def hello_world():
    country = create_momdel("Italy")
    return jsonify(ProgramController().show_data(country))


if __name__ == "__main__":
    app.run()

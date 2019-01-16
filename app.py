from flask import Flask
from flask import request
from flask import render_template

import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get('https://swapi.co/api/planets/')
    data = response.json()
    planets = data['results']

    # We will replace all of this mess...
    # planet_html = []
    #
    # for planet in planets:
    #     planet_html.append('<li>{} :: {}</li>'.format(planet['name'], planet['climate']))
    #
    # planet_html = ''.join(planet_html)
    #
    # # Get html and render to screen
    # index_file = open('templates/index.html', 'r')
    # index_html = index_file.read()
    # index_html = index_html.replace('{{planet_list}}', planet_html)
    # index_file.close()
    #
    # return index_html

    # With this:
    return render_template('2.2-SK8.html', planet_list=planets)


@app.route('/book-now/', methods=['GET', 'POST'])
def book_now():
    # Book now is configured to accept POST requests, so we can access the form data as a dictionary:
    print(request.form['1-tickets'])
    return 'Booking your trip!'



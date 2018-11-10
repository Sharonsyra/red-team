from flask import Flask, jsonify
from google import google
from urllib.parse import urlparse


import os
import re

app = Flask(__name__)
# app.secret_key = os.getenv('SECRET')


@app.route('/')
def google_search():
    results = []
    num_page = 1
    search_results = google.search("Michuki Law", num_page)
    print(search_results)
    for result in search_results:
        parsed_uri = urlparse(result.link)
        result_given = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        domain = result_given.split('.')[1]
        results.append({domain:result.link})
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

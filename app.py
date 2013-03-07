from flask import (Flask, request, url_for, jsonify)
import os
import json
import urllib
import urllib2

app = Flask(__name__)

def make_api_query(term, course):
    base_url = 'http://data.adicu.com/courses?'
    params = urllib.urlencode({
        'api_token': app.DATA_ADICU_COM_API_KEY,
            'term': term,
            'course': course
        }
    )

    url = base_url + params
    print url

    results = json.loads(urllib2.urlopen(url).read())
    return results
    

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/courses.json')
def courses():
    results = make_api_query('spring2013', 'MATHV1202')
    return jsonify(results)

if __name__ == '__main__':
    #app.debug = True

    app.DATA_ADICU_COM_API_KEY = os.environ.get('DATA_ADICU_COM_API_KEY')

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    url_for('static', filename='css/default.css')
    url_for('static', filename='css/normalize.css')
    url_for('static', filename='css/normalize.min.css')

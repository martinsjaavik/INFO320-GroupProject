from flask import Flask, render_template, request
import requests, json, urllib.parse
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Query
@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']

    # POST request to SPARQL endpoint
    endpoint = 'http://localhost:8080/sparql'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(endpoint, data={'query': query}, headers=headers)

    if response.status_code != 200:
        return render_template('index.html', response_table='<p>Error</p>')

    response = response.json()

    # Data to make table with
    if 'results' in response and 'bindings' in response['results']:
        bindings = response['results']['bindings']
        if bindings:
            field_names = list(bindings[0].keys())
        else:
            field_names = []

        table_data = []

        for binding in bindings:
            row = [binding[field_name]['value'] if field_name in binding else '' for field_name in field_names]
            table_data.append(row)

        response_table = build_table(field_names, table_data)

    return render_template('index.html', response_table=response_table)

def build_table(field_names, data):
    table_html = '<table border="1"><tr>'
    for field_name in field_names:
        table_html += '<th>{}</th>'.format(field_name)
    table_html += '</tr>'

    for row in data:
        table_html += '<tr>'
        for value in row:
            if value.startswith('http'):
                # Removes URL, only retains name
                decoded_value = urllib.parse.unquote(value)
                display_value = decoded_value.rsplit('/', 1)[-1]
            else:
                display_value = value 

            table_html += '<td>{}</td>'.format(display_value)
        table_html += '</tr>'
    
    table_html += '</table>'
    return table_html

if __name__ == '__main__':
    app.run(debug=True)

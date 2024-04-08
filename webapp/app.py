from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Route to render the HTML page with the form
@app.route('/')
def index():
    return render_template('index.html', response_table=None)

# Route to handle the form submission
@app.route('/query', methods=['POST'])
def query():
    # Get the SPARQL query from the form
    sparql_query = request.form['query']

    # Make a POST request to the SPARQL endpoint
    endpoint_url = 'http://localhost:8080/sparql'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(endpoint_url, data={'query': sparql_query}, headers=headers)

    # Parse the JSON response
    response_json = response.json()

    # Extract the data from the response for the table
    if 'results' in response_json and 'bindings' in response_json['results']:
        bindings = response_json['results']['bindings']
        if bindings:
            # Get all unique keys (field names) from the first binding
            field_names = list(bindings[0].keys())
        else:
            field_names = []

        table_data = []

        for binding in bindings:
            row = [binding[field_name]['value'] if field_name in binding else '' for field_name in field_names]
            table_data.append(row)

        response_table = build_table(field_names, table_data)
    else:
        response_table = '<p>No data found</p>'

    # Render the HTML page with the response table
    return render_template('index.html', response_table=response_table)

def build_table(field_names, data):
    table_html = '<table border="1"><tr>'
    for field_name in field_names:
        table_html += '<th>{}</th>'.format(field_name)
    table_html += '</tr>'

    for row in data:
        table_html += '<tr>'
        for value in row:
            table_html += '<td>{}</td>'.format(value)
        table_html += '</tr>'
    
    table_html += '</table>'
    return table_html

if __name__ == '__main__':
    app.run(debug=True)

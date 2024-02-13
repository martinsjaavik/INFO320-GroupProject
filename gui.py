import tkinter as tk
from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import SPARQLResult

# Connect to the Ontop SPARQL endpoint
sparql_endpoint = "http://localhost:8080/sparql"

# Define namespaces
ns = Namespace("http://example.org/ontology#")
dbo = Namespace("http://dbpedia.org/ontology/")

def query_vkg(parameter):
    # Example SPARQL query to retrieve data based on user input
    query = f"""
        PREFIX ns: <http://example.org/ontology#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        SELECT ?result
        WHERE {{
            ?s ns:hasParameter "{parameter}" ;
               ns:hasResult ?result .
        }}
    """

    # Execute the SPARQL query
    g = Graph()
    results = g.query(sparql_endpoint, query)

    # Process and return results
    query_results = [str(row[0]) for row in results]
    return query_results

def on_submit():
    parameter = entry.get()
    results = query_vkg(parameter)
    result_text.set("\n".join(results))

# Create the main application window
root = tk.Tk()
root.title("VKG Interaction GUI")

# Create and place widgets
label = tk.Label(root, text="Enter Parameter:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=400, justify="left")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

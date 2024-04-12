from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
import customtkinter
import sys 
import os
sys.path.append(os.path.abspath("j.py"))
from j import *
import tkinter as tk
from CTkTable import *


# Load your ontology file into a RDFLib Graph
g = Graph()
g.parse("endpoint/input/ontology-materialized.ttl", format="ttl")  # Replace with the actual path to your ontology file and format

# Define your SPARQL query
query = """
    PREFIX ex: <http://example.org/ontology/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX obda: <https://w3id.org/obda/vocabulary#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <http://schema.org/>



SELECT ?country ?o WHERE {
        ?country ex:ObesityRate ?o.
    }
LIMIT 10
    """ # Adjust your query as per your ontology structure

# Execute the SPARQL query
results = g.query(query)

# Execute the query and initialize row and column counts
row_count = 0
column_count = 0

# Process the results
for row in results:
    print(str(row[0]).split("/")[-1])
    print(str(row[1]))
    row_count += 1
    column_count = max(column_count, len(row))

# Close the graph
g.close()

root = customtkinter.CTk()
new_window = customtkinter.CTkToplevel(fg_color="white")
new_window.title("This is a new window!")
new_window.geometry("600x400")
new_window.resizable(False, True) # Width, Height
#new_window.attributes('-topmost', True)
        


value = [["Africa",2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5]]
table = CTkTable(master=new_window, row=row_count, column=column_count, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)
main2()
new_window.update()


root.mainloop()

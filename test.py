from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

# Load your ontology file into a RDFLib Graph
g = Graph()
g.parse("ontology-materialized.ttl", format="ttl")  # Replace with the actual path to your ontology file and format

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
ORDER BY DESC(?o)
LIMIT 50
    """ # Adjust your query as per your ontology structure

# Execute the SPARQL query
results = g.query(query)

# Process the results
for row in results:
    print(str(row[0]).split("/")[-1])
    print(str(row[1]).split("/")[-1])

# Close the graph
g.close()
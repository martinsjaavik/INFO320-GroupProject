from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

# Load your ontology file into a RDFLib Graph
g = Graph()
g.parse("ontology-materialized.ttl", format="ttl")  # Replace with the actual path to your ontology file and format

# Define your SPARQL query
query = prepareQuery(
    """
    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object
    }
    LIMIT 1
    """,
    initNs={})  # Adjust your query as per your ontology structure

# Execute the SPARQL query
results = g.query(query)

# Process the results
for row in results:
    print(str(row[0]).split("/")[-1])
    print(str(row[1]).split("/")[-1])
    print(str(row[2]).split("/")[-1])

# Close the graph
g.close()
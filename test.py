from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF, XSD, DC, RDFS
from rdflib.collection import Collection
from SPARQLWrapper import SPARQLWrapper, JSON, TURTLE, GET, POST

def test():
        g = Graph()
        g.parse("ontology.ttl")
        q = g.query("""
SELECT DISTINCT ?s ?p ?o WHERE {
?s ?p ?o .
}

""")
        print(list(q))
test()
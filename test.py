from rdflib import Graph, Namespace, URIRef, BNode, Literal


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
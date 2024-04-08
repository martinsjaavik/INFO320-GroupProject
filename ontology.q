[QueryItem="All triples"]
PREFIX ex: <http://example.org/ontology/>
SELECT ?s ?p ?o WHERE
{
	?s ?p ?o .
}

[QueryItem="Obesity rate"]
PREFIX ex: <http://example.org/ontology/>
SELECT ?country ?o WHERE {
        ?country ex:ObesityRate ?o.
    }
ORDER BY DESC(?o)
LIMIT 50

[QueryItem="Has Capital"]
PREFIX ex: <http://example.org/ontology/>
SELECT ?country ?capital WHERE {
        ?country ex:hasCapital ?capital.
    }
ORDER BY ASC(?country)
LIMIT 50
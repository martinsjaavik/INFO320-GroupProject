[QueryItem="All triples"]
SELECT ?s ?p ?o WHERE
{
	?s ?p ?o .
}
[QueryItem="Obesity rate"]
PREFIX ex: <http://example.org/ontology/>

PREFIX schema: <http://schema.org/>

SELECT ?country ?o WHERE {
        ?country ex:ObesityRate ?o.
    }
ORDER BY DESC(?o)
LIMIT 50
[QueryItem="Life expectancy"]
PREFIX ex: <http://example.org/ontology/>

PREFIX schema: <http://schema.org/>

SELECT ?country ?LifeExpectancy WHERE {
        ?country ex:belongsToContinent ex:Europe;
		ex:hasLifeExpectancy ?LifeExpectancy.
    }
ORDER BY ASC(?country)
LIMIT 50
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
[QueryItem="Region with highest life expectancy"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?region ?country ?lifeExpectancy
WHERE {
  ?region rdf:type ex:Region .
  ?country ex:belongsToRegion ?region .
  ?country ex:hasLifeExpectancy ?lifeExpectancy .
}
ORDER BY DESC(?lifeExpectancy)
LIMIT 10
[QueryItem="Higher male obesity rate"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?country ?maleObesityRate ?femaleObesityRate
WHERE {
  ?country rdf:type ex:Country .
  ?country ex:MaleObesityRate ?maleObesityRate .
  ?country ex:FemaleObesityRate ?femaleObesityRate .
  FILTER (?maleObesityRate > ?femaleObesityRate)
}
[QueryItem="Higher female obesity rate"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?country ?femaleObesityRate ?maleObesityRate
WHERE {
  ?country rdf:type ex:Country .
  ?country ex:FemaleObesityRate ?femaleObesityRate .
  ?country ex:MaleObesityRate ?maleObesityRate .
  FILTER (?femaleObesityRate > ?maleObesityRate)
}
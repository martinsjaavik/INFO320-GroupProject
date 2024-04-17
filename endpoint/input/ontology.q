[QueryItem="All triples"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?s ?p ?o
WHERE {
    ?s ?p ?o .
}

LIMIT 10
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
[QueryItem="Corrolation between happiness and obesity"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?country ?happinessScore ?obesityRate
WHERE {
  ?country ?p ex:Country .
  ?country ?p ?countryName .
  
  OPTIONAL { ?country ex:hasHappinessScore ?happinessScore }
  
  OPTIONAL { ?country ex:ObesityRate ?obesityRate }
  
  FILTER (bound(?happinessScore))
  FILTER (bound(?obesityRate))
}
ORDER BY DESC(?happinessScore)
[QueryItem="Average happines score by region"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?region (AVG(?happinessScore) AS ?avgHappiness)
WHERE {
  ?country rdf:type ex:Country .
  ?country ex:hasHappinessScore ?happinessScore .
  ?country ex:belongsToRegion ?region .
  ?region rdf:type ex:Region .
}
GROUP BY ?region
ORDER BY DESC(?avgHappiness)
[QueryItem="European countries"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?s WHERE {
?s ?p ex:OceaniaCountry
}
[QueryItem="Democracies"]
PREFIX ex: <http://example.org/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?country ?government WHERE {
  ?country rdf:type ex:Country .
  ?country ex:hasGovernment ?government .
  ?government rdf:type ex:Democracy .
}
[QueryItem="Dictatorships"]
PREFIX ex: <http://example.org/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?country ?government WHERE {
  ?country rdf:type ex:Country .
  ?country ex:hasGovernment ?government .
  ?government rdf:type ex:Dictatorship .
}
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

SELECT ?country
WHERE {
  ?country rdf:type ex:Country .
  ?country a ex:Dictatorship .
}
[QueryItem="Dictatorships"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?country ?gov WHERE {
  ?country rdf:type ex:Country .
  ?country a ex:Dictatorship .
}
[QueryItem="Continents"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?country ?continent WHERE {
  ?country rdf:type ex:Country .
  ?country ex:belongsToContinent ?continent .
  ?continent rdf:type ex:Europe .
}
[QueryItem="Compare Norway and Sweden"]
PREFIX ex: <http://example.org/ontology/>

SELECT ?country ?capital ?obesity ?happiness
WHERE {
  {
    ex:Norway ex:hasCapital ?capital ;
              ex:hasHappinessScore ?happiness ;
              ex:ObesityRate ?obesity .
    BIND("Norway" as ?country)
  }
  UNION
  {
    ex:Sweden ex:hasCapital ?capital ;
              ex:hasHappinessScore ?happiness ;
              ex:ObesityRate ?obesity .
    BIND("Sweden" as ?country)
  }
}
# SPARQL Queries

## Introduction

SPARQL (SPARQL Protocol and RDF Query Language) is a standardized query language used for querying and manipulating data stored in RDF (Resource Description Framework) format. RDF is a flexible and extensible data model for representing information in the form of subject-predicate-object triples. In this lesson, we will explore the basics of SPARQL queries and how they can be used to retrieve specific information from RDF datasets.

## SPARQL Query Basics

SPARQL queries consist of several essential components:

1. **PREFIX**: The PREFIX keyword is used to define namespace prefixes that are used throughout the query to shorten URIs. It provides a way to associate a short prefix with a full URI.

2. **SELECT**: The SELECT keyword is used to specify the variables that should be returned in the query results. These variables can represent specific data elements or properties from the RDF dataset.

3. **WHERE**: The WHERE keyword is used to specify the patterns or conditions that must be satisfied by the RDF data in order to retrieve the desired information. It allows you to specify the subject-predicate-object triples or patterns that should match the data.

4. **FILTER**: The FILTER keyword is used to further refine the query results based on specified conditions. It allows you to include or exclude data based on certain criteria, such as comparing values or checking for specific patterns.

## Example SPARQL Queries

### Query 1: Find x Number of People

```sparql
PREFIX schema: <http://schema.org/>
SELECT ?person ?name
WHERE {
  ?person a schema:Person ;
          schema:name ?name .
}
LIMIT %x
```

This query retrieves people and their names from the RDF dataset using the schema:Person class. The ?person variable represents the subject, and schema:name represents the predicate. Replace '%x' with the amount of people you want to search for.

### Query 2: Find Specific Person by Name

```sparql
PREFIX schema: <http://schema.org/>
SELECT ?s ?p ?o
WHERE {
  ?s ?p ?o ;
     a schema:Person ;
     schema:name "%s" .
}

```

This query retrieves information about a specific person by their name. Replace '%s' with the name of the person you want to find.

### Query 3: Find x Number of Works

```sparql
PREFIX schema: <http://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?work ?title
WHERE {
  ?work a schema:MusicComposition ;
        rdfs:label ?title .
}
LIMIT %s
```

This query retrieves music compositions and their titles from the RDF dataset using the schema:MusicComposition class. Replace '%s' with the amount of works you want to search for.

### Query 4: Find Works by String in the Title (Case-Sensitive)

```sparql
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX schema: <http://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?work ?composer ?title
WHERE {
  ?work a <http://schema.org/MusicComposition> ;
        dcterms:creator ?composer ;
        rdfs:label ?title .
  FILTER regex(?title, "%s", "i")
}
LIMIT %i
```

Here, we start to combine different search queries. We FILTER for a specific piece, '%s', and LIMIT to get '%i' number of '%s' pieces. 
This query retrieves music compositions with titles containing the specified string (case-insensitive). Replace '%s' with the string you want to search for, and %l with the number of pieces you want to retrieve.

## Conclusion
SPARQL queries provide a powerful and standardized way to retrieve specific information from RDF datasets. By combining the PREFIX, SELECT, WHERE, and FILTER keywords, you can construct queries that suit your specific data retrieval needs. Understanding the basics of SPARQL queries is essential for working with RDF data and leveraging its full potential.

Note: The examples above are for illustrative purposes and may need to be modified to match the specific RDF dataset and vocabulary being used.



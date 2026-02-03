import streamlit as st
import requests
import json
import urllib.parse
from datetime import date, timedelta, time, datetime

def render_sparql_query(query):
    encoded_query_url = get_encoded_url(query)
    html_link = f'<a href="{encoded_query_url}" target="_blank">Encoded Query</a>'
    st.components.v1.html(html_link, height=30)

def get_encoded_url(query):
    base_url = "https://data.carnegiehall.org/sparql/"
    encoded_query = urllib.parse.quote(query)
    encoded_query_url = f"{base_url}?query={encoded_query}"
    return encoded_query_url


# Define content for each page
def query_generator():
    st.title("Carnegie Hall Data Lab SPARQL Query Generator")

    query_options = {
        "Find people": """
            PREFIX schema: <http://schema.org/>
            SELECT ?person ?name WHERE {
                ?person a schema:Person ;
                schema:name ?name .
            }
            LIMIT %s""",
        "Find a specific person by name": """
            PREFIX schema: <http://schema.org/>
            select ?s ?p ?o where {
                ?s ?p ?o ;
                a schema:Person ;
                schema:name "%s" .
            }""",
        "Find works": """
            PREFIX schema: <http://schema.org/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            select ?work ?title where {
                ?work a schema:MusicComposition ;
                    rdfs:label ?title .
            }
            LIMIT %s"""
			,
		"Find works by string in the title (case-insensitive)": """
			PREFIX dcterms: <http://purl.org/dc/terms/>
			PREFIX schema: <http://schema.org/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			select distinct ?work ?composer ?title where {
			?work a <http://schema.org/MusicComposition> ;
				dcterms:creator ?creator ;
				rdfs:label ?title .
			?creator schema:name ?composer
				filter regex(?title, "%s")
			}
			LIMIT %l """,

        "Find performances of a specific work": """
            PREFIX schema: <http://schema.org/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

            SELECT ?performanceID ?date ?performerID ?name ?work ?title
            WHERE {
            ?performanceID schema:subEvent ?workPerformance ;
                            schema:startDate ?date .
            ?workPerformance schema:workPerformed ?work .

            ?work a schema:MusicComposition ;
                    rdfs:label ?title .
            FILTER (CONTAINS(?title, "%s"))


            ?workPerformance mo:performer ?performerID .
            ?performerID schema:name ?name .
            }
            LIMIT %l
        """,

        "Find performances on a specific day": """
            PREFIX schema: <http://schema.org/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

            SELECT ?performanceID ?date ?performerID ?name ?work ?title
            WHERE {
            ?performanceID schema:subEvent ?workPerformance ;
                            schema:startDate ?date .
            ?workPerformance schema:workPerformed ?work .

            ?work a schema:MusicComposition ;
                    rdfs:label ?title .
            FILTER (CONTAINS(?title, "%s"))
            FILTER (?date >= "%d"^^xsd:dateTime && ?date < "%a"^^xsd:dateTime)
            ?workPerformance mo:performer ?performerID .
            ?performerID schema:name ?name .
            }
            LIMIT %l
        """,

        "Find performances within a specific date range": """
            PREFIX schema: <http://schema.org/>
            PREFIX mo: <http://purl.org/ontology/mo/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

            SELECT ?performanceID ?date ?performerID ?name ?work ?title
            WHERE {
            ?performanceID schema:subEvent ?workPerformance ;
                            schema:startDate ?date .
            ?workPerformance schema:workPerformed ?work .

            ?work a schema:MusicComposition ;
                    rdfs:label ?title .

            FILTER (?date >= "%d"^^xsd:dateTime && ?date < "%a"^^xsd:dateTime)
            ?workPerformance mo:performer ?performerID .
            ?performerID schema:name ?name .
            }
            LIMIT %l
        """

    }

    selected_option = st.selectbox("Select an option", list(query_options.keys()))

    if selected_option in ("Find people", "Find works"):
        query_template = query_options[selected_option]
        search_term = st.text_input(f"Enter number of {selected_option.split()[1]} to find:")
        if search_term:
            query = query_template % search_term
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)

    elif selected_option == "Find a specific person by name":
        query_template = query_options[selected_option]
        search_term = st.text_input("Enter search term:")
        if search_term:
            query = query_template % search_term
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)

    elif selected_option == "Find works by string in the title (case-insensitive)":
        query_template = query_options[selected_option]
        search_term = st.text_input("Enter title:")
        limit_box = st.checkbox("Limit Results")
        if limit_box:
            limit_term = st.text_input("Enter number of pieces:")
        if search_term and limit_box and limit_term:
            query = query_template.replace("%s", search_term).replace("%l", limit_term)
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)
        if search_term and not limit_box:
            query = query_template.replace("%s", search_term).replace("LIMIT %l", '')
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)

    elif selected_option == "Find performances of a specific work":
        query_template = query_options[selected_option]
        search_term = st.text_input("Enter title:")
        limit_box = st.checkbox("Limit Results")
        if limit_box:
            limit_term = st.text_input("Enter number of pieces:")
        if search_term and limit_box and limit_term:
            query = query_template.replace("%s", search_term).replace("%l", limit_term)
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)
        if search_term and not limit_box:
            query = query_template.replace("%s", search_term).replace("LIMIT %l", '')
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)

    elif selected_option == "Find performances on a specific day":
        query_template = query_options[selected_option]
        search_term = st.text_input("Enter title:")
        limit_box = st.checkbox("Limit Results")
        if limit_box:
            limit_term = st.text_input("Enter number of pieces:")
        today = date.today()
        min_date = today - timedelta(days=365 * 123)  # Set the minimum date to 100 years ago
        max_date = today + timedelta(days=365 * 0) 
        date_sel = st.date_input("Select date:",min_value=min_date, max_value=max_date)
    # Convert the selected date to xsd:dateTime format
        xsd_date = datetime.strptime(str(date_sel), "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00")
    # Calculate the day after the selected date
        day_after_xsd_date = (datetime.strptime(xsd_date, "%Y-%m-%dT%H:%M:%S") + timedelta(days=1)).strftime("%Y-%m-%dT00:00:00")
        if (search_term or date_sel) and limit_box and limit_term:
            if not search_term:
                search_term = "''"
            query = query_template.replace("%s", search_term).replace("%l", limit_term).replace("%d", xsd_date).replace("%a", day_after_xsd_date)
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)
        if (search_term or date_sel) and not limit_box:
            if not search_term:
                search_term = "''"
            query = query_template.replace("%s", search_term).replace("LIMIT %l", '').replace("%d", xsd_date).replace("%a", day_after_xsd_date)
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)


    if selected_option == "Find performances within a specific date range":
        query_template = query_options[selected_option]
        limit_box = st.checkbox("Limit Results")
        if limit_box:
            limit_term = st.text_input("Enter number of pieces:")
        today = date.today()
        min_date = today - timedelta(days=365 * 123)  # Set the minimum date to 100 years ago
        max_date = today + timedelta(days=365 * 0) 
        date_sel_min = st.date_input("Select Min date:",min_value=min_date, max_value=max_date)
        date_sel_max = st.date_input("Select Max date:",min_value=min_date, max_value=max_date)
    # Convert the selected date to xsd:dateTime format
        xsd_date_min = datetime.strptime(str(date_sel_min), "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00")
        xsd_date_max = datetime.strptime(str(date_sel_max), "%Y-%m-%d").strftime("%Y-%m-%dT23:59:59")

        if date_sel_min and date_sel_max and limit_box and limit_term:
            query = query_template.replace("%l", limit_term).replace("%d", xsd_date_min).replace("%a", xsd_date_max)
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)
        if date_sel_min and date_sel_max and not limit_box:
            query = query_template.replace("LIMIT %l", '').replace("%d", xsd_date_min).replace("%a", xsd_date_max)
            st.subheader("Generated SPARQL Query:")
            st.code(query)
            render_sparql_query(query)


def sparql_queries():
    url = "https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/dev_Edgar/SPARQL.md"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        st.markdown(content)
    else:
        st.error(f"Error loading content from {url}. Status code: {response.status_code}")

# Create sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to:", ( "SPARQL Queries","Query Generator"))

# Page routing
if page == "Query Generator":
    query_generator()
else:
    sparql_queries()
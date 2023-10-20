# import neomodel
from neo4j import GraphDatabase

def execute_query(host:str, user: str, password: str, query, params={}):
    # Returns a tuple of records, summary, keys
    with GraphDatabase.driver(host, auth=(user, password)) as driver:
        records, summary, keys =  driver.execute_query(query, params)
        # Only interested in list of result records
        return records

def reset(host:str, user: str, password:str):
    # Clears nodes and relationships - but labels remain and can only be cleared via GUI
    query = """
    MATCH (n)
    REMOVE n
    """
    execute_query(host, user, password, query, params = {})

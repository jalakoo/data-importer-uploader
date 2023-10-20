
import io
from data_importer_uploader.n4j import execute_query, reset

def upload_csv(
        csv: str, 
        json: str,
        neo4j_creds : (str, str,str),
        reset_before_upload: bool = True
        ) -> bool:
    """
    Uploads a .csv file using a .json mapping file.

    Args:
        csv: Stringified .csv with data to upload
        json: Stringified .json mapping file
        neo4j_creds: A tuple of (host, user, password) for the Neo4j instance to upload to.
        reset_before_upload: Boolean flag to reset the Neo4j instance before uploading.
    
    Returns:
        True if the upload was successful, False otherwise
    """


    raise NotImplementedError

def upload(
        zip: io.BytesIO,
        neo4_creds: (str, str, str),
        reset_before_upload: bool = True
        ) -> bool:
    """
    Uploads a zip file of .csvs and a .json file compatible with Neo4j's Data-Importer

    Args:
        zip: An io.BytesIO representation of the source .zip file
        neo4j_creds: A tuple of (host, user, password) for the Neo4j instance to upload to.
        reset_before_upload: Boolean flag to reset the Neo4j instance before uploading.
    
    Returns:
        True if the upload was successful, False otherwise
    """

    # TODO: Load .zip file
    # TODO: Extract .json file (should only be one)
    # TODO: Verify .json format
    # TODO: Extract .csv files
    # TODO: Verify data integrity

    # TODO: Reset Neo4j if requested
    if reset_before_upload:
        reset(*neo4_creds)
        
    # TODO: Run load to upload each .csv file

    # TODO: Smoke test that the data was uploaded?

    raise NotImplementedError
from elasticsearch import Elasticsearch


def create_connection():
    """
    Creates a connection to elastic search object.
    :return:
    """
    config = {
        'host': '0.0.0.0'
    }

    try:
        es = Elasticsearch([config, ], timeout=300)
        return es
    except:
        print("Error creating es object check if docker is running...")

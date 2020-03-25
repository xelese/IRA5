from Scripts.connection.connection import create_connection
from data.variables import get_index_name


def token_extraction(es, query, index_name):
    """
    parses query to produce tokens.
    :param es: elastic search object.
    :param query: query string.
    :param index_name: name of the index to form token from.
    :return: list of relevant tokens.
    """
    # parse the query to get token data.
    query = query.split()

    # json to parse the words of the query.
    request = {
        "field": "content",
        "text": query,
    }

    # tokens for each query
    tokens = es.indices.analyze(index=index_name, body=request)
    all_terms = []
    for token in tokens["tokens"]:
        term = token["token"]
        all_terms.append(term)

    return all_terms


def get_relevant_docs(query):
    """
    get the relevant documents from es given by query in web app.
    :param query: query string.
    :return: list of relevant documents.
    """
    # create a connection to elastic search object.
    es = create_connection()

    # get name of index from elastic main py file.
    index_name = get_index_name()

    # create tokens for each query
    tokens = token_extraction(es, query, index_name)

    # generate a list of documents from the dictionary.
    list_documents = []
    result = es.search(index="hw3_dataset", size=100, body={'query': {'match': {'content': ' '.join(tokens)}}})
    for item in result["hits"]["hits"]:
        list_documents.append(item["_source"]["url"])

    return list_documents

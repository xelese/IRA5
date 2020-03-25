from flask import Flask, render_template
from flask import request

from Scripts.data_processing.query_processing import get_relevant_docs
from data.variables import get_index_name

app = Flask(__name__)


@app.route("/")
def home():
    """
    This is the homepage of the flask web page. Allows you to search for links.
    :return: render on an html.
    """
    return render_template("index.html")


@app.route("/search_query")
def search():
    """
    searches for data using internal elastic search scoring and produces a list of links.
    :return: render the results on the html page. If no query is given then it reloads the home page.
    """
    # get query from web page.
    query = request.args['query']

    # if nothing is provided just reload the page.
    if query is "":
        return render_template("index.html")

        # keep the name of the index consistent.
    index_name = get_index_name()

    # get the list of relevant docs.
    list_documents = get_relevant_docs(query)

    # render the list of docs on html.
    return render_template("index.html", content=list_documents)


# @app.route("/get_grade")
# def grade_links():
#     """
#     gets grade from the form in html from the radio button.
#     :return: list of grades.
#     """
#     # get query from web page.
#     list_grade = request.args['grade']
#
#     print(list_grade)


if __name__ == "__main__":
    app.run(debug=True)

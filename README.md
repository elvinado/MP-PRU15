# Analysis of PRU-15

## Table of Contents

- [About](#about)
- [Notebook 1](#notebook-1)
- [Notebook 2](#notebook-2)

## About <a name = "about"></a>

The primary objective of this project is to show methods of handling messy real-world data. The domain of interest for this project is the results of Malaysian 15th General Election (PRU-15). 

## Notebook 1: Scraping the winners names from news article <a name = "notebook-1"></a>

Web scraping is an essential skill for a data professional. An understanding of the data and its context are imperative in order to extract “correct” information. Without domain knowledge, we may pass the wrong and misleading information to the next analyst. They might use it to build whatever narrative based on their agenda. However, our task is to collect the most accurate data. Here, I present the method to extract election results from a news website article.

- [Jupyter Notebook](MPs_pru15_names.ipynb)
- [Medium Article](https://medium.com/@elvinado/web-scraping-election-results-of-pru-15-ge-15-using-python-e9310129bf9e)

### Prerequisites

1. Python
2. Jupyter Notebook
3. Pandas
4. Selenium
5. Matplotlib

## Notebook 2: Visualisation of MPs' Relationship Based on Mentions in News <a name = "notebook-2"></a>

A visualisation of MPs' relationships based on mentions in news articles could take the form of a network diagram, showing each MP as a node and lines connecting them representing mentions of one MP in an article about another. This would allow users to see which MPs have strong connections and which are more isolated. Overall, the visualisation would provide a useful way to understand the relationships between MPs based on news coverage.

- [Jupyter Notebook](MPs_news_relationships.ipynb)
- [Medium Artickle](https://medium.com/@elvinado/visualisation-of-mps-relationship-based-on-mentions-in-news-using-python-ee62abbbd851)

### Prerequisites

1. Python
2. Jupyter Notebook
3. Pandas
4. Requests
5. Newspaper3K
6. SpaCy
7. Scikit-Learn
8. Numpy
9. NetworkX
10. PyVis
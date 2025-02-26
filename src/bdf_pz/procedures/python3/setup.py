import palimpzest as pz
import pandas as pd
import time
import os
import IPython

# formatter = IPython.get_ipython().display_formatter.formatters['text/plain']
# formatter.max_seq_length = 0

# set OPENAI_API_KEY environment variable based on OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = "{{ OPENAI_API_KEY }}" 

# Represents a scientific research paper, which in practice is usually from a PDF file
scientific_paper_schema = [
    {"name": "paper_title", "type": str, "desc": "The title of the paper. This is a natural language title, not a number or letter."},
    {"name": "author", "type": str, "desc": "The name of the first author of the paper"},
    {"name": "abstract", "type": str, "desc": "A short description of the paper contributions and findings"},
]

reference_schema = [
    {"name": "index", "type": int, "desc": "The index of the reference in the paper."},
    {"name": "title", "type": str, "desc": "The title of the paper being cited."},
    {"name": "first_author", "type": str, "desc": "The author of the paper being cited."},
    {"name": "year", "type": int, "desc": "The year in which the cited paper was published."},
]

DATA_PATH = "testdata/"
# print("Setup complete")

registered_datasets = {}
for name in os.listdir(DATA_PATH):
    registered_datasets[name] = os.path.join(DATA_PATH, name)

existing_schemas = {"ScientificPaper":scientific_paper_schema,
                    "Reference":reference_schema}
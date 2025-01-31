import palimpzest as pz
from palimpzest.core import PDFFile
import pandas as pd
import time
import os
import IPython

formatter = IPython.get_ipython().display_formatter.formatters['text/plain']
formatter.max_seq_length = 0

# set OPENAI_API_KEY environment variable based on OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = "{{ OPENAI_API_KEY }}"

class ScientificPaper(pz.core.PDFFile):
   """Represents a scientific research paper, which in practice is usually from a PDF file"""
   paper_title = pz.core.Field(desc="The title of the paper. This is a natural language title, not a number or letter.")
   author = pz.core.Field(desc="The name of the first author of the paper")
   abstract = pz.core.Field(desc="A short description of the paper contributions and findings")

class Reference(pz.core.Schema):
    """ Represents a reference to another paper, which is cited in a scientific paper"""
    index = pz.core.Field(desc="The index of the reference in the paper")
    title = pz.core.Field(desc="The title of the paper being cited")
    first_author = pz.core.Field(desc="The author of the paper being cited")
    year = pz.core.Field(desc="The year in which the cited paper was published")

import IPython
formatter = IPython.get_ipython().display_formatter.formatters['text/plain']
formatter.max_seq_length = 0

from palimpzest.core import File, Number, TextFile, RawJSONObject, PDFFile, ImageFile, EquationImage, PlotImage, URL, Download, WebPage, XLSFile, Table

existing_schemas = {
    "File": File,
    "Number": Number,
    "TextFile": TextFile,
    "RawJSONObject": RawJSONObject,
    "PDFFile": PDFFile,
    "ImageFile": ImageFile,
    "EquationImage": EquationImage,
    "PlotImage": PlotImage,
    "URL": URL,
    "Download": Download,
    "WebPage": WebPage,
    "XLSFile": XLSFile,
    "Table": Table,
    "ScientificPaper": ScientificPaper,
    "Reference": Reference
}

print("Setup complete")

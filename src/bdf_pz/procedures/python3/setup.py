import palimpzest as pz
import pandas as pd
import time
import os
import IPython

# formatter = IPython.get_ipython().display_formatter.formatters['text/plain']
# formatter.max_seq_length = 0

# set OPENAI_API_KEY environment variable based on OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = "{{ OPENAI_API_KEY }}" 

class ScientificPaper(pz.PDFFile):
   """Represents a scientific research paper, which in practice is usually from a PDF file"""
   paper_title = pz.Field(desc="The title of the paper. This is a natural language title, not a number or letter.", required=True)
   author = pz.Field(desc="The name of the first author of the paper", required=True)
   abstract = pz.Field(desc="A short description of the paper contributions and findings", required=False)

class Reference(pz.Schema):
    """ Represents a reference to another paper, which is cited in a scientific paper"""
    index = pz.Field(desc="The index of the reference in the paper", required=True)
    title = pz.Field(desc="The title of the paper being cited", required=True)
    first_author = pz.Field(desc="The author of the paper being cited", required=True)
    year = pz.Field(desc="The year in which the cited paper was published", required=True)

from palimpzest.corelib.schemas import File, Number, TextFile, RawJSONObject, PDFFile, ImageFile, EquationImage, PlotImage, URL, Download, WebPage, XLSFile, Table

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

def custom_repr(self):
    class_name = self.__class__.__name__
    class_info = [f"{class_name}: {self.__doc__}"]
    for name, field in self.field_names():
        if isinstance(field, pz.Field):
            class_info.append(f"{name}: description='{field.desc}', required={field.required}")
    return "\n".join(class_info)

# Add the custom __repr__ method to the class attributes
# attributes["__repr__"] = custom_repr
print("Setup complete")
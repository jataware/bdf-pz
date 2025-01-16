import palimpzest as pz
import pandas as pd
import time
import os
from palimpzest.corelib.schemas import File, Number, TextFile, RawJSONObject, PDFFile, ImageFile, EquationImage, PlotImage, URL, Download, WebPage, XLSFile, Table


# set OPENAI_API_KEY environment variable based on OPENAI_API_KEY

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

# Define a class name
class_name = "Author"

# Create the class dynamically
attributes = {"__doc__": " Schema for extracting author information from documents."}

# Custom __repr__ to output detailed information about the class and its fields
def custom_repr(self):
    class_info = [f"{class_name}: {self.__doc__}"]
    for name, field in self.__class__.__dict__.items():
        if isinstance(field, pz.Field):
            class_info.append(f"{name}: description='{field.desc}', required={field.required}")
    return "\n".join(class_info)

# Add the custom __repr__ method to the class attributes
attributes["__repr__"] = custom_repr

for name, desc, required in zip(['name', 'affiliation', 'email'], ['The full name of the author.', 'The affiliation of the author.', 'The email address of the author.'], [True, False, False]):
    attributes[name] = pz.Field(desc=desc, required=required)

# Create the class dynamically using type()
new_class = type(class_name, (pz.Schema,), attributes)

# Assign the dynamically created class to a variable using globals()
globals()[class_name] = new_class
existing_schemas[class_name] = new_class

try:
    schema = existing_schemas["PDFFile"]
except KeyError:
    raise ValueError(f"Schema not found in existing schemas!")


dataset = pz.Dataset(source="bdf-demo", schema=schema)
# condition = "The paper is about brain cancer."
# dataset = dataset.filter(condition)
convert_schema = Author
cardinality_str = "one_to_many"
cardinality = pz.Cardinality.ONE_TO_MANY if cardinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE
dataset = dataset.convert(convert_schema, desc=Author.__doc__, cardinality=cardinality)

if "dataset" not in locals():
    output = "bdf-demo"
else:
    output = dataset
print("Output dataset:")
print(dataset)

print(output.schema.field_names())

policy_method =  "min_cost"
engine = pz.NoSentinelPipelinedSingleThreadExecution

# Select a policy
if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()
else:
    raise ValueError(f"Unknown policy: {policy_method}")

records, execution_stats = pz.Execute(output,
                        policy = policy,
                        nocache=True,
                        allow_code_synth= False,
                        allow_token_reduction = False,
                        execution_engine=engine)

results = []
statistics = []

print("Iterating over the results:")
print(len(records))

print(output.schema.field_names())

for record in records:
    print("Record:")
    data_obj = {}
    for name in output.schema.field_names():
        print(f"Getting attribute: {name}")
        data_obj[name] = record.__getattr__(name)
    data_obj['source'] = record.filename
    results.append(data_obj)
    # results.append(record.as_dict())

results_df = pd.DataFrame(results)
print(results_df)
import palimpzest as pz
import pandas as pd
import time
import os
import IPython



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


import pandas as pd
from prettytable import PrettyTable

ds = pz.DataDirectory().listRegisteredDatasets()

# construct table for printing
table = [["Name", "Type", "Path"]]
for path, descriptor in ds:
    table.append([path, descriptor[0], descriptor[1]])

# print table of registered datasets
t = PrettyTable(table[0])
t.add_rows(table[1:])
import os
files = os.listdir("/home/gerardo/bdf-pz/testdata/bdf-demo")

files
if "dataset" not in locals():
    print("Setting dataset")
    dataset = pz.Dataset("bdf-demo", schema=ScientificPaper)
condition = "The paper is published after 2021"

dataset = dataset.filter(condition)

dataset
# Define a class name
class_name = "AuthorAffiliationSchema"

# Create the class dynamically
attributes = {"__doc__": " Schema to extract authors and their affiliations from scientific papers."}

# Custom __repr__ to output detailed information about the class and its fields
def custom_repr(self):
    class_info = [f"{class_name}: {self.__doc__}"]
    for name, field in self.__class__.__dict__.items():
        if isinstance(field, pz.Field):
            class_info.append(f"{name}: description='{field.desc}', required={field.required}")
    return "\n".join(class_info)

# Add the custom __repr__ method to the class attributes
attributes["__repr__"] = custom_repr

for name, desc, required in zip(['author_name', 'affiliation'], ['Name of the author', 'Affiliation of the author'], [True, True]):
    attributes[name] = pz.Field(desc=desc, required=required)

# Create the class dynamically using type()
new_class = type(class_name, (pz.Schema,), attributes)

# Assign the dynamically created class to a variable using globals()
globals()[class_name] = new_class

new_class
if "dataset" not in locals():
    dataset = pz.Dataset("bdf-demo", schema=ScientificPaper)
convert_schema = AuthorAffiliationSchema

caridinality_str = "one_to_many"

cardinality = pz.Cardinality.ONE_TO_MANY if caridinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE

dataset = dataset.convert(convert_schema, desc=AuthorAffiliationSchema.__doc__, cardinality=cardinality)

dataset
if "dataset" not in locals():
    output = "bdf-demo"
else:
    output = dataset

policy_method = "min_cost"

# optimization block
engine = pz.StreamingSequentialExecution
if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()
iterable  =  pz.Execute(output,
                        policy = policy,
                        nocache=True,
                        allow_code_synth=False,
                        allow_token_reduction=False,
                        execution_engine=engine)

results = []
statistics = []

for idx, (extraction, plan, stats) in enumerate(iterable):

    record_time = time.time()
    statistics.append(stats)

    for ex in extraction:
        ex_obj = {}
        for name in output.schema.fieldNames():
            ex_obj[name] = ex.__getattribute__(name)
        print(ex_obj)
        results.append(ex_obj)

results_df = pd.DataFrame(results)
print(results_df)
# context: frozendict.frozendict({'type': 'tool', 'name': 'filter_data'})
# Unable to parse result.

if "dataset" not in locals():
    print("Setting dataset")
    dataset = pz.Dataset("bdf-demo", schema=ScientificPaper)
condition = "The paper is published from 2019 onwards"

dataset = dataset.filter(condition)

dataset
if "dataset" not in locals():
    dataset = pz.Dataset("bdf-demo", schema=ScientificPaper)
convert_schema = AuthorAffiliationSchema

caridinality_str = "one_to_many"

cardinality = pz.Cardinality.ONE_TO_MANY if caridinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE

dataset = dataset.convert(convert_schema, desc=AuthorAffiliationSchema.__doc__, cardinality=cardinality)

dataset
# Error: KeyError 'PDFFile.b434331434.contents'

if "dataset" not in locals():
    output = "bdf-demo"
else:
    output = dataset

policy_method = "min_cost"

# optimization block
engine = pz.StreamingSequentialExecution
if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()
iterable  =  pz.Execute(output,
                        policy = policy,
                        nocache=True,
                        allow_code_synth=False,
                        allow_token_reduction=False,
                        execution_engine=engine)

results = []
statistics = []

for idx, (extraction, plan, stats) in enumerate(iterable):

    record_time = time.time()
    statistics.append(stats)

    for ex in extraction:
        ex_obj = {}
        for name in output.schema.fieldNames():
            ex_obj[name] = ex.__getattribute__(name)
        print(ex_obj)
        results.append(ex_obj)

results_df = pd.DataFrame(results)
print(results_df)

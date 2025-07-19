import palimpzest as pz
import pandas as pd
import time
import os
import IPython


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

# Define a class name
# Custom __repr__ to output detailed information about the class and its fields
schema = []
schema_name = "GeneDisease"
for idx, field_name in enumerate(['gene_name', 'disease_name']):
    desc = ['The name of the gene.', 'The name of the disease related to the gene.'][idx]
    field = {"name":field_name, "desc":desc, "type":eval(['str', 'str'][idx])}
    schema.append(field)

existing_schemas[schema_name] = schema
dataset_path = registered_datasets["bdf-usecase3-tiny"]
dataset = pz.Dataset(source=dataset_path)

convert_schema = existing_schemas["GeneDisease"]

cardinality_str = "one_to_many"

cardinality = pz.Cardinality.ONE_TO_MANY if cardinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE

dataset = dataset.sem_add_columns(convert_schema, cardinality=cardinality)

if "dataset" not in locals():
    output = "<palimpzest.sets.Dataset object at 0x7d5ea9497110>"
else:
    output = dataset

policy_method = "max_quality"

if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MinCost()
    # policy = pz.MaxQuality()

config = pz.QueryProcessorConfig(
    policy=policy,
    cache=False,
    verbose=False,
    allow_code_synth=False,
)

results = output.run(config)

results_df = results.to_df()
print(results_df)


# import palimpzest as pz
# dataset = pz.Dataset("testdata/bdf-usecase3-tiny")

# # condition = "The paper is about brain cancer."
# # dataset = dataset.sem_filter(condition)

# gene_mutations = [{'name': 'gene_name',
#   'desc': 'The name of the gene mentioned in the text.',
#   'type': str},
#  {'name': 'disease_name',
#   'desc': 'The name of the disease associated with the gene.',
#   'type': str},
#  {'name': 'context_info',
#   'desc': 'Additional context information regarding the gene and disease.',
#   'type': str}]

# convert_schema = gene_mutations
# cardinality = pz.Cardinality.ONE_TO_MANY
# cardinality = pz.Cardinality.ONE_TO_ONE
# dataset = dataset.sem_add_columns(convert_schema, cardinality=cardinality)

# output = dataset
# policy = pz.MinCost()
# # policy = pz.MaxQuality()

# config = pz.QueryProcessorConfig(
#     policy=policy,
#     cache=False,
#     execution_strategy="parallel",
# )

# results = output.run(config)
# results_df = results.to_df()
# print(results_df)
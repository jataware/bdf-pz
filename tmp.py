import palimpzest as pz
import pandas as pd
import time
import os
import IPython


sci_paper_cols = [
    {"name": "title", "type": str, "desc": "The title of the paper. This is a natural language title, not a number or letter."},
    {"name": "author", "type": str, "desc": "The name of the first author of the paper"},
    {"name": "abstract", "type": str, "desc": "A short description of the paper contributions and findings"},
]

reference_cols = [
    {"name": "index", "type": int, "desc": "The index of the reference in the paper"},
    {"name": "title", "type": str, "desc": "The title of the paper being cited"},
    {"name": "first_author", "type": str, "desc": "The author of the paper being cited"},
    {"name": "year", "type": int, "desc": "The year in which the cited paper was published"},
]

print("Setup complete")

schema_dicts = []
for name, desc in zip(['name', 'affiliation', 'email'], ['The full name of the author.', 'The affiliation of the author.', 'The email address of the author.']):
    schema_dicts.append({"name":name, "type":str, "desc":desc})

import palimpzest as pz
# try:
    # schema = existing_schemas["Author"]
# except KeyError:
    # raise ValueError(f"Schema 'Author' not found in existing schemas!")
dataset = pz.Dataset("testdata/bdf-demo")
condition = "The paper is about brain cancer."
dataset = dataset.sem_filter(condition)
convert_schema = schema_dicts
cardinality_str = "one_to_many"
cardinality = pz.Cardinality.ONE_TO_MANY if cardinality_str == "one_to_many" else pz.Cardinality.ONE_TO_ONE
dataset = dataset.sem_add_columns(convert_schema, cardinality=cardinality)

if "dataset" not in locals():
    output = "bdf-demo"
else:
    output = dataset

policy_method = "min_cost"

# optimization block
if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()

config = pz.QueryProcessorConfig(
    policy=policy,
    nocache=True,
    verbose=False,
    processing_strategy="streaming",
    execution_strategy="sequential",
    optimizer_strategy="pareto",
    allow_token_reduction=False,
    allow_code_synth=False,
)

iterable = output.run(config)

statistics = []
results = []
for data_record_collection in iterable:
    table = data_record_collection.data_records
    stats = data_record_collection.plan_stats
    record_time = time.time()
    statistics.append(stats)
    results.extend(table)

results_df = pd.DataFrame(results)
if "dataset" not in locals():
    output = "{{ output_dataset }}"
else:
    output = dataset

policy_method = "{{ policy_method }}"

# optimization block
engine = pz.StreamingSequentialExecution
if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()
iterable  =  pz.Execute(output,
                        policy = policy,
                        nocache=True,
                        allow_code_synth={{ allow_code_synth }},
                        allow_token_reduction={{ allow_token_reduction }},
                        execution_engine=engine)

results = []
statistics = []

for idx, (record, plan, stats) in enumerate(iterable):
    
    record_time = time.time()
    statistics.append(stats)

    for dr in record:
        data_obj = {}
        for name in output.schema.field_names():
            data_obj[name] = dr.__getattr__(name)
        data_obj['source'] = dr.filename
        results.append(data_obj)

results_df = pd.DataFrame(results)
results_df
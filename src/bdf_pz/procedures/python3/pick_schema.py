# Define a class name
schema_name = "{{ schema_name }}"
if schema_name in existing_schemas:
    schema = existing_schemas[schema_name]
else:
    schema = None
schema

# SPDX-FileCopyrightText: 2024-present Brandon Rose <rose.brandon.m@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import TYPE_CHECKING, Dict, Tuple, List
import pandas as pd

from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool
from beaker_kernel.lib import BeakerAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel

import json

JSON_OUTPUT = False

class BdfPzAgent(BeakerAgent):
    """
    You are a helpful agent that is intended to assist users in using Palimpzest, a 
    declarative system for optimizing AI workloads.

    """

    async def auto_context(self):
        return f"""You are an assistent that is intended to assist users in using Palimpzest.
        Try to identify all of the steps needed, and all of the tools. Assume the user wants to do all of the steps at once.
        
        If the user asks to extract something from a set of documents, you can use palimpzeest to do this. First, generate a schema for the extraction. Then, if necessary filter the data to only include the relevant documents. Next, convert the dataset to the schema that was generated. Finally, execute the workload to extract the information from the dataset.
        """

    @tool()
    async def register_dataset(self, path: str, name: str, agent: AgentRef) -> str:
        """
        This function registers a dataset with Palimpzest. It takes a path to a file or directory
        and a name for the dataset. The dataset will be registered and made available for use in
        subsequent operations.

        Args:
            path (str): The path to the file or directory to register as a dataset.
            name (str): The name to give to the registered dataset. If not explicitly set, the name of the file or directory will be used.

        Returns:
            str: A message indicating the result of the registration process.
        """

        code = agent.context.get_code("register_dataset", {"path": path, "name": name})
        response = await agent.context.evaluate(code)
        return response["return"]

    @tool()
    async def list_datasets(self, agent: AgentRef) -> str:
        """
        This function lists all available datasets in the system. You should use these results to nicely format the output for the user.

        Returns:
            str: A table of the datasets in the system.
        """

        code = agent.context.get_code("list_datasets", {})

        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output



    @tool()
    async def retrieve_dataset(self,
                            agent: AgentRef) -> list[str]:
        """
        This function lists the available papers in the system. The papers are also considered a dataset. The function prints which scientific papers are available for the user to use.

        Returns:
            list[str]: a list of the names of the datasets available to the user.
        """

        code = agent.context.get_code("retrieve_dataset",{},)

        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output    

        return ""    

    @tool()
    async def generate_extraction_schema(self, schema_name: str, 
                                         schema_description: str, 
                                         field_names: list, 
                                         field_descriptions: list,
                                         field_required: list,
                                         agent: AgentRef) -> str:
        """
        This function takes in a set of fields to be used to generate an extraction schema. This should be used when the user is interested in generating a new type of extraction schema. For example, let's say the user is interested
        in extracting parameter values from a set of scientific papers. The user can define the fields of the schema to be used for the extraction.
        In this case the schema name might be `Parameter` and the field information is passed in via three lists which must 
        be constructed in proper order. For example, for parameter extractions the fields may be `name`, `value`, `unit`, `source`, etc.
        You should provide a description for each field as well as whether the field is required or not in the same order as you provide the field names. Field names should not have spaces or special characters, but can have underscores.

        Args:
            schema_name (str): the name of the schema to add
            schema_description (str): a description of the schema
            field_names (list): a list of field names
            field_descriptions (list): a list of field descriptions
            field_required (list): a list of whether the field is required or not

        Returns:
            str: the name of the new schema that was created
        """

        code = agent.context.get_code(
            "create_schema",
            {
                "schema_name": schema_name,
                "schema_description": schema_description,
                "field_names": field_names,
                "field_descriptions": field_descriptions,
                "field_required": field_required,
            },
        )

        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output    
    
    @tool()
    async def filter_data(self,
                              input_dataset:str,
                              filter_expression:str,
                              agent: AgentRef,
                              loop: LoopControllerRef) -> str:
        """
        This function generates a filtered dataset given an input dataset and a filtering expression. The filter expression is a string that describes a condition that has to be satisfied for each of the data item in the dataset. For example if a user is interested in a dataset of scientific papers and wants to only keep papers that are published in the year 2022, the filter expression might be "The papers is published in 2022".

        Args:
            input_dataset (str): The input Dataset to use for the filtering.
            filter_expression (str): A string that describes a condition in natural language that can be used to filter out data points within a collection. 

        Returns:
            str: returns a new dataset corresponding to the filtered input dataset.
        """
        
        
        code = agent.context.get_code(
            "filter_data",
            {
                "input_dataset": input_dataset,
                "filter_expression": filter_expression,
            },
        )
        loop.set_state(loop.STOP_SUCCESS)


        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output    
    @tool 
    async def convert_dataset(self,
                           input_dataset:str,
                           schema:str,
                           cardinality:str,
                           agent: AgentRef,
                           loop: LoopControllerRef) -> str:
        """
        This function converts an input dataset to a new output dataset with a different schema.
        The function can be used for example to extract information from a collection of input documents.
        The function is typically needed to apply a generated schema to an existing dataset, before executing a workload.
        If multiple objects of the new schema can be extracted from a single object of the input dataset, the cardinality should be set to "one_to_many". If only one object of the new schema can be extracted from a single object of the input dataset, the cardinality should be set to "one_to_one".        
        For example if a user wants to extract the titles for a dataset of scientific papers, the schema might be a TitleSchema.
        

        Args:
            input_dataset (str): An existing object of type dataset to use for conversion.
            schema (str): A schema with a name and a set of attributes that describes the object of the new converted dataset.
            cardinality (str): The cardinality of the conversion. Either "one_to_one" or "one_to_many".

        Returns:
            str: returns a new dataset corresponding to the converted input dataset.

        """

        code = agent.context.get_code(
            "convert_dataset",
            {
                "input_dataset": input_dataset,
                "schema": schema,
                "cardinality": cardinality,
            },
        )

        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output    

    @tool()
    async def set_input_source(self,
                               agent: AgentRef) -> str:
        """
        This function sets the input dataset for the agent to work with when using Palimpzest (pz). 
        The input source, also known as the source dataset, or the input dataset, is any dataset that the user will run any workload on.

    
        Returns:
            str: returns the input source dataset as a palimpzest dataset called `dataset`.
        """
        
        code = agent.context.get_code(
        "set_input_source", {})
        
        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output    


    @tool()
    async def execute_workload(self,
                                output_dataset: str,
                                policy_method: str, 
                                allow_code_synth: str,
                                allow_token_reduction: str,
                                agent: AgentRef,
                                loop: LoopControllerRef) -> str:
        """
        This function executes a workload starting from a given output dataset.
        If necessary, before executing the workload, any input dataset must be processed to match the schema of the output dataset.
        Processing an input dataset can be composed of several operations such as filtering or converting from one schema to the next. For example, if I want to extract the title of papers with at least 5 authors, I can first filter the papers to only include those with more than 5 authors and then convert the scientific papers to a schema that only includes the title information.
        In this case, the input dataset is the scientific papers dataset and the output dataset would be obtained first with filtering and then with converting the dataset to a schema that only includes the title information.

        The policy method chosen is either to minimize the extraction cost or to maximize the quality 
        of the extraction. 
        The allow_code_synth and allow_token_reduction are flags that allow the system to use optimization strategies, repsectively to run on synthesized code and to reduce the tokens used when calling LLMs.
        This returns the extractions as a Pandas DataFrame.

        Args:
            output_dataset (str): An output dataset on which to run the workload.
            policy_method (str): Either "min_cost" or "max_quality". Defaults to "min_cost".
            allow_code_synth (str): Whether to allow code synthesis or not. Defaults to "False".
            allow_token_reduction (str): Whether to allow token reduction or not. Defaults to "False".

        Returns:
            str: returns the extracted references as a Pandas DataFrame called `results_df`.

        You should show the user the result after this function runs.

        """

        code = agent.context.get_code(
            "execute_workload",
            {
                "output_dataset": output_dataset,
                "policy_method": policy_method,
                "allow_code_synth": allow_code_synth,
                "allow_token_reduction": allow_token_reduction,
            },
        )
        loop.set_state(loop.STOP_SUCCESS)

        
        if JSON_OUTPUT:
            return json.dumps(
                {
                    "action": "code_cell",
                    "language": "python3",
                    "content": code.strip(),
                }
            )
        else:
            result = await agent.context.evaluate(
                code,
                parent_header={},
            )
            print(code)
            output = result.get("return")

            return output    
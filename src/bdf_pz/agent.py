# SPDX-FileCopyrightText: 2024-present Brandon Rose <rose.brandon.m@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import TYPE_CHECKING, Dict, Tuple

from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool
from beaker_kernel.lib import BeakerAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel

import json

class BdfPzAgent(BeakerAgent):
    """
    You are a helpful agent that is intended to assist users in using Palimpzest, a 
    declarative system for optimizing AI workloads.

    """

    @tool()
    async def extract_references(self, policy_method: str, agent: AgentRef) -> str:
        """
        This function extracts references from a set of pre-loaded scientific papers. The policy method chosen is either to minimize 
        the extraction cost or to maximize the quality of the extraction. This returns the extractions as a Pandas DataFrame.

        Args:
            policy_method (str): Either "min_cost" or "max_quality". Defaults to "min_cost".

        Returns:
            str: returns the extracted references as a Pandas DataFrame called `references_df`.

        You should show the user the result after this function runs.
        """

        code = agent.context.get_code(
            "extract_references",
            {
                "policy_method": policy_method,
            },
        )
        result = await agent.context.evaluate(
            code,
            parent_header={},
        )

        extracted_references = result.get("return")

        return extracted_references
    
    @tool()
    async def generate_extraction_schema(self, schema_name: str, 
                                         schema_description: str, 
                                         field_names: list[str], 
                                         field_descriptions: list[str],
                                         field_required: list[bool],
                                         agent: AgentRef) -> str:
        """
        This function takes in a set of fields to be used to generate an extraction schema. This should be used
        when the user is interested in generating a new type of extraction schema. For example, let's say the user is interested
        in extracting parameter values from a set of scientific papers. The user can define the fields of the schema to be used for the extraction.
        In this case the schema name might be `Parameter` and the field information is passed in via three lists which must 
        be constructed in proper order. For example, for parameter extractions the fields may be `name`, `value`, `unit`, `source`, etc.
        You should provide a description for each field as well as whether the field is required or not in the same order
        as you provide the field names. Field names should not have spaces or special characters, but can have underscores.

        Args:
            schema_name (str): the name of the schema to add
            schema_description (str): a description of the schema
            field_names (list[str]): a list of field names
            field_descriptions (list[str]): a list of field descriptions
            field_required (list[bool]): a list of whether the field is required or not

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
        result = await agent.context.evaluate(
            code,
            parent_header={},
        )

        extracted_references = result.get("return")

        return extracted_references    

    @tool()
    async def extract_schema(self, policy_method: str, schema: str, 
                             agent: AgentRef,
                             loop: LoopControllerRef) -> str:
        """
        This function performs extractions from a set of pre-loaded scientific papers for the given schema. 
        The policy method chosen is either to minimize the extraction cost or to maximize the quality 
        of the extraction. This returns the extractions as a Pandas DataFrame.

        Args:
            policy_method (str): Either "min_cost" or "max_quality". Defaults to "min_cost".
            schema (str): The schema to use for the extraction.

        Returns:
            str: returns the extracted references as a Pandas DataFrame called `results_df`.

        You should show the user the result after this function runs.
        """

        code = agent.context.get_code(
            "extract_schema",
            {
                "policy_method": policy_method,
                "schema": schema,
            },
        )
        # loop.set_state(loop.STOP_SUCCESS)
        # return json.dumps(
        #     {
        #         "action": "code_cell",
        #         "language": "python3",
        #         "content": code.strip(),
        #     }
        # )
        result = await agent.context.evaluate(
            code,
            parent_header={},
        )

        extracted_references = result.get("return")

        return extracted_references
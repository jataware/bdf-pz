# SPDX-FileCopyrightText: 2024-present Brandon Rose <rose.brandon.m@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import TYPE_CHECKING

from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool
from beaker_kernel.lib import BeakerAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel


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


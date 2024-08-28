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
    async def magic_eight_ball(self, question: str) -> str:
        """
        This is an example tool that is provided to help users understand how tools work in Beaker. It should only be
        used when a user explicitly asks for it.

        This simulates a Magic 8 ball toy where a person asks questions and gets answers indicating yes/no/maybe.

        If the tool returns the value "rephrase", the agent should use the ask_user tool to rephrase the question and
        then rerun this tool with the new question.

        Args:
            question (str): The question the user would like to have answered. The question must be answerable as
                            yes/no/maybe. If the question is not a yes/no/maybe question then inform the user, using the
                            ask_user tool for them reword the question so that it is a proper question before proceding.
        Returns:
            str: A string that is either the response the magic eight ball returned or the token "rephrase".
        """
        import random
        choices = [
            "rephrase",
            "Signs point to yes!",
            "Doesn't look good...",
            "My sources say no.",
            "I asked Siri and she said it's a secret.",
            f"How on earth do can you think that '{question.strip()}' is an appropriate question to ask me!?!?",
            "Yes, duh!",
            "No way, Jose!",
        ]
        if question.startswith("sudo"):
            return "Your wish is granted!"
        return random.choice(choices)

        # TOOD: Procedure called by agent


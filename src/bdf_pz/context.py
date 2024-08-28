# SPDX-FileCopyrightText: 2024-present Brandon Rose <rose.brandon.m@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import Dict, Any, TYPE_CHECKING
import os

from beaker_kernel.lib import BeakerContext
from beaker_kernel.lib.utils import action

from .agent import BdfPzAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel


class BdfPzContext(BeakerContext):
    """
    Biomedical Data Fabric Palimpzest Context Class
    """

    compatible_subkernels = ["python3"]
    SLUG = "bdf-pz"

    def __init__(self, beaker_kernel: "BeakerKernel", config: Dict[str, Any]):
        super().__init__(beaker_kernel, BdfPzAgent, config)

    async def setup(self, context_info=None, parent_header=None):
        command = "\n".join(
            [
            self.get_code("setup", {"openai_key": os.environ.get("OPENAI_API_KEY")}),
            ]
        )
        await self.execute(command)

    async def auto_context(self):
            return f"""
            You are an assistant helping biomedical researchers users the Palimpzest library to extract references from scientific papers.
            """.strip()


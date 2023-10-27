# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Wrapper around AI21 APIs."""


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra, root_validator
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

class LLM_Wrapper(LLM):

    base_llm: LLM

    @property
    def _llm_type(self) -> str:
        return self.base_llm._llm_type()

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        """Call out to AI21's complete endpoint.

        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python

                response = ai21("Tell me a joke.")
        """
        # call the overriden method
        return self.base_llm._call(prompt, stop, run_manager).strip()

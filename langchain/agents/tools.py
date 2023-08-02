"""Interface for tools."""
from typing import Optional

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools.base import BaseTool, Tool, tool


class InvalidTool(BaseTool):
    """Tool that is run when invalid tool name is encountered by agent."""

    name = "invalid_tool"
    """Name of the tool."""
    description = "Called when tool name is invalid."
    """Description of the tool."""

    def _run(
        self, tool_name: str, run_manager: Optional[CallbackManagerForToolRun] = None, **kwargs
    ) -> str:
        """Use the tool."""
        if kwargs["language"] == "zh":
            return f"\"{tool_name}\" 不是一个有效的工具，请尝试其他工具。"
        else:
            return f"{tool_name} is not a valid tool, try another one."

    async def _arun(
        self,
        tool_name: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
        **kwargs,
    ) -> str:
        """Use the tool asynchronously."""
        if kwargs["language"] == "zh":
            return f"\"{tool_name}\" 不是一个有效的工具，请尝试其他工具。"
        else:
            return f"{tool_name} is not a valid tool, try another one."


__all__ = ["InvalidTool", "BaseTool", "tool", "Tool"]

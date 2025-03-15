# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolCallResponse", "Result", "ResultUnionMember0", "ResultUnionMember1", "ResultUnionMember1Error"]


class ResultUnionMember0(BaseModel):
    call_id: Optional[str] = None
    """The unique identifier (e.g.

    UUID) for this tool call. If an ID is not provided by the client, the server
    will generate one.
    """

    duration: Optional[float] = None
    """The runtime duration of the tool call, in milliseconds"""

    success: Optional[Literal[True]] = None

    value: Union[Dict[str, object], List[object], str, float, bool, None] = None
    """The value returned from the tool."""


class ResultUnionMember1Error(BaseModel):
    message: str
    """An error message that can be shown to the user or the AI model."""

    additional_prompt_content: Optional[str] = None
    """Additional content to be included in the retry prompt."""

    can_retry: Optional[bool] = None
    """Whether the tool call can be retried by the client."""

    developer_message: Optional[str] = None
    """
    An internal message that will be logged but will not be shown to the user or the
    AI model.
    """

    retry_after_ms: Optional[int] = None
    """The number of milliseconds (if any) to wait before retrying the tool call."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ResultUnionMember1(BaseModel):
    error: ResultUnionMember1Error
    """An error that occurred inside the tool function."""

    call_id: Optional[str] = None
    """The unique identifier (e.g.

    UUID) for this tool call. If an ID is not provided by the client, the server
    will generate one.
    """

    duration: Optional[float] = None
    """The runtime duration of the tool call, in milliseconds"""

    success: Optional[Literal[False]] = None


Result: TypeAlias = Union[ResultUnionMember0, ResultUnionMember1]


class ToolCallResponse(BaseModel):
    result: Result

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)

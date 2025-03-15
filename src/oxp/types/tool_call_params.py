# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolCallParams", "Request", "RequestContext", "RequestContextAuthorization", "RequestContextSecret"]


class ToolCallParams(TypedDict, total=False):
    request: Required[Request]

    schema: Annotated[str, PropertyInfo(alias="$schema")]


class RequestContextAuthorizationTyped(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the authorization method or authorization provider."""

    token: Required[str]
    """The token for the tool call."""


RequestContextAuthorization: TypeAlias = Union[RequestContextAuthorizationTyped, Dict[str, object]]


class RequestContextSecretTyped(TypedDict, total=False):
    id: Required[str]
    """The secret's unique identifier."""

    value: Required[str]
    """The secret's value."""


RequestContextSecret: TypeAlias = Union[RequestContextSecretTyped, Dict[str, object]]


class RequestContextTyped(TypedDict, total=False):
    authorization: Iterable[RequestContextAuthorization]
    """The authorization information for the tool call."""

    secrets: Iterable[RequestContextSecret]
    """The secrets for the tool call."""

    user_id: str
    """A unique ID that identifies the user, if required by the tool."""


RequestContext: TypeAlias = Union[RequestContextTyped, Dict[str, object]]


class Request(TypedDict, total=False):
    tool_id: Required[str]
    """
    A tool's unique identifier in the format 'Toolkit.Tool[@version]', where
    @version is optional.
    """

    call_id: str
    """A unique identifier (e.g.

    UUID) for this tool call. Used as an idempotency key. If omitted, the server
    will generate an ID.
    """

    context: RequestContext

    input: Dict[str, object]
    """The input parameters for the tool call."""

    trace_id: str
    """An optional trace identifier for the tool call."""

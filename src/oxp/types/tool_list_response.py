# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ToolListResponse",
    "Item",
    "ItemRequirements",
    "ItemRequirementsAuthorization",
    "ItemRequirementsAuthorizationOauth2",
    "ItemRequirementsSecret",
]


class ItemRequirementsAuthorizationOauth2(BaseModel):
    scopes: Optional[List[str]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ItemRequirementsAuthorization(BaseModel):
    id: Optional[str] = None
    """
    A provider's unique identifier, allowing the tool to specify a specific
    authorization provider.
    """

    oauth2: Optional[ItemRequirementsAuthorizationOauth2] = None
    """OAuth 2.0-specific authorization details."""


class ItemRequirementsSecret(BaseModel):
    id: str
    """The secret's unique identifier."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ItemRequirements(BaseModel):
    authorization: Optional[List[ItemRequirementsAuthorization]] = None

    secrets: Optional[List[ItemRequirementsSecret]] = None

    user_id: Optional[bool] = None
    """Whether the tool requires a user ID."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Item(BaseModel):
    id: str
    """
    A tool's unique identifier in the format 'Toolkit.Tool[@version]', where
    @version is optional.
    """

    description: str
    """A plain language explanation of when and how the tool should be used."""

    name: str
    """The tool's name. Only allows alphanumeric characters, underscores, and dashes."""

    version: str
    """
    A tool's semantic version in the format 'x.y.z', where x, y, and z are integers.
    """

    input_schema: Optional[Dict[str, object]] = None
    """JSON Schema describing the input parameters for the tool.

    Supports standard JSON Schema validation but excludes $ref and
    definitions/schemas for simplicity.
    """

    output_schema: Optional[Dict[str, object]] = None
    """JSON Schema describing the output parameters for the tool.

    Supports standard JSON Schema validation but excludes $ref and
    definitions/schemas for simplicity.
    """

    requirements: Optional[ItemRequirements] = None


class ToolListResponse(BaseModel):
    items: List[Item]

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)

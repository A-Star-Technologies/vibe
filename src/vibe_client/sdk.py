"""Hand-written entry point for the generated Vibe client (kept outside the generated files so regeneration
doesn't overwrite it).

    from vibe_client.sdk import VibeClient
    vibe = VibeClient(api_key="...")                  # default: the public API-key gateway
    groups = vibe.list_groups().groups

VibeClient is the generated public client (vibe_client) plus the API-key header and the gateway address.
This module is published: it must never reference the internal client (see internal_sdk.py).
"""
from typing import Any

from smithy_core.interceptors import Interceptor, RequestContext
from smithy_http import Field

from .client import Vibe
from .config import Config

DEFAULT_ENDPOINT = "https://us-east-1.vibe.api.astartech.ai"


class ApiKeyInterceptor(Interceptor[Any, Any, Any, Any]):
    """Adds the caller's API key (x-api-key) to every request."""

    def __init__(self, api_key: str):
        self._api_key = api_key

    def modify_before_signing(self, context: RequestContext[Any, Any]) -> Any:
        request = context.transport_request
        request.fields.set_field(Field(name="x-api-key", values=[self._api_key]))
        return request


class VibeClient(Vibe):
    """The Vibe API client, authenticated with an API key (Vibe web app > Account)."""

    def __init__(self, api_key: str, endpoint: str = DEFAULT_ENDPOINT, **config: Any):
        if not api_key:
            raise ValueError("api_key is required (Vibe web app > Account)")
        super().__init__(config=Config(endpoint_uri=endpoint.rstrip("/"),
                                       interceptors=[ApiKeyInterceptor(api_key)], **config))


"""Hand-written entry point for the generated Vibe client (kept outside the generated files so regeneration
doesn't overwrite it).

    from vibe_client.sdk import VibeClient
    vibe = VibeClient(api_key="...")                  # default: the public API-key gateway
    groups = vibe.list_groups().groups

VibeClient is the generated public client (vibe_client) plus the API-key header and the gateway address.

VibeInternalClient is the same for vibe_client._internal, generated with every operation of the API (data, agent
upload, payment methods, ...). It's for our own agentic tooling and is not part of the public, supported surface:
names and shapes can change without notice. Every operation is still authorized server-side as usual.
"""
from typing import Any

from smithy_core.interceptors import Interceptor, RequestContext
from smithy_http import Field

from ._internal.client import Vibe as _InternalVibe
from ._internal.config import Config as _InternalConfig
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


class VibeInternalClient(_InternalVibe):
    """Every Vibe API operation, authenticated with an API key. Internal: not a supported public interface."""

    def __init__(self, api_key: str, endpoint: str = DEFAULT_ENDPOINT, **config: Any):
        if not api_key:
            raise ValueError("api_key is required (Vibe web app > Account)")
        super().__init__(config=_InternalConfig(endpoint_uri=endpoint.rstrip("/"),
                                                interceptors=[ApiKeyInterceptor(api_key)], **config))

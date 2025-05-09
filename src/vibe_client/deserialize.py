# Code generated by smithy-python-codegen DO NOT EDIT.

import json
from typing import Any

from smithy_core.documents import DocumentValue
from smithy_core.types import TimestampFormat
from smithy_http.aio.interfaces import HTTPResponse
from smithy_http.aio.restjson import parse_rest_json_error_info
from smithy_json import JSONCodec

from .config import Config
from .models import (
    ApiError,
    ForbiddenException,
    QueryAgentOutput,
    UnauthorizedException,
    UnknownApiError,
    ValidationException,
    VibeValidationException,
)


async def _deserialize_query_agent(http_response: HTTPResponse, config: Config) -> QueryAgentOutput:
    if http_response.status != 200 and http_response.status >= 300:
        raise await _deserialize_error_query_agent(http_response, config)

    kwargs: dict[str, Any] = {}

    body = await http_response.consume_body_async()
    if body:
        codec = JSONCodec(default_timestamp_format=TimestampFormat.EPOCH_SECONDS)
        deserializer = codec.create_deserializer(body)
        body_kwargs = QueryAgentOutput.deserialize_kwargs(deserializer)
        kwargs.update(body_kwargs)

    return QueryAgentOutput(**kwargs)

async def _deserialize_error_query_agent(http_response: HTTPResponse, config: Config) -> ApiError:
    code, message, parsed_body = await parse_rest_json_error_info(http_response)

    match code.lower():
        case "unauthorizedexception":
            return await _deserialize_error_unauthorized_exception(http_response, config, parsed_body, message)

        case "validationexception":
            return await _deserialize_error_validation_exception(http_response, config, parsed_body, message)

        case "vibevalidationexception":
            return await _deserialize_error_vibe_validation_exception(http_response, config, parsed_body, message)

        case "forbiddenexception":
            return await _deserialize_error_forbidden_exception(http_response, config, parsed_body, message)

        case _:
            return UnknownApiError(f"{code}: {message}")

async def _deserialize_error_validation_exception(
    http_response: HTTPResponse,
    config: Config,
    parsed_body: dict[str, DocumentValue] | None,
    default_message: str,
) -> ValidationException:
    kwargs: dict[str, Any] = {"message": default_message}

    if parsed_body is None:
        body = await http_response.consume_body_async()
    else:
        body = json.dumps(parsed_body).encode('utf-8')

    if body:
        codec = JSONCodec(default_timestamp_format=TimestampFormat.EPOCH_SECONDS)
        deserializer = codec.create_deserializer(body)
        body_kwargs = ValidationException.deserialize_kwargs(deserializer)
        kwargs.update(body_kwargs)

    return ValidationException(**kwargs)

async def _deserialize_error_forbidden_exception(
    http_response: HTTPResponse,
    config: Config,
    parsed_body: dict[str, DocumentValue] | None,
    default_message: str,
) -> ForbiddenException:
    kwargs: dict[str, Any] = {"message": default_message}

    if parsed_body is None:
        body = await http_response.consume_body_async()
    else:
        body = json.dumps(parsed_body).encode('utf-8')

    if body:
        codec = JSONCodec(default_timestamp_format=TimestampFormat.EPOCH_SECONDS)
        deserializer = codec.create_deserializer(body)
        body_kwargs = ForbiddenException.deserialize_kwargs(deserializer)
        kwargs.update(body_kwargs)

    return ForbiddenException(**kwargs)

async def _deserialize_error_unauthorized_exception(
    http_response: HTTPResponse,
    config: Config,
    parsed_body: dict[str, DocumentValue] | None,
    default_message: str,
) -> UnauthorizedException:
    kwargs: dict[str, Any] = {"message": default_message}

    if parsed_body is None:
        body = await http_response.consume_body_async()
    else:
        body = json.dumps(parsed_body).encode('utf-8')

    if body:
        codec = JSONCodec(default_timestamp_format=TimestampFormat.EPOCH_SECONDS)
        deserializer = codec.create_deserializer(body)
        body_kwargs = UnauthorizedException.deserialize_kwargs(deserializer)
        kwargs.update(body_kwargs)

    return UnauthorizedException(**kwargs)

async def _deserialize_error_vibe_validation_exception(
    http_response: HTTPResponse,
    config: Config,
    parsed_body: dict[str, DocumentValue] | None,
    default_message: str,
) -> VibeValidationException:
    kwargs: dict[str, Any] = {"message": default_message}

    if parsed_body is None:
        body = await http_response.consume_body_async()
    else:
        body = json.dumps(parsed_body).encode('utf-8')

    if body:
        codec = JSONCodec(default_timestamp_format=TimestampFormat.EPOCH_SECONDS)
        deserializer = codec.create_deserializer(body)
        body_kwargs = VibeValidationException.deserialize_kwargs(deserializer)
        kwargs.update(body_kwargs)

    return VibeValidationException(**kwargs)

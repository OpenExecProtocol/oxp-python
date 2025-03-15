# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from oxp import Oxp, AsyncOxp
from oxp.types import ToolCallResponse, ToolListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Oxp) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Oxp) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Oxp) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_call(self, client: Oxp) -> None:
        tool = client.tools.call(
            request={"tool_id": "sqFnKL1N_jr_.U0_2_jv__a"},
        )
        assert_matches_type(ToolCallResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_call_with_all_params(self, client: Oxp) -> None:
        tool = client.tools.call(
            request={
                "tool_id": "sqFnKL1N_jr_.U0_2_jv__a",
                "call_id": "call_id",
                "context": {
                    "authorization": [
                        {
                            "id": "id",
                            "token": "token",
                        }
                    ],
                    "secrets": [
                        {
                            "id": "id",
                            "value": "value",
                        }
                    ],
                    "user_id": "user_id",
                },
                "input": {"foo": "bar"},
                "trace_id": "trace_id",
            },
            schema="https://example.com",
        )
        assert_matches_type(ToolCallResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_call(self, client: Oxp) -> None:
        response = client.tools.with_raw_response.call(
            request={"tool_id": "sqFnKL1N_jr_.U0_2_jv__a"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCallResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_call(self, client: Oxp) -> None:
        with client.tools.with_streaming_response.call(
            request={"tool_id": "sqFnKL1N_jr_.U0_2_jv__a"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCallResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOxp) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOxp) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOxp) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_call(self, async_client: AsyncOxp) -> None:
        tool = await async_client.tools.call(
            request={"tool_id": "sqFnKL1N_jr_.U0_2_jv__a"},
        )
        assert_matches_type(ToolCallResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_call_with_all_params(self, async_client: AsyncOxp) -> None:
        tool = await async_client.tools.call(
            request={
                "tool_id": "sqFnKL1N_jr_.U0_2_jv__a",
                "call_id": "call_id",
                "context": {
                    "authorization": [
                        {
                            "id": "id",
                            "token": "token",
                        }
                    ],
                    "secrets": [
                        {
                            "id": "id",
                            "value": "value",
                        }
                    ],
                    "user_id": "user_id",
                },
                "input": {"foo": "bar"},
                "trace_id": "trace_id",
            },
            schema="https://example.com",
        )
        assert_matches_type(ToolCallResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_call(self, async_client: AsyncOxp) -> None:
        response = await async_client.tools.with_raw_response.call(
            request={"tool_id": "sqFnKL1N_jr_.U0_2_jv__a"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCallResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_call(self, async_client: AsyncOxp) -> None:
        async with async_client.tools.with_streaming_response.call(
            request={"tool_id": "sqFnKL1N_jr_.U0_2_jv__a"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCallResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from oxp import Oxp, AsyncOxp

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check(self, client: Oxp) -> None:
        health = client.health.check()
        assert health is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check(self, client: Oxp) -> None:
        response = client.health.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert health is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check(self, client: Oxp) -> None:
        with client.health.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert health is None

        assert cast(Any, response.is_closed) is True


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check(self, async_client: AsyncOxp) -> None:
        health = await async_client.health.check()
        assert health is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncOxp) -> None:
        response = await async_client.health.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert health is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncOxp) -> None:
        async with async_client.health.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert health is None

        assert cast(Any, response.is_closed) is True

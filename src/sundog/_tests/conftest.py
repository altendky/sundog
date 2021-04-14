import functools
import pathlib
import typing

import attr
import pymodbus.client.asynchronous.tcp
import pymodbus.client.asynchronous.schedulers
import pytest
import _pytest.fixtures
import trio

import sundog.client
import sundog.server


@attr.s(auto_attribs=True, frozen=True)
class SunSpecServerFixtureResult:
    host: str
    port: int
    server: sundog.server.Server


@pytest.fixture(name="sunspec_server")
async def sunspec_server_fixture(
    nursery: trio.Nursery,
) -> typing.AsyncIterator[SunSpecServerFixtureResult]:
    model_summaries = [
        sundog.server.ModelSummary(id=1, length=66),
        sundog.server.ModelSummary(id=17, length=12),
        sundog.server.ModelSummary(id=103, length=50),
        sundog.server.ModelSummary(id=126, length=226),
    ]

    server = sundog.server.Server.build(model_summaries=model_summaries)

    host = "127.0.0.1"

    [listener] = await nursery.start(
        functools.partial(
            trio.serve_tcp,
            server.tcp_server,
            host=host,
            port=0,
        ),
    )

    yield SunSpecServerFixtureResult(
        host=host,
        port=listener.socket.getsockname()[1],
        server=server,
    )


@pytest.fixture(name="unscanned_sunspec_client")
async def unscanned_sunspec_client_fixture(
    sunspec_server: SunSpecServerFixtureResult,
) -> typing.AsyncIterator[sundog.client.Client]:
    async with sundog.client.open_client(
        host=sunspec_server.host,
        port=sunspec_server.port,
    ) as client:
        yield client


@pytest.fixture(name="sunspec_client")
async def sunspec_client_fixture(
    unscanned_sunspec_client: sundog.client.Client,
) -> sundog.client.Client:
    await unscanned_sunspec_client.scan()
    return unscanned_sunspec_client

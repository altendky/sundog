"""Top-level package for sundog."""

from sundog.exceptions import (
    SundogError,
    BaseAddressNotFoundError,
    InternalError,
    InvalidBaseAddressError,
    ModbusError,
)

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

base_address_sentinel = b"SunS"

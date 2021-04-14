import typing

if typing.TYPE_CHECKING:
    import pymodbus.pdu


class SundogError(Exception):
    """The base for all sundog errors.  Not to be raised directly, but could be used if
    you want to catch any except this program may explicitly raise."""

    # https://github.com/sphinx-doc/sphinx/issues/7493
    __module__ = "sundog"


class BaseAddressNotFoundError(SundogError):
    """Raised if no address matched the expected SunSpec sentinel value."""

    def __init__(self, addresses: typing.Sequence[int]) -> None:
        import sundog

        sentinel = repr(sundog.base_address_sentinel)
        addresses_string = ", ".join(str(address) for address in addresses)
        super().__init__(
            f"SunSpec sentinel {sentinel} not found while searching: {addresses_string}"
        )

    # https://github.com/sphinx-doc/sphinx/issues/7493
    __module__ = "sundog"


class InternalError(Exception):
    """Raised when things that should not happen do, and they aren't the user's fault."""

    # https://github.com/sphinx-doc/sphinx/issues/7493
    __module__ = "sundog"


class InvalidBaseAddressError(SundogError):
    """Raised if the specified base address does not match the expected SunSpec
    sentinel value.
    """

    def __init__(self, address: int, value: bytes) -> None:
        import sundog

        sentinel = repr(sundog.base_address_sentinel)
        super().__init__(
            f"SunSpec sentinel {sentinel} not found at {address}: {value!r}"
        )

    # https://github.com/sphinx-doc/sphinx/issues/7493
    __module__ = "sundog"


class ModbusError(SundogError):
    """Raised when a Modbus action results in a Modbus exception."""

    def __init__(self, exception: "pymodbus.pdu.ExceptionResponse") -> None:
        codes = [
            f"{label}: {value} == 0x{value:02x}"
            for label, value in [
                ["original", exception.original_code],
                ["function", exception.function_code],
                ["exception", exception.exception_code],
            ]
        ]
        message = f"Exception response received.  {', '.join(codes)}"

        super().__init__(message)

    # https://github.com/sphinx-doc/sphinx/issues/7493
    __module__ = "sundog"

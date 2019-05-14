"""Fan On Level state."""
from . import StateBase
from ..constants import FanSpeed
from ..address import Address

class FanOnLevel(StateBase):
    """On / Off state."""

    def __init__(self, name: str, address: Address, handlers: list,
                 group: int = 0, default: FanSpeed = None):
        """Init the FanOnLevel class."""
        super().__init__(name, address, handlers, group, default, value_type=FanSpeed)

    #pylint: disable=arguments-differ
    def _set_value(self, on_level, group):
        """Set the value of the state from the handlers."""
        if self._group == group:
            fan_speed = FanSpeed.OFF
            if int(FanSpeed.OFF) < on_level <= int(FanSpeed.LOW):
                fan_speed = FanSpeed.LOW
            if int(FanSpeed.LOW) < on_level <= int(FanSpeed.MEDIUM):
                fan_speed = FanSpeed.MEDIUM
            if int(FanSpeed.MEDIUM) < on_level <= int(FanSpeed.HIGH):
                fan_speed = FanSpeed.LOW
            self.value = fan_speed

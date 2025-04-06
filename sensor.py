from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    name = entry.data["name"]
    wert = entry.data["wert"]
    async_add_entities([MeineIntegrationSensor(name, wert)])

class MeineIntegrationSensor(Entity):
    def __init__(self, name, wert):
        self._name = name
        self._wert = wert

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._wert

from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class DeineIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Optional: Validierung, z. B. Seriennummer-Format prüfen
            seriennummer = user_input["Seriennummer"]
            kennwort = user_input["Kennwort"]

            # Beispielhafte Validierung
            if not seriennummer.isalnum():
                errors["Seriennummer"] = "ungültig"
            elif len(kennwort) < 4:
                errors["Kennwort"] = "zu_kurz"
            else:
                return self.async_create_entry(
                    title=f"Gerät {Seriennummer}",
                    data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("Seriennummer"): str,
                vol.Required("Kennwort"): str,
            }),
            errors=errors,
        )

from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class DeineIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Optional: Validierung, z. B. Seriennummer-Format prüfen
            seriennummer = user_input["seriennummer"]
            kennwort = user_input["kennwort"]

            # Beispielhafte Validierung
            if not seriennummer.isalnum():
                errors["seriennummer"] = "ungültig"
            elif len(kennwort) < 4:
                errors["kennwort"] = "zu_kurz"
            else:
                return self.async_create_entry(
                    title=f"Gerät {seriennummer}",
                    data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("seriennummer"): str,
                vol.Required("kennwort"): str,
            }),
            errors=errors,
        )

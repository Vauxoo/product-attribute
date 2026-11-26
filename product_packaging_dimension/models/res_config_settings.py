# Copyright 2026 Vauxoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    def set_values(self):
        """Recompute dimensional packaging volumes when the volume UoM changes."""
        icp = self.env["ir.config_parameter"].sudo()
        old_value = icp.get_param("product.volume_in_cubic_feet")
        res = super().set_values()
        if icp.get_param("product.volume_in_cubic_feet") != old_value:
            self.env["product.packaging"]._recompute_dimensional_volume()
        return res

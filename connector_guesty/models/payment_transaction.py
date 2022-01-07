# Copyright (C) 2021 Casai (https://www.casai.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import datetime
import logging

from odoo import _, api, models
from odoo.exceptions import ValidationError

_log = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    @api.model
    def create(self, values):
        res = super().create(values)
        for sale in res.sale_order_ids:
            if sale.state == "cancel":
                raise ValidationError(_("Order was canceled"))

            if sale.validity_date < datetime.datetime.now():
                raise ValidationError(_("Order was expired"))

            reservation_id = (
                self.env["pms.reservation"]
                .sudo()
                .search([("sale_order_id", "=", sale.id)], limit=1)
            )

            if reservation_id:
                try:
                    reservation_id.guesty_check_availability()
                except Exception as ex:
                    _log.error(ex)
                    raise ValidationError(_("Reservation dates are not available"))
        return res

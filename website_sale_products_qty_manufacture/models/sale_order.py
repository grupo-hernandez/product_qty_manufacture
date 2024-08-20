from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
  
    def _get_cart_and_free_qty(self, line=None, product=None, **kwargs):
        """ Get cart quantity and free quantity for given product or line's product.

        Note: self.ensure_one()

        :param SaleOrderLine line: The optional line
        :param ProductProduct product: The optional product
        """
        self.ensure_one()
        if not line and not product:
            return 0, 0
        cart_qty = sum(
            self._get_common_product_lines(line, product, **kwargs).mapped('product_uom_qty')
        )
        free_qty = (product or line.product_id).with_context(warehouse=self.warehouse_id.id).free_qty + (product or line.product_id).with_context(warehouse=self.warehouse_id.id).qty_bom_available_get()
        return cart_qty, free_qty
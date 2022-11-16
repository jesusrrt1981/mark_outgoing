from odoo import fields, models, api,_


class Company(models.Model):
    _inherit="mail.mail"

    

    def cancel_pay(self):
        for line in self:
            if line.state == 'exception':
                line.write({'state': 'outgoing'})
            

   
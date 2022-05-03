from  datetime import date 
from odoo import api,fields,models


    
class NewBankDataLine(models.Model):
    _name="new.bank.data.line"
    _description="New Bank Data Line" 
       

    date=fields.Date(string="Date", default=date.today(),tracking=True)
    label=fields.Char(string="Description",tracking=True)
    debit=fields.Float(string="Debit",tracking=True)
    credit=fields.Float(string="Credit",tracking=True)
    balance=fields.Float(string="Balance",compute="_total_balance",tracking=True)
    transaction_type=fields.Selection([("credit","Credit"),("debit","Debit")],tracking=True)
    record_id=fields.Many2one("new.bank.data",string="Record I'd")
    
    @api.depends("transaction_type")
    def _total_balance(self):
        
        for rec in self:
            temp_balance=0
            temp_balance = rec.balance
            if rec.transaction_type =="credit":
                rec.balance = temp_balance - rec.credit
            elif rec.transaction_type =="debit":
                rec.balance = temp_balance + rec.debit
            
                    
class NewBankData(models.Model):
    _name="new.bank.data"
    _description= "New Bank Data"
    _inherit="new.bank.data.line"

    
    
    customer_id=fields.Many2one("new.bank.customer" , string="Customer I'd",tracking=True)
    opening_balance=fields.Float(string="Opening Balance",tracking=True)
    closing_balance=fields.Float(string="Closing Balance",compute="_sum_of_balance",tracking=True)
    statements_ids=fields.One2many("new.bank.data.line","record_id",string="Statement")
    
    
    @api.depends("statements_ids")
    def _sum_of_balance(self):
        
        for rec in self:
            rec.closing_balance=rec.balance
                          


class NewBankCustomer(models.Model):
    _name="new.bank.customer"
    _description="New Bank Customer"    
    
    
    name=fields.Char(string="Customer Name",tracking=True,required=True)
    email=fields.Char(string="Customer Email",tracking=True)
    
    
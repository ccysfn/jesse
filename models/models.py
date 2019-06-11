# -*- coding: utf-8 -*-

from odoo import models, fields, api

class soft(models.Model):
    _name = 'jyinspur.soft'

    name = fields.Char('名称')
    ggxh = fields.Char('规格型号')
    price = fields.Float('价格')
    soft_type = fields.Selection([('single','单组织'),('multiple','多组织')],'类型')
    #price = fields.Float(compute="_value_pc", store=True)
    description = fields.Text('描述')
    jldw = fields.Many2one('uom.uom',string='单位')
    qm = fields.Char(string='全名',compute='qm_compute')  #compute为调用函数名
    state = fields.Selection([('draft','未提交'),('processing','已提交'),('done','已审批')],readonly=True,string='审批状态',default='draft')

    @api.one
    @api.depends('name','ggxh')  #填入需要的参数
    def qm_compute(self):
        self.qm = str(self.name) + '-' + str(self.ggxh)  #需要加上str()函数不然提示数据类型错误

    #@api.depends('value')
    #def _value_pc(self):
        #self.value2 = float(self.value) / 100
    @api.multi
    def confirm(self):
        self.write({'state': 'processing'})
        return {}

    @api.multi
    def cancle_confirm(self):
        self.write({'state': 'draft'})
        return {}

    @api.multi
    def done(self):
        self.write({'state': 'done'})
        return {}

    @api.multi
    def no_pass(self):
        self.write({'state': 'processing'})
        return {}


class user(models.Model):
    _name = 'jyinspur.user'
    grade = fields.Char('年级')


class base(models.Model):
    _name = 'jyinspur.base'
    dict = fields.Char('字典')

#软件订单
class softorders(models.Model):
    _name = 'jyinspur.softorder'
    soft = fields.Many2one('jyinspur.soft',string='软件产品')
    quantity=fields.Integer('数量')
    user = fields.Many2one('res.partner',string='用户')
    state = fields.Selection([('draft','未提交'),('processing','已提交'),('done','已审批')],readonly=True,string='审批状态',default='draft')
    price = fields.Float('单价',compute='_get_price')
    sum = fields.Float('总价',default=0, compute='_compute_pay_total', store=True,readonly=True)
    
    @api.one
    @api.depends('price', 'quantity')
    def _compute_pay_total(self):
        self.sum = self.price*self.quantity
    
    @api.one
    @api.depends('soft')
    def _get_price(self):
        self.price = self.soft.price
    
    
    @api.multi
    def confirm(self):
        self.write({'state': 'processing'})
        return {}

    @api.multi
    def cancle_confirm(self):
        self.write({'state': 'draft'})
        return {}

    @api.multi
    def done(self):
        self.write({'state': 'done'})
        return {}

    @api.multi
    def no_pass(self):
        self.write({'state': 'processing'})
        return {}




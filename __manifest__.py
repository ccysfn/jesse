# -*- coding: utf-8 -*-
{
    'name': "jyinspur",

    'summary': """
        jyinspur soft""",

    'description': """
        jyinspur soft
    """,

    'author': "jyinspur-cao",
    'website': "http://www.inspur.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/parents.xml',
        'views/views.xml',
        'views/base.xml',
        #'views/course.xml',
        'views/softorder.xml',
        'views/user.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
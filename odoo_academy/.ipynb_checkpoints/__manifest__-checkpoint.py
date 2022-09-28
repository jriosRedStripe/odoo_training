# -*- coding: utf-8 -*-

{
    'name': 'Academia Odoo',
    'summary': """ Academy app to manage Training """,
    'description': """ Academy module to manage Training:
                * Courses
                * Sessions
                * Atendees
    """,
    'author': 'Jesús Ríos',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale'],
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    'demo':[
        'demo/academy_demo.xml',
    ],
    'license': 'LGPL-3',
}
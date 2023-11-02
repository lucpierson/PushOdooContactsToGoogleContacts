# -*- coding: utf-8 -*-
# Copyright 2023 Luc PIERSON <luc.pierson@gmail.com>
# Copyright 2023 Informatel-Lab Luc Pierson
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "lpn_contact_module",

    'summary': """
        this is a http launcher possibility to push the odoo contact 
        list on an identified through oauth2 credentials gmail account """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Luc Pierson" ,
    'website': "http://bdm.lucpierson.com",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

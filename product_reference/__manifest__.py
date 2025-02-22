{
    'name': 'Product Reference',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Product reference management''',
    'depends': [
        'base',
        'base_xmlid',
        'uom',
        'product',
        'mrp',
        'product_reference_management',
        'product_state_review',
        'product_location',
        'product_prices',
        'product_legacy_routes',
        'product_tagging',
        'product_pack_order_type',
        'product_public_code',
        'mrp_production_request',
        'mrp_bom_dates',
        'mrp_bom_supplier',
        'mrp_bom_prices',
        'mrp_buy_consu',
        'sale_purchase',
        'sale_timesheet',
        'stock_available_unreserved',
    ],
    'data':
        [
            'security/model_security.xml',
            'security/ir.model.access.csv',
            'views/assets.xml',
            'views/product_template.xml',
            'views/product_product.xml',
            'views/ref_attribute.xml',
            'views/ref_property.xml',
            'views/ref_reference.xml',
            'views/ref_reference_line.xml',
            'views/ref_category.xml',
            'views/ref_category_line.xml',
            'views/ref_version.xml',
            'views/res_config_settings.xml',
            'wizard/change_product_state_by_category.xml',
            'views/menu.xml',
        ],
    'demo':
        [
            'demo/ref_categories.xml',
            'demo/ref_references.xml',
        ],
    'installable': True
}

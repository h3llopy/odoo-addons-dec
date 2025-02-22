{
    'name': 'Purchase Stock Traceability',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': 'Get origin for each purchase line',
    'depends': [
        'purchase_line_procurement_group',
        'purchase_traceability',
        'stock_traceability',
        'stock_orderpoint_traceability',
        'sale_traceability',
    ],
    #'force_migration':'12.0.0.0.0',
    'data':
        [
            'views/purchase_order.xml',
        ],
    'installable': True
}

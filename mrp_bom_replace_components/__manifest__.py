{
    'name': 'Manufacturing Bom Replace Components',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Replace in batch''',
    'depends': [
        'mrp',
        'mrp_bom_supplier',
        'mrp_buy_consu',
        'queue_job',
    ],
    'data': [
        'views/bom_template.xml',
        'wizard/replace_bom_components.xml',
    ],
    'installable': True
}

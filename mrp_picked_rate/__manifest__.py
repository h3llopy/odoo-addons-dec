{
    'name': 'Manufacturing Picked Rate',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Reimplementation of picked_rate''',
    'depends': ['mrp', ],
    'data': [
        'data/mrp_production_cron.xml',
        'views/mrp_production.xml',
    ],
    'installable': True
}

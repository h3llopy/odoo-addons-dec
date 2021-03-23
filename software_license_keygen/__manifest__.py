{
    'name': 'Software License (keygen)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Key generator''',
    'external_dependencies':
        {
            'python':
                [
                    'key_generator',  # pip install key-generator
                    'Crypto',  # pip install pycryptodome
                ],
        },
    'depends': ['software_license', ],
    'data':
        [
            'views/software_license.xml',
            'views/software_license_application.xml',
        ],
    'installable': True
}

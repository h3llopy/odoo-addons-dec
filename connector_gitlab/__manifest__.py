{
    'name': 'GitLab Connector',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Create and map gitlab users when giving portal access",
    'depends': ['base', ],
    'data': [
        'security/model_security.xml',
        'security/ir.model.access.csv',
        'views/gitlab_resource.xml',
    ],
    'installable': True
}

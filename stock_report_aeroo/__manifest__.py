{
    'name': 'Stock (aeroo report)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Picking report''',
    'depends': [
        'company_fax',
        'stock',
        'dec_report_aeroo',
    ],
    'data':
        [
            'report/stock_picking.xml',
        ],
    'installable': True
}

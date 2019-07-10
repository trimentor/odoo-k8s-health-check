# -*- coding: utf-8 -*-
{
    'name': "k8s_health_check",

    'summary': """
        Let K8S know if the app is ready or alive/dead
    """,

    'description': """
        Let K8S know if the app is ready to serve traffic (readiness probe),
        or if it is alive or dead (liveness probe).
    """,

    'author': "Kjel Delaey",
    'website': "https://github.com/trimentor/odoo-k8s-health-check",

    'category': 'Uncategorized',
    'version': '0.0.1',

    'depends': ['base'],
}

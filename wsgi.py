# -*- coding: utf-8 -*-
# @Time : 2023/7/12 2:18 下午
# @Author : lshunger
# @Email : 470968155@qq.com
# @File : wsgi.py

from server.app import app
from server.website import Website
from server.backend import Backend_Api
from json import load


# Load configuration from config.json
config = load(open('config.json', 'r'))
site_config = config['site_config']

# Set up the website routes
site = Website(app)
for route in site.routes:
    app.add_url_rule(
        route,
        view_func=site.routes[route]['function'],
        methods=site.routes[route]['methods'],
    )

# Set up the backend API routes
backend_api = Backend_Api(app, config)
for route in backend_api.routes:
    app.add_url_rule(
        route,
        view_func=backend_api.routes[route]['function'],
        methods=backend_api.routes[route]['methods'],
    )

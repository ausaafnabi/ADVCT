# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2021 - Amberflux
"""

from flask import Blueprint

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

import os

from dash import Dash
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

from config import Config


def create_app():
    flawlys = Flask(__name__)
    # Load default configurations from config.py
    flawlys.config.from_object(Config)

    from app.dash.layout import layout as layout_main
    from app.dash.callbacks import register_callbacks as register_callbacks_main
    register_dash_app(app_obj=flawlys,
                      server_url_path='',
                      title='Main Dashboard',
                      layout=layout_main,
                      register_callbacks=register_callbacks_main(flawlys)
                      )

    from app.dash_ec2_ami.layout import layout as layout_ec2_ami
    from app.dash_ec2_ami.callbacks import register_callbacks as register_callbacks_ec2_ami
    register_dash_app(app_obj=flawlys,
                      server_url_path='ami',
                      title='EC2 AMI Dashboard',
                      layout=layout_ec2_ami,
                      register_callbacks=register_callbacks_ec2_ami(flawlys)
                      )

    register_extensions(flawlys)
    register_blueprints(flawlys)

    return flawlys


def register_dash_app(app_obj, server_url_path, title, layout, register_callbacks):
    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
    }

    flawlys = Dash(__name__,
                   server=app_obj,
                   url_base_pathname=f'/{server_url_path}/',
                   assets_folder=get_root_path(__name__) + f'/{server_url_path}/assets/',
                   meta_tags=[meta_viewport])

    with app_obj.app_context():
        flawlys.title = title
        flawlys.layout = layout
        register_callbacks(flawlys)

    _protect_dash_views(flawlys)


def _protect_dash_views(app_obj):
    for view_function in app_obj.server.view_functions:
        if view_function.startswith(app_obj.config.url_base_pathname):
            app_obj.server.view_functions[view_function] = login_required(
                app_obj.server.view_functions[view_function]
            )


def register_extensions(app_obj):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(app_obj)
    login.init_app(app_obj)
    login.login_view = "main.login"
    migrate.init_app(app_obj, db)


def register_blueprints(app_obj):
    from app.server import server_bp

    app_obj.register_blueprint(server_bp)

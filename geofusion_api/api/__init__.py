from geofusion_api.api.main import api_bp


def init_app(app):
    app.register_blueprint(api_bp)

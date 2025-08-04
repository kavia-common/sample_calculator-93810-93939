from flask import Flask, jsonify
from flask_cors import CORS
from .routes.health import blp
from flask_smorest import Api
from .config import Config
from .db import db
from .logging_config import init_logging

def create_app():
    """PUBLIC_INTERFACE
    Factory for creating Flask app with essential extensions, DB, logging, and error handlers set up.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(Config)

    # Swagger and CORS Config
    app.config["API_TITLE"] = "Sample Calculator Backend API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Logging setup
    init_logging(app)

    # Initialize DB
    db.init_app(app)
    
    # Register blueprints
    api = Api(app)
    api.register_blueprint(blp)
    
    # Centralized error handler
    @app.errorhandler(Exception)
    def handle_error(error):
        app.logger.error(f"Unhandled error: {str(error)}")
        return jsonify({
            "error": str(error),
            "type": error.__class__.__name__
        }), 500

    return app

# Application entrypoint
app = create_app()


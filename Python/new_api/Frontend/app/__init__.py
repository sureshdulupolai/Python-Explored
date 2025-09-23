from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register Blueprints
    from app.routes.product import product_bp
    app.register_blueprint(product_bp, url_prefix="/products")

    # from app.routes.category import category_bp
    # app.register_blueprint(category_bp, url_prefix="/categories")

    return app

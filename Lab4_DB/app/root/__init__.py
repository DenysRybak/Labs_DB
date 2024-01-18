from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)


    from .agencies_route import agency_bp
    from .agency_region_route import agency_regions_bp
    from .animator_event_type_route import animator_event_types_bp
    from .animators_agencies_route import animators_agencies_bp
    from .animators_route import animators_bp
    from .order_agencies_route import order_agencies_bp
    from .order_animators_route import order_animators_bp
    from .order_days_route import order_days_bp
    from .orders_route import order_bp
    from .type_events_routes import type_events_bp

    app.register_blueprint(agency_bp)
    app.register_blueprint(agency_regions_bp)
    app.register_blueprint(animator_event_types_bp)
    app.register_blueprint(animators_agencies_bp)
    app.register_blueprint(animators_bp)
    app.register_blueprint(order_agencies_bp)
    app.register_blueprint(order_animators_bp)
    app.register_blueprint(order_days_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(type_events_bp)
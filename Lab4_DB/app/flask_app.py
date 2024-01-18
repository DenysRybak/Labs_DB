from app import create_flask_app

flask_app = create_flask_app()

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=False)

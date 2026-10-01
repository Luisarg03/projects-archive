from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Levanto mi servidor Prod
    # app.run(port=5000, debug=True)  # Levanto mi servidor Desa

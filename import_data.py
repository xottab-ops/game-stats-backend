from app import create_app
from app.seeds import load_data

app = create_app()

with app.app_context():
    load_data("static/steam.csv")
    print("Data uploaded from file!")

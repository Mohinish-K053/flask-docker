from flask import Flask, jsonify
from config import Config
from models import db, Hit

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Use app context to initialize DB and default values
with app.app_context():
    db.create_all()
    if not Hit.query.first():
        db.session.add(Hit(count=0))
        db.session.commit()

@app.route('/')
def index():
    hit = Hit.query.first()
    hit.count += 1
    db.session.commit()
    return jsonify(message="Welcome!", hits=hit.count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


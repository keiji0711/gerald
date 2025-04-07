from flask import Flask
from routes.officers import bp as officers_bp
from routes.members import bp as members_bp
from routes.admin import bp as admin_bp

app = Flask(__name__)

app.register_blueprint(officers_bp)
app.register_blueprint(members_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
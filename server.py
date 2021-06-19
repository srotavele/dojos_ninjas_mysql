from flask_app import app
from flask_app.controllers import dojo_ctrl, new_ninja_ctrl


if __name__ == "__main__":
    app.run(debug=True)
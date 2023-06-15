from flask import render_template
import config
from models import Student

app = config.connex_app
#app.add_api(config.basedir / "swagger.yml")

@app.route("/", methods=['GET'])
def home():
    students = Student.query.all()
    return render_template('student.html', students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
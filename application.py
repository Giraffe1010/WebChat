from flask import Flask, render_template

app = Flask(__name__) # WSGI standard
# make it central callable object

app.secret_key = 'secretkey'

@app.route("/", methods=['GET','POST'])
def index():
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

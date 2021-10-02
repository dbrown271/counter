from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "im batman" 


@app.route('/')
def index():
    if "button" in session:
        session["button"] += 1
    else:
        session["button"] = 0
    
    return render_template('index.html')


@app.route('/times_two')
def times_two():
    if "button2" in session:
        session["button2"] += 2
    else:
        session["button2"] = 0
    
    return render_template('index.html')



@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)

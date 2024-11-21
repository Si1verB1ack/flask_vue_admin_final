from app import app, render_template

@app.route('/')
def dashboard():
    return render_template('admin/index.html')
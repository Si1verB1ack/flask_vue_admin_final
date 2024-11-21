from app import app, render_template

@app.route('/admin/products')
def products_list():
    return render_template('admin/product/list.html')
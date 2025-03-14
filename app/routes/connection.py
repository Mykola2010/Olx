from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import ProductForm
from app.models import Product, Session, engine


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-product/', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        session = Session(bind=engine)
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            image=form.image.data
        )
        try:
            session.add(new_product)
            session.commit()
            flash("Product added successfully!", "success")
            return redirect(url_for('add_product'))
        except Exception as exception:
            session.rollback()
            flash(f"Error: {exception}", "danger")
        finally:
            session.close()

    return render_template('add_product.html', form=form)
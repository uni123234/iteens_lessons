from flask import render_template

from . import bp  # Зверніть увагу на крапку перед "."


@bp.route('/')
def get_index():
    return render_template('main/main_page.html', title='Головна сторінка', message='Budget_tracker')

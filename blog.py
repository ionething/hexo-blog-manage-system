import os, platform

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
@login_required
def index():
    """Show all the posts, most recent first."""
    return render_template('index.html', os=os)


@bp.route('/setting')
@login_required
def setting():
    settings = get_db().execute('SELECT * FROM setting ORDER BY setting_index').fetchall()
    return render_template('setting.html', settings=settings)


@bp.route('/saveSetting', methods=('post',))
@login_required
def save_setting():
    setting_key = request.form.get('setting_key', None, type=str)
    setting_value = request.form.get('setting_value', None, type=str)
    if setting_key:
        db = get_db()
        db.execute('update setting set setting_value = ? where setting_key = ?', (setting_value, setting_key))
        db.commit()
        return jsonify(state=200, msg='修改成功')
    return jsonify(state=404, msg='设置的值不存在')


@bp.route('/list')
@login_required
def list():
    blogs = []
    setting_dir = get_db().execute("select setting_value from setting where setting_key='blog.dir'").fetchone()
    if setting_dir is not None and os.path.isdir(setting_dir[0]):
        blogs = [x.rstrip('.md') for x in os.listdir(setting_dir[0]) if
                 os.path.isfile(os.path.join(setting_dir[0], x)) and x.endswith('.md')]
    return render_template('list.html', blogs=blogs)


@bp.route('/edit')
@login_required
def edit():
    name = request.args.get('name', '')
    text = ''
    if name:
        setting_dir = get_db().execute("select setting_value from setting where setting_key='blog.dir'").fetchone()
        if setting_dir is not None and os.path.isdir(setting_dir[0]):
            with open(os.path.join(setting_dir[0], name + ".md"), 'r') as f:
                text = f.read()

    args = {
        "name": name,
        "text": text
    }
    return render_template('edit.html', **args)


@bp.route('/save', methods=("post", ))
@login_required
def save():
    name = request.form['name']
    rename = request.form['rename']
    text = request.form['text']

    if not rename:
        abort(400)

    setting_dir = get_db().execute("select setting_value from setting where setting_key='blog.dir'").fetchone()
    if setting_dir is not None and os.path.isdir(setting_dir[0]):
        if name:
            # 修改
            file_dir = os.path.join(setting_dir[0], name + ".md")
            if not os.path.exists(file_dir):
                abort(400)
            else:
                if name != rename:
                    file_dir_re = os.path.join(setting_dir[0], rename + ".md")
                    os.rename(file_dir, file_dir_re)
                    file_dir = file_dir_re
                with open(file_dir, 'w') as f:
                    f.write(text)
                flash("保存成功")

        else:
            # 新增
            file_dir = os.path.join(setting_dir[0], rename + ".md")
            if not os.path.exists(file_dir):
                with open(file_dir, 'w') as f:
                    f.write(text)
                flash("保存成功")
            else:
                flash("存在同样标题的博客，请修改标题名称")

    return redirect(url_for('blog.edit', name=rename))

@bp.route('/operate')
@login_required
def operate():
    return "operate"

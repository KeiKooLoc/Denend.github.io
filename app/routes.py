# -*- coding: utf-8 -*-
from flask import render_template, url_for, redirect, flash, session, request, jsonify
from app import app, db, captcha
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Answer, Question, Post
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from json import dumps
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    num_of_users = str(len(User.query.all()))
    if request.method == 'POST':
        body = request.form['body']
        if len(body) > 500 or len(body) < 1:
            flash('the message must be between 1 and 500 symbols', 'info')
            return redirect(url_for('home'))
        else:
            post = Post(body=body, author=current_user)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('home'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('home', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('home', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('home.html', title=u'Дом, сука', num_of_users=num_of_users, posts=posts.items,
                            next_url=next_url, prev_url=prev_url)


@app.route('/delete/<string:id>', methods =['POST'])
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post was successfully deleted', 'success')
    return redirect(url_for('home'))


@app.route('/edit_post/<string:id>', methods = ['GET', 'POST'])
def edit_post(id):
    post = Post.query.get(id)
    if post.user_id != current_user.id:
        return redirect(url_for('home'))
    if request.method == 'POST' and current_user.id == post.user_id:
        new_body = request.form['body']
        post.body = new_body
        db.session.commit()
        flash('Your post successfully changed', 'success')
        return redirect(url_for('home'))
    return render_template('edit_post.html', post=post.body)


@app.route('/_opros_process', methods=['GET', 'POST'])
def opros_process():
    if request.method == 'POST':
        ans = request.get_json()
        for key in ans:
           q = Question.query.get(int(key))
           answer = Answer(qstion=q, author=current_user, ans=ans[key]['result'])
           db.session.add(answer)
        db.session.commit()
        result = {}
        for i in range(1, 10):
            result[i] = Answer.query.filter_by(ans=True, question_id=i).count()
        return jsonify(result)


@app.route('/opros')
@login_required
def opros():
    a = Answer.query.filter_by(user_id=current_user.id).count()
    if a > 0:
        flash(u'уже проходил опрос', 'info')
        return redirect(url_for('home'))
    return render_template('opros.html', title=u'Бро, пройди опросик')


@app.route('/_statistics_process', methods=['GET', 'POST'])
def statistics_process():
    result = {}
    for i in range(1, 10):
        result[i] = Answer.query.filter_by(ans=True, question_id=i).count()
    return jsonify(result)


@app.route('/statistics')
@login_required
def statistic():
    a = Answer.query.filter_by(user_id=current_user.id).count()
    if a == 0:
        flash(u'пройди опрос и сможешь посмотреть статистику', 'info')
        return redirect(url_for('opros'))
    return render_template('statistic.html', title=u'дыбай шо там')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title=u'курлык')


@app.route('/f_y_process', methods=['GET', 'POST'])
def f_y_process():
    result = request.get_json()
    u = User.query.filter_by(id=current_user.id).first()
    if int(result['count']) > u.f_y_record:
        u.f_y_record = int(result['count'])
        db.session.commit()
    top3 = User.query.filter(User.f_y_record>=0).order_by(User.f_y_record.desc())[:3]
    top3dic = {}
    for div_id, i in enumerate(reversed(top3)):
        top3dic[i.f_y_record] = [i.username, div_id]
    print(top3dic)
    return dumps(top3dic, indent=2, sort_keys=True)


# Flappy Yuras view
@app.route('/flappy_yuras')
@login_required
def flappy_yuras():
    top3ls = []
    for i in range(3):
        top = User.query.filter(User.f_y_record>=0).order_by(User.f_y_record.desc())[i:i+1]
        for u in top:
            top3ls.append(u.username)
            top3ls.append(u.f_y_record)
    return render_template('flappy_yuras.html', top1name=top3ls[0], top1score=top3ls[1],
                                                top2name=top3ls[2], top2score=top3ls[3],
                                                top3name=top3ls[4], top3score=top3ls[5])


#User Login
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        # get forms  fields
        username = request.form['username']
        password = request.form['password']
        remember_me = request.form.get('remember_me')
        if remember_me is not None:
            remember_me = True
        else:
            remember_me = False
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash(u'Курлык, неправильный логин или пароль', 'danger')
            return redirect(url_for('login'))
        # Passed
        session['logged_in'] = True
        session['username'] = username
        login_user(user, remember=remember_me)
        flash(u'you are now logged in', 'success')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title=u'залагинся')


# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out', 'success')
    return redirect(url_for('home'))


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is not None:
            flash(u'Уже кто-то назвал себя так', 'danger')
            return redirect(url_for('register'))
        else:
            if captcha.validate():
                u = User(username=username)
                u.set_password(password)
                db.session.add(u)
                db.session.commit()
                flash('Congratulations, you are now a registred user!', 'success')
                return redirect(url_for('login'))
            else:
                flash('captcha is not right', 'danger')
                return redirect(url_for('register'))
    return render_template('register.html', title=u'зарегай себя')

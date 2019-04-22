#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    user_answers = db.relationship('Answer', backref='author', lazy='dynamic')
    f_y_record = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<id: {}, username: {}, f_y_record: {}>'.format(
                self.id, self.username, self.f_y_record)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'id = {}, body = {}, time = {}, user id = {}'.format(
                self.id, self.body, self.timestamp, self.user_id)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    answers = db.relationship('Answer', backref='qstion', lazy='dynamic')

    def __repr__(self):
        return '<id: {}, body: {}>, answers: {}'.format(
                self.id, self.body, self.answers )


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ans = db.Column(db.Boolean)

    def __repr__(self):
        return '<id: {}, question_id: {}, user_id: {}, ans: {}>'.format(
                self.id, self.question_id, self.user_id, self.ans)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

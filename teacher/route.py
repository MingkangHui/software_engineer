from flask import render_template, redirect, url_for, request, escape
from app import app, session
import sqlite3
from werkzeug.security import check_password_hash


@app.route('/teacher/index')
def teacherindex():
    return render_template("teacherindex.html")


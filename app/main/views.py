from flask import render_template, request, redirect, url_for, abort
from . import main
from ..requests import get_quotes, get_quotes1, get_quotes2, get_quotes3, get_quotes4
from flask_login import login_required, current_user
from app.models import User, NewBlog
from . forms import UpdateProfile, BlogForm
from app import db, photos
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title="Le Blunt"
    randomquotes = get_quotes()
    randomquotes1 = get_quotes1()
    randomquotes2 = get_quotes2()
    randomquotes3 = get_quotes3()
    randomquotes4 = get_quotes4()

    return render_template('index.html', title=title, randomquotes = randomquotes, randomquotes1=randomquotes1, randomquotes2=randomquotes2, randomquotes3=randomquotes3, randomquotes4=randomquotes4)

@main.route('/userblogpage', methods = ['GET', 'POST'])
@login_required
def userblogpage():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 

    blog_body = NewBlog.query.all()

    return render_template('userblogpage.html', blog_body=blog_body)

#Display profile
@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#Update Profile

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def updateprofile(uname):

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template("profile/update.html", form = form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def updateppic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:

        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname=uname))


# Blog form

@main.route('/createblog', methods = ['GET', 'POST'])
@login_required
def createblog():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 
    form = BlogForm() 
    if form.validate_on_submit():


        upblog = NewBlog( blogtitle = form.title.data, myblog = form.name.data, author = form.author.data)

        db.session.add(upblog)
        db.session.commit()

        return redirect(url_for('main.userblogpage'))

    return render_template('createblog.html', blog_form = form)



@expose('/admin', methods=['GET', 'POST'])
def administrator():
    blog_body = NewBlog.query.all()

    return render_template('userblogpage.html', blog_body=blog_body)







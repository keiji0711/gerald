from flask import Blueprint, render_template,request,redirect, url_for

bp = Blueprint('members',__name__, template_folder='members/templates')

@bp.route('/members/member_dashboard')
def member_dashboard():
    return render_template('members/member_dashboard.html')

@bp.route('/members/member_announcements')
def member_announcements():
    return render_template('members/member_announcement.html')




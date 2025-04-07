from flask import Blueprint, render_template,request,redirect, url_for

bp = Blueprint('admin',__name__, template_folder='admin/templates')

@bp.route('/admin/admin_dashboard')
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')

@bp.route('/admin/organizations')
def list_organizations():
    return render_template('admin/admin_org_list.html')

@bp.route('/admin/officers')
def list_officers():
    return render_template('admin/admin_officer_list.html')

@bp.route('/admin/admin_org_archived')
def archived_org():
    return render_template('admin/admin_archived_org.html')

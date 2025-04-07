from flask import Blueprint,render_template,request,redirect,url_for,jsonify

bp = Blueprint('officers',__name__,template_folder='officers/templates')

pending_members = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Johnson"},
]

events = [
    {"id": 1, "title": "Club Orientation", "date": "2025-04-10", "time": "10:00 AM", "location": "Hall A", "description": "Welcome event for new members."},
    {"id": 2, "title": "Tech Workshop", "date": "2025-03-28", "time": "2:00 PM", "location": "Lab 3", "description": "Hands-on coding session."},
]

rsvps = []  # List to store RSVPs

@bp.context_processor
def inject_pending_count():
    """Make pending_count available in all templates (base.html)"""
    return dict(pending_count=len(pending_members), pending_members=pending_members)

@bp.route("/dashboard")
def dashboard():
    return render_template("officers/dashboard.html")

@bp.route('/members')
def members():
    return render_template('officers/members.html')

@bp.route('/approve/<int:member_id>', methods=['POST'])
def approve_member(member_id):
    """Approve a pending member (remove from pending list without reloading)"""
    global pending_members
    pending_members = [m for m in pending_members if m["id"] != member_id]
    return jsonify({"success": True, "pending_count": len(pending_members)})

@bp.route('/reject/<int:member_id>', methods=['POST'])
def reject_member(member_id):
    """Reject a pending member (remove from pending list without reloading)"""
    global pending_members
    pending_members = [m for m in pending_members if m["id"] != member_id]
    return jsonify({"success": True, "pending_count": len(pending_members)})


@bp.route('/announcements')
def announcements_page():
    sample_announcements = [
        {"id": 1, "title": "Club Meeting", "date": "2025-04-01", "type": "Important", "details": "Meeting at 5 PM in Room 101."},
        {"id": 2, "title": "Event Reminder", "date": "2025-04-05", "type": "Reminder", "details": "Don't forget about the upcoming hackathon!"},
        {"id": 3, "title": "General Update", "date": "2025-04-10", "type": "General", "details": "New club T-shirts are available now."}
    ]
    return render_template("officers/announcements.html", announcements=sample_announcements)

@bp.route('/create_announcement', methods=['POST'])
def create_announcement():
    title = request.form.get('title')
    date = request.form.get('date')
    announcement_type = request.form.get('type')
    details = request.form.get('details')

    # Fake database save (replace with actual DB logic later)
    print(f"New Announcement: {title}, {date}, {announcement_type}, {details}")

    # Redirect back to the announcements page
    return redirect(url_for('officers/announcements_page'))



@bp.route("/finances")
def finances():
    # Dummy Data for Display
    total_income = 5000
    total_expenses = 2000
    transactions = [
        {"date": "2025-03-28", "description": "Salary", "type": "income", "amount": 3000},
        {"date": "2025-03-25", "description": "Groceries", "type": "expense", "amount": 200},
        {"date": "2025-03-20", "description": "Freelance Work", "type": "income", "amount": 2000},
        {"date": "2025-03-18", "description": "Electricity Bill", "type": "expense", "amount": 500}
    ]

    return render_template("officers/finances.html", total_income=total_income, total_expenses=total_expenses, transactions=transactions)

@bp.route("/add_transaction", methods=["POST"])
def add_transaction():
    return "Transaction added (dummy response)", 200

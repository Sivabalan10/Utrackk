from flask import Flask,render_template,redirect,request,jsonify,url_for

app = Flask(__name__)

# home page 
@app.route("/")
def homepage():
    return "Login page"
    
# Login call
@app.route("/login")
def login():
    return "home page"
# Logout call
@app.route("/logout")
def logout():
    return redirect('/')

# Sign_up page
@app.route("/sign_up")
def sign_up():
    return "sign_up page"

# Storing account
@app.route("/sign_up/account_added")
def account_added():
    return redirect('/')

# group_joined
@app.route("/group_joined")
def group_joined():
    return "list the group"

# group details
@app.route("/groups_joined/group_details")
def group_details():
    return "dynammic info about group"

# other members
@app.route("/groups_joined/group_details/other_members")
def other_members():
    return "other members page"

# join group
@app.route("/join_group")
def join_group():
    return "listing groups using search with join icon"

# complaint box page
@app.route("/complaint_box")
def complaint_box():
    return "complaint box form"

# mark entering 
@app.route("/enter_secured_mark")
def enter_secured_mark():
    return "mark entering page"

#profile page
@app.route("/profile")
def profile():
    return "profile with edit icon interms of form (easy approach)"

if  __name__ == "__main__":
    app.run(debug=True)

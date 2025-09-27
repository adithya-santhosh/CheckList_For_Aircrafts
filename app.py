import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-and-secure-key-change-me'

# --- START: Corrected Data Structures ---

def load_checklists_from_excel(file_path='Aircraft_Preflight_Checklist.xlsx'):
    try:
        df = pd.read_excel(file_path)
        df['FullChecklistItem'] = df['Checklist Item'].astype(str) + ': ' + df['Action'].astype(str)
        checklists_dict = {}
        for model, group in df.groupby('Aircraft'):
            checklists_dict[model] = {
                "items": group['FullChecklistItem'].tolist(),
                "image": group['ImageFile'].iloc[0]
            }
        return checklists_dict
    except Exception as e:
        print(f"Error loading checklists from Excel: {e}")
        return {
            "Cessna 172": {"items": ["Sample Item 1", "Sample Item 2"], "image": "cessna_172.png"},
            "Piper PA-28": {"items": ["Sample Item A", "Sample Item B"], "image": "piper_pa28.png"}
        }

checklists = load_checklists_from_excel()

USERS = {'admin': 'password123'}

# ✅ THIS IS THE CORRECTED SECTION
# The fleet must be a list of dictionaries, each with 'name' and 'image'
airlines = {
    "IndiGo": {
        "logo": "indigo.png", 
        "fleet": [
            {"name": "Airbus A320", "image": "airbusa320.jpeg"},
            {"name": "ATR 72", "image": "atr72.jpeg"}
        ]
    },
    "Air India": {
        "logo": "airindia.png", 
        "fleet": [
            {"name": "Boeing 777", "image": "boeing777.jpeg"},
            {"name": "Airbus A350", "image": "airbusa350.jpeg"}
        ]
    },
    "Vistara": {
        "logo": "vistara.png",
        "fleet": [
            {"name": "Boeing 787 Dreamliner", "image": "boeing787.jpeg"},
            {"name": "Airbus A321neo", "image": "airbus_a321neo.jpeg"}
        ]
    }
}
# --- END: Corrected Data Structures ---


# --- Routes (No changes needed here) ---

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# (All other routes like /, /login, /dashboard, etc., remain exactly the same)
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            session['username'] = username
            flash('You were successfully logged in!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/checklists')
@login_required
def available_checklists():
    return render_template('available_checklists.html', checklists=checklists, active_page='checklists')

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    selected_aircraft = request.form.get('aircraft')
    return redirect(url_for('success', aircraft=selected_aircraft))

@app.route('/success')
@login_required
def success():
    aircraft_model = request.args.get('aircraft')
    checklist_data = checklists.get(aircraft_model, {"items": [], "image": ""})
    return render_template('checklist.html', aircraft=aircraft_model, items=checklist_data['items'], active_page='checklists')

@app.route('/airlines')
@login_required
def airlines_list():
    return render_template('airlines.html', airlines=airlines, active_page='airlines')

@app.route('/airlines/<airline_name>')
@login_required
def airline_details(airline_name):
    airline = airlines.get(airline_name)
    if not airline:
        return "Airline not found", 404
    return render_template('airline_details.html', airline_name=airline_name, airline_data=airline, active_page='airlines')

if __name__ == '__main__':
    app.run(debug=True)
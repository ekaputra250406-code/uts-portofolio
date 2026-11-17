from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'rahasia_super_aman_hidayat' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- MODEL DATABASE ---
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(200), nullable=False)

# --- ROUTE HALAMAN PUBLIK ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    all_projects = Project.query.all()
    # PERHATIKAN BARIS INI: Disini saya ubah menjadi 'project.html' (tanpa s)
    return render_template('project.html', projects=all_projects)

@app.route('/skills')
def skills():
    all_skills = Skill.query.all()
    return render_template('skills.html', skills=all_skills)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- ROUTE LOGIN & ADMIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Username atau Password salah!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/admin')
def admin_dashboard():
    if not session.get('logged_in'): return redirect(url_for('login'))
    all_skills = Skill.query.all()
    all_projects = Project.query.all()
    return render_template('admin.html', skills=all_skills, projects=all_projects)

# ==========================================
# CRUD PROJECTS
# ==========================================
@app.route('/admin/project/add', methods=['GET', 'POST'])
def add_project():
    if not session.get('logged_in'): return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_project = Project(
            title=request.form['title'],
            role=request.form['role'],
            year=request.form['year'],
            description=request.form['description'],
            tech_stack=request.form['tech_stack']
        )
        db.session.add(new_project)
        db.session.commit()
        flash('Proyek berhasil ditambahkan!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('form_project.html', action="Tambah", project=None)

@app.route('/admin/project/edit/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    if not session.get('logged_in'): return redirect(url_for('login'))
    
    project = db.session.get(Project, id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.role = request.form['role']
        project.year = request.form['year']
        project.description = request.form['description']
        project.tech_stack = request.form['tech_stack']
        db.session.commit()
        flash('Proyek berhasil diupdate!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('form_project.html', action="Edit", project=project)

@app.route('/admin/project/delete/<int:id>')
def delete_project(id):
    if not session.get('logged_in'): return redirect(url_for('login'))
    project = db.session.get(Project, id)
    db.session.delete(project)
    db.session.commit()
    flash('Proyek berhasil dihapus!', 'success')
    return redirect(url_for('admin_dashboard'))

# ==========================================
# CRUD SKILLS
# ==========================================
@app.route('/admin/skill/add', methods=['GET', 'POST'])
def add_skill():
    if not session.get('logged_in'): return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_skill = Skill(
            name=request.form['name'],
            category=request.form['category'],
            proficiency=int(request.form['proficiency'])
        )
        db.session.add(new_skill)
        db.session.commit()
        flash('Skill berhasil ditambahkan!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('form_skill.html', action="Tambah", skill=None)

@app.route('/admin/skill/edit/<int:id>', methods=['GET', 'POST'])
def edit_skill(id):
    if not session.get('logged_in'): return redirect(url_for('login'))
    
    skill = db.session.get(Skill, id)
    if request.method == 'POST':
        skill.name = request.form['name']
        skill.category = request.form['category']
        skill.proficiency = int(request.form['proficiency'])
        db.session.commit()
        flash('Skill berhasil diupdate!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('form_skill.html', action="Edit", skill=skill)

@app.route('/admin/skill/delete/<int:id>')
def delete_skill(id):
    if not session.get('logged_in'): return redirect(url_for('login'))
    skill = db.session.get(Skill, id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill berhasil dihapus!', 'success')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
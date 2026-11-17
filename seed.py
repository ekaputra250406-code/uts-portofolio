from app import app, db, Skill, Project

def seed_data():
    with app.app_context():
        if Skill.query.first() is None:
            # Data Skills
            skills = [
                Skill(name="HTML5", category="FRONTEND", proficiency=60),
                Skill(name="CSS3", category="FRONTEND", proficiency=55),
                Skill(name="Tailwind CSS", category="FRONTEND", proficiency=50),
                Skill(name="Python", category="BACKEND", proficiency=55),
                Skill(name="Flask", category="BACKEND", proficiency=45),
                Skill(name="SQLite", category="DATABASE", proficiency=40),
                Skill(name="Git", category="TOOLS", proficiency=40),
                Skill(name="Linux", category="TOOLS", proficiency=35),
            ]
            
            # Data Projects (Sesuai portofolio lamamu)
            projects = [
                Project(
                    title="Aplikasi Keuangan", 
                    role="Fullstack Developer", 
                    year="2025", 
                    description="Aplikasi web manajemen keuangan pribadi untuk mencatat pemasukan, pengeluaran, dan laporan secara real-time.", 
                    tech_stack="Python, Flask, SQLite, Tailwind CSS"
                ),
                Project(
                    title="Blog Belajar", 
                    role="Backend Developer", 
                    year="2025", 
                    description="Aplikasi web untuk mencatat pelajaran dan catatan pribadi dengan sistem autentikasi yang aman.", 
                    tech_stack="Python, Flask, SQLite"
                ),
                Project(
                    title="Detektor Jari", 
                    role="Computer Vision Enthusiast", 
                    year="2024", 
                    description="Program eksperimen computer vision untuk mendeteksi dan menghitung jumlah jari menggunakan webcam.", 
                    tech_stack="Python, OpenCV, MediaPipe"
                )
            ]
            
            db.session.add_all(skills + projects)
            db.session.commit()
            print("✅ Data dummy berhasil dimasukkan!")
        else:
            print("⚠️ Database sudah terisi.")

if __name__ == "__main__":
    seed_data()
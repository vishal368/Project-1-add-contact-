from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store submissions in memory
submissions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if name and email and message:
        submissions.append({
            'name': name,
            'email': email,
            'message': message
        })
    return redirect(url_for('submissions_page'))

@app.route('/submissions')
def submissions_page():
    return render_template('submissions.html', submissions=submissions)

@app.route('/delete/<int:index>')
def delete_submission(index):
    if 0 <= index < len(submissions):
        submissions.pop(index)
    return redirect(url_for('submissions_page'))

if __name__ == '__main__':
    app.run(debug=True)
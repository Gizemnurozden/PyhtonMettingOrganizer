from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

meetings = []

@app.route('/')
def index():
    return render_template('index.html', meetings=meetings)

@app.route('/add_meeting', methods=['POST'])
def add_meeting():
    meeting_name = request.form.get('meeting_name')
    date = request.form.get('date')
    time = request.form.get('time')

    if meeting_name and date and time:
        meeting = {'name': meeting_name, 'date': date, 'time': time}
        meetings.append(meeting)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

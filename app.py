from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = "ai-learning-dna-secret-key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mock-test')
def mock_test():
    return render_template('mock-test.html')

@app.route('/mock-result', methods=['POST'])
def mock_result():
    answers = {
        "q1": "stack",
        "q2": "select",
        "q3": "http",
        "q4": "kernel"
    }
    score = 0
    for question, correct_answer in answers.items():
        if request.form.get(question) == correct_answer:
            score += 1
    mock_percentage = round((score / len(answers)) * 100)
    session['mock_percentage'] = mock_percentage
    return render_template('mock-result.html', score=score, total=len(answers), mock_percentage=mock_percentage)

@app.route('/analyze', methods=['POST'])
def analyze():
    name = request.form['name']
    dsa = int(request.form['dsa'])
    dbms = int(request.form['dbms'])
    os_score = int(request.form['os'])
    cn = int(request.form['cn'])
    coding_problems = int(request.form['coding_problems'])
    coding_days = int(request.form['coding_days'])
    github_username = request.form['github_username'].strip()

    # Coding Performance
    problem_score = min(coding_problems / 2, 50)
    consistency_score = (coding_days / 30) * 50
    coding_score = round(problem_score + consistency_score, 2)

    if coding_score >= 80:
        coding_status = "Strong Coder"
    elif coding_score >= 60:
        coding_status = "Developing Coder"
    else:
        coding_status = "Needs More Practice"

    # Overall Score
    overall_score = round((dsa + dbms + os_score + cn) / 4, 2)
    mock_percentage = session.get('mock_percentage', 0)
    combined_score = round((overall_score + mock_percentage + coding_score) / 3, 2)

    # Subject Scores
    scores = {
        "DSA": dsa,
        "DBMS": dbms,
        "Operating System": os_score,
        "Computer Networks": cn
    }

    strength = max(scores, key=scores.get)
    weakness = min(scores, key=scores.get)

    # Performance Classification
    def classify(score):
        if score >= 80:
            return "Strong"
        elif score >= 60:
            return "Average"
        else:
            return "Weak"

    dsa_status = classify(dsa)
    dbms_status = classify(dbms)
    os_status = classify(os_score)
    cn_status = classify(cn)

    # Learning DNA
    if combined_score >= 85:
        learning_dna = "High Performer"
        recommendation = "You are doing excellent. Focus on advanced problem solving and interview preparation."
    elif combined_score >= 70:
        learning_dna = "Consistent Learner"
        recommendation = f"You are performing well. Improve {weakness} to become a top performer."
    elif combined_score >= 50:
        learning_dna = "Potential Performer"
        recommendation = f"You have good potential. Spend more time on {weakness} and practice regularly."
    else:
        learning_dna = "Needs Focus"
        recommendation = f"Start with fundamentals of {weakness} and take weekly mock tests."

    # GitHub API
    github_data = {}
    repos_data = []
    github_error = ""

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI-Learning-DNA"
    }

    github_url = f"https://api.github.com/users/{github_username}"

    try:
        github_response = requests.get(github_url, headers=headers, timeout=10)

        if github_response.status_code == 200:
            github_data = github_response.json()

            repos_url = f"https://api.github.com/users/{github_username}/repos?per_page=100&sort=updated"
            repos_response = requests.get(repos_url, headers=headers, timeout=10)

            if repos_response.status_code == 200:
                repos_data = repos_response.json()
            else:
                github_error = f"Repositories API error: {repos_response.status_code}"
        else:
            github_error = f"GitHub profile API error: {github_response.status_code}"

    except requests.RequestException as error:
        github_error = "Unable to connect to GitHub"

    return render_template('dashboard.html', name=name, dsa=dsa, dbms=dbms, os_score=os_score, cn=cn, overall_score=overall_score, strength=strength, weakness=weakness, recommendation=recommendation, dsa_status=dsa_status, dbms_status=dbms_status, os_status=os_status, cn_status=cn_status, coding_score=coding_score, coding_status=coding_status, coding_problems=coding_problems, coding_days=coding_days, github_username=github_username, github_data=github_data, repos_data=repos_data, github_error=github_error, learning_dna=learning_dna, mock_percentage=mock_percentage, combined_score=combined_score)

@app.route('/github')
def github():
    username = "archi14052005-collab"
    url = f"https://api.github.com/users/{username}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI-Learning-DNA"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "username": data["login"],
                "name": data["name"],
                "followers": data["followers"],
                "following": data["following"],
                "repositories": data["public_repos"],
                "profile": data["html_url"]
            }

        return {"error": f"GitHub API error: {response.status_code}"}

    except requests.RequestException:
        return {"error": "Unable to connect to GitHub"}

if __name__ == '__main__':
    app.run(debug=True)
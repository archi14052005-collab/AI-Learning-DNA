
from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "ai-learning-dna-secret-key"


def get_github_data(github_username):
    github_data = {}
    repos_data = []
    github_error = ""

    if not github_username:
        return github_data, repos_data, "No GitHub username provided."

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI-Learning-DNA"
    }

    try:
        response = requests.get(
            f"https://api.github.com/users/{github_username}",
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            github_data = response.json()
            repos_response = requests.get(
                f"https://api.github.com/users/{github_username}/repos?per_page=100&sort=updated",
                headers=headers,
                timeout=10
            )

            if repos_response.status_code == 200:
                repos_data = repos_response.json()
            else:
                github_error = "Unable to load GitHub repositories."
        else:
            github_error = "GitHub profile not found."

    except requests.RequestException:
        github_error = "Unable to connect to GitHub."

    return github_data, repos_data, github_error


def classify(score):
    if score >= 80:
        return "Strong"
    elif score >= 60:
        return "Average"
    return "Weak"


def build_dashboard_data():
    if "student" not in session:
        return None

    student = session["student"]
    name = student["name"]
    dsa = student["dsa"]
    dbms = student["dbms"]
    os_score = student["os_score"]
    cn = student["cn"]
    coding_problems = student["coding_problems"]
    coding_days = student["coding_days"]
    github_username = student["github_username"]

    problem_score = min(coding_problems / 2, 50)
    consistency_score = min((coding_days / 30) * 50, 50)
    coding_score = round(problem_score + consistency_score, 2)

    if coding_score >= 80:
        coding_status = "Strong Coder"
    elif coding_score >= 60:
        coding_status = "Developing Coder"
    else:
        coding_status = "Needs More Practice"

    overall_score = round((dsa + dbms + os_score + cn) / 4, 2)

    mock_attempted = session.get("mock_attempted", False)
    mock_percentage = session.get("mock_percentage", 0)
    mock_subject_scores = session.get("mock_subject_scores", {})

    if mock_attempted:
        combined_score = round(
            (overall_score + mock_percentage + coding_score) / 3, 2
        )
    else:
        combined_score = round((overall_score + coding_score) / 2, 2)

    scores = {
        "DSA": dsa,
        "DBMS": dbms,
        "Operating System": os_score,
        "Computer Networks": cn
    }

    strength = max(scores, key=scores.get)
    weakness = min(scores, key=scores.get)

    dsa_status = classify(dsa)
    dbms_status = classify(dbms)
    os_status = classify(os_score)
    cn_status = classify(cn)

    if combined_score >= 85:
        learning_dna = "High Performer"
        recommendation = (
            "You are doing well. Focus on advanced problem solving "
            "and interview preparation."
        )
    elif combined_score >= 70:
        learning_dna = "Consistent Learner"
        recommendation = (
            f"You are performing well. Improve {weakness} "
            "to strengthen your fundamentals."
        )
    elif combined_score >= 50:
        learning_dna = "Potential Performer"
        recommendation = (
            f"You have good potential. Spend more time on {weakness} "
            "and practice regularly."
        )
    else:
        learning_dna = "Needs Focus"
        recommendation = (
            f"Start with the fundamentals of {weakness} "
            "and take regular mock tests."
        )

    github_data, repos_data, github_error = get_github_data(
        github_username
    )

    return {
        "name": name,
        "dsa": dsa,
        "dbms": dbms,
        "os_score": os_score,
        "cn": cn,
        "overall_score": overall_score,
        "strength": strength,
        "weakness": weakness,
        "recommendation": recommendation,
        "dsa_status": dsa_status,
        "dbms_status": dbms_status,
        "os_status": os_status,
        "cn_status": cn_status,
        "coding_score": coding_score,
        "coding_status": coding_status,
        "coding_problems": coding_problems,
        "coding_days": coding_days,
        "github_username": github_username,
        "github_data": github_data,
        "repos_data": repos_data,
        "github_error": github_error,
        "learning_dna": learning_dna,
        "mock_percentage": mock_percentage,
        "mock_attempted": mock_attempted,
        "mock_subject_scores": mock_subject_scores,
        "combined_score": combined_score
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        name = request.form["name"].strip()
        dsa = int(request.form["dsa"])
        dbms = int(request.form["dbms"])
        os_score = int(request.form["os"])
        cn = int(request.form["cn"])
        coding_problems = int(request.form["coding_problems"])
        coding_days = int(request.form["coding_days"])
        github_username = request.form["github_username"].strip()

        if not name:
            return "Please enter your name."

        scores = [dsa, dbms, os_score, cn]

        if any(score < 0 or score > 100 for score in scores):
            return "Subject scores must be between 0 and 100."

        if coding_problems < 0 or coding_days < 0:
            return "Coding values cannot be negative."

        if coding_days > 30:
            return "Coding days cannot exceed 30."

        session["student"] = {
            "name": name,
            "dsa": dsa,
            "dbms": dbms,
            "os_score": os_score,
            "cn": cn,
            "coding_problems": coding_problems,
            "coding_days": coding_days,
            "github_username": github_username
        }

        dashboard_data = build_dashboard_data()
        return render_template("dashboard.html", **dashboard_data)

    except (ValueError, KeyError):
        return "Please enter valid information in all fields."


@app.route("/dashboard")
def dashboard():
    dashboard_data = build_dashboard_data()

    if dashboard_data is None:
        return redirect(url_for("home"))

    return render_template("dashboard.html", **dashboard_data)


@app.route("/mock-test")
def mock_test():
    if "student" not in session:
        return redirect(url_for("home"))

    return render_template("mock-test.html")


@app.route("/mock-result", methods=["POST"])
def mock_result():
    if "student" not in session:
        return redirect(url_for("home"))

    answers = {
        "q1": "ologn",
        "q2": "dijkstra",
        "q3": "stack",
        "q4": "where",
        "q5": "inner",
        "q6": "redundancy",
        "q7": "deadlock",
        "q8": "requeue",
        "q9": "paging",
        "q10": "reliable",
        "q11": "names",
        "q12": "404"
    }

    subject_questions = {
        "DSA": ["q1", "q2", "q3"],
        "DBMS": ["q4", "q5", "q6"],
        "OS": ["q7", "q8", "q9"],
        "CN": ["q10", "q11", "q12"]
    }

    score = sum(
        1 for question, answer in answers.items()
        if request.form.get(question) == answer
    )

    total = len(answers)
    mock_percentage = round((score / total) * 100)

    mock_subject_scores = {}

    for subject, questions in subject_questions.items():
        subject_correct = sum(
            1 for question in questions
            if request.form.get(question) == answers[question]
        )
        mock_subject_scores[subject] = round(
            (subject_correct / len(questions)) * 100
        )

    session["mock_percentage"] = mock_percentage
    session["mock_attempted"] = True
    session["mock_subject_scores"] = mock_subject_scores

    return render_template(
        "mock-result.html",
        score=score,
        total=total,
        mock_percentage=mock_percentage,
        mock_subject_scores=mock_subject_scores
    )


@app.route("/github")
def github():
    username = session.get("student", {}).get(
        "github_username", "archi14052005-collab"
    )

    github_data, repos_data, github_error = get_github_data(username)

    if github_data:
        return {
            "username": github_data.get("login"),
            "name": github_data.get("name"),
            "followers": github_data.get("followers"),
            "following": github_data.get("following"),
            "repositories": github_data.get("public_repos"),
            "profile": github_data.get("html_url")
        }

    return {"error": github_error}


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)


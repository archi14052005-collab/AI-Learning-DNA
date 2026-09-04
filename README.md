# 🧠 AI Learning DNA

AI Learning DNA is a personalized student performance dashboard that combines academic performance, GitHub activity, and mock test results to provide a simple learning analysis.

## ✨ Features

- 📊 Academic performance analysis
- 🐙 GitHub profile integration
- 📦 GitHub repository information
- 📝 Technical mock test
- 🧮 Automatic mock test score calculation
- 🧠 Learning DNA analysis
- 📈 Personalized learning insights
- 🔐 Session-based logout
- 💻 Clean and responsive dashboard

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- GitHub API
- Jinja2

## 🔄 Project Flow

User → Home Page → Enter Academic Scores → Analyze Performance → Dashboard

Dashboard → Academic Score  
Dashboard → GitHub Profile  
Dashboard → Mock Test → Submit Test → Mock Test Result → Dashboard  
Dashboard → Learning DNA Analysis → Personalized Learning Insights

## 🐙 GitHub Integration

The project integrates with the GitHub API to display basic GitHub profile information.

The dashboard displays:

- GitHub username
- Number of repositories
- Followers
- Following
- Profile name
- GitHub repository information

This helps combine coding activity with academic performance.

## 📝 Mock Test

The application includes a technical mock test to evaluate the student's basic technical knowledge.

The test includes questions related to:

- Data Structures
- DBMS
- Computer Networks
- Operating Systems

The application automatically checks the submitted answers and calculates the mock test score.

### Mock Test Flow

Start Mock Test → Answer Questions → Submit Test → Calculate Score → Display Result → Return to Dashboard

## 🧠 Learning DNA Analysis

The Learning DNA section provides a personalized learning analysis based on the student's performance.

It combines:

- Academic scores
- Mock test performance
- Coding activity
- GitHub activity

The analysis helps identify areas of strength and areas that may need improvement.

## 📊 Dashboard

The dashboard brings important information together in one place.

It includes:

- Academic Score
- GitHub Profile
- GitHub Repositories
- Mock Test Score
- Learning DNA Analysis
- Personalized Learning Insights

## 🚀 How to Run

### 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the project folder

cd AI-Learning-DNA

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the virtual environment

For Windows:

venv\Scripts\activate

### 5. Install required packages

pip install flask requests

### 6. Run the application

python app.py

### 7. Open the application

http://127.0.0.1:5000/

## 📁 Project Structure

AI-Learning-DNA/
├── app.py
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── mock-test.html
│   └── mock-result.html
├── static/
│   └── style.css
└── README.md

## 📸 Project Screenshots

Screenshots of the dashboard, Learning DNA analysis, and mock test result will be added after final testing.

## 🔮 Future Enhancements

- 🤖 AI-based personalized recommendations
- 📊 Advanced performance analytics
- 📈 Progress tracking over time
- 📝 More mock tests
- 📚 Subject-wise performance analysis
- 🐙 Detailed GitHub activity analysis
- 🗄️ Database integration
- 🎯 Personalized learning roadmap

## 🎯 Project Purpose

AI Learning DNA demonstrates how academic performance, coding activity, and assessment results can be combined into a single personalized student dashboard.

The main goal of the project is to help students understand their current performance and identify areas where they can improve.

## 👩‍💻 Developed As a Student Project

AI Learning DNA is developed as a student project to demonstrate skills in Python, Flask, web development, API integration, and basic performance analytics.
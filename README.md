# 🧠 AI Learning DNA

AI Learning DNA is a personalized student performance dashboard developed using Python, Flask, HTML, CSS, and JavaScript. It combines academic performance, GitHub profile information, and technical mock test results to help students understand their performance and identify areas for improvement.

The project demonstrates frontend and backend web development, API integration, session management, and basic performance analysis through an interactive dashboard.

## ✨ Key Features

* 📊 **Academic Performance Analysis** – Analyze academic scores through a personalized dashboard.
* 🐙 **GitHub Profile Integration** – Fetch GitHub profile information using the GitHub API.
* 📦 **GitHub Repository Information** – Display repository details and coding profile information.
* 📝 **12-Question Technical Mock Test** – Practice technical questions from four core computer science subjects.
* 🧮 **Automatic Score Calculation** – Evaluate submitted answers and calculate the mock test score.
* 📚 **Subject-Wise Performance** – View results for individual subjects.
* 🧠 **Learning DNA Analysis** – Review performance-based learning insights.
* 📈 **Personalized Learning Insights** – Identify strengths and areas that may need improvement.
* 🔐 **Session-Based Logout** – Manage the user session through logout functionality.
* 💻 **Responsive Dashboard** – Use the application through a clean, responsive interface.

## 🛠️ Technologies Used

| Technology      | Purpose                                              |
| --------------- | ---------------------------------------------------- |
| Python          | Backend programming and application logic            |
| Flask           | Backend web framework and routing                    |
| HTML            | Structure of web pages                               |
| CSS             | Styling and responsive design                        |
| JavaScript      | Frontend interactions                                |
| Jinja2          | Dynamic HTML rendering                               |
| GitHub REST API | Retrieving GitHub profile and repository information |

## 📝 Technical Mock Test

The application includes a technical mock test with **12 questions across four subjects**.

* **Data Structures and Algorithms (DSA):** 3 questions
* **Database Management Systems (DBMS):** 3 questions
* **Operating Systems (OS):** 3 questions
* **Computer Networks (CN):** 3 questions

### Mock Test Workflow

1. Open the Mock Test section from the dashboard.
2. Answer the technical questions.
3. Submit the test.
4. The application checks the answers and calculates the score.
5. View the overall result and subject-wise performance.
6. Return to the dashboard to review learning insights.

## 🐙 GitHub Integration

AI Learning DNA uses the GitHub API to retrieve basic public profile information.

The dashboard can display:

* GitHub username
* Profile name
* Number of repositories
* Followers and following
* Repository information

This integration brings coding profile information together with academic and mock test performance.

## 🧠 Learning DNA Analysis

The Learning DNA section provides a simple analysis of the student's available performance information.

It brings together:

* Academic scores
* Mock test performance
* GitHub profile and repository information

These insights help students review their current performance, recognize areas of strength, and identify subjects that may require additional practice.

## 📊 Dashboard Overview

The dashboard organizes the main project features in one place:

* Academic Score
* GitHub Profile
* GitHub Repositories
* Technical Mock Test
* Mock Test Results
* Learning DNA Analysis
* Personalized Learning Insights

## 🔄 Project Workflow

```text
Home Page
    ↓
Enter Academic Details
    ↓
Analyze Performance
    ↓
Dashboard
    ├── Academic Performance
    ├── GitHub Profile and Repositories
    ├── Technical Mock Test
    │       ↓
    │   Answer Questions
    │       ↓
    │   Submit Test
    │       ↓
    │   Calculate Score
    │       ↓
    │   View Subject-Wise Results
    └── Learning DNA Analysis
            ↓
       Personalized Insights
```

## 🚀 How to Run the Project

### Prerequisites

* Python installed on your system
* Git installed on your system
* Internet connection for GitHub API requests

### 1. Clone the Repository

```bash
git clone https://github.com/archi14052005-collab/AI-Learning-DNA.git
```

### 2. Open the Project Folder

```bash
cd AI-Learning-DNA
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install flask requests
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open the Application

Open your browser and visit:

http://127.0.0.1:5000/

## 📁 Project Structure

```text
AI-Learning-DNA/
│
├── app.py
├── student_data.csv
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── mock-test.html
│   └── mock-result.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## 🔮 Future Enhancements

* 🤖 Machine learning-based student performance prediction
* 📊 Advanced performance analytics and visualizations
* 📈 Student progress tracking over time
* 📝 Additional subject-wise mock tests
* 🐙 Detailed GitHub activity analysis
* 🗄️ Database integration for persistent student records
* 🎯 Personalized learning roadmaps

## 🎯 Project Objective

The objective of AI Learning DNA is to bring academic performance, technical assessment results, and coding profile information into a single dashboard. It aims to help students review their performance and understand where they can focus their learning efforts.

## 👩‍💻 About the Project

AI Learning DNA is a student project developed using **Python, Flask, HTML, CSS, and JavaScript**. It demonstrates practical skills in frontend web development, backend programming, responsive interface design, REST API integration, session management, and basic student performance analysis.

The project provides hands-on experience in building a web application that combines multiple features through a single interactive dashboard.

## 🔗 GitHub Repository

[View AI Learning DNA on GitHub](https://github.com/archi14052005-collab/AI-Learning-DNA)

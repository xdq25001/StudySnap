# StudySnap

StudySnap is a study-tracking dashboard that helps students keep track of their study habits, monitor their confidence, and identify subjects that may need more attention.

## Features

* Add study sessions with a date, subject, topic, study time, and confidence level
* Track total study time
* Calculate average confidence across study sessions
* Set and track a weekly study goal
* Track consecutive study days with a study streak
* Visualize study time by subject
* Visualize average confidence by subject
* View study time over time
* Generate an automatic insight based on the subject with the lowest average confidence
* View all saved study sessions in an interactive table

## Technologies

* Python
* Pandas
* Streamlit
* Matplotlib
* CSV

### app.py

The main Streamlit dashboard. Users can add study sessions and view their study statistics, weekly goals, streaks, visualizations, and insights.

### analyze.py

Uses Pandas to analyze study session data and generate summaries and visualizations.

### main.py

A command-line version of the study tracker that allows users to record study sessions.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/xdq25001/StudySnap.git
cd StudySnap
```

### 2. Install the required libraries

```bash
pip install pandas matplotlib streamlit
```

### 3. Start the dashboard

```bash
streamlit run app.py
```

The Streamlit dashboard will open in your browser.

## How It Works

StudySnap stores study sessions in a CSV file. Each session contains:

* Date
* Subject
* Topic
* Study time in minutes
* Confidence level from 1–5

Pandas is used to group and analyze the collected data. StudySnap uses this information to calculate study totals, confidence averages, weekly progress, study streaks, and subject-level insights.

##

import streamlit as st
import pandas as pd
import os
from datetime import date

filename = "study_sessions.csv"

st.title("📚 StudySnap")
st.write("Track your study habits and see where you can improve.")

if not os.path.exists(filename):
    df = pd.DataFrame(
        columns=["Date", "Subject", "Topic", "Minutes", "Confidence"]
    )
    df.to_csv(filename, index=False)

df = pd.read_csv(filename)

st.header("➕ Add Study Session")

session_date = st.date_input("Date", date.today())
subject = st.text_input("Subject")
topic = st.text_input("Topic")
minutes = st.number_input(
    "Study time (minutes)",
    min_value=1,
    step=5
)
confidence = st.slider(
    "Confidence (1-5)",
    1,
    5,
    3
)

if st.button("Save Session"):

    if subject and topic:
        new_session = pd.DataFrame({
            "Date": [session_date],
            "Subject": [subject],
            "Topic": [topic],
            "Minutes": [minutes],
            "Confidence": [confidence]
        })

        new_session.to_csv(
            filename,
            mode="a",
            header=False,
            index=False
        )

        st.success("Study session saved! 📚")

        df = pd.read_csv(filename)

    else:
        st.warning("Please enter a subject and topic.")


if len(df) > 0:

    df["Date"] = pd.to_datetime(df["Date"])

    total_minutes = df["Minutes"].sum()
    average_confidence = df["Confidence"].mean()

    # -------------------------
    # Summary Metrics
    # -------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Study Time",
            f"{total_minutes // 60}h {total_minutes % 60}m"
        )

    with col2:
        st.metric(
            "Average Confidence",
            f"{average_confidence:.1f}/5"
        )

    # Calculate study streak
    study_dates = set(df["Date"].dt.date)

    current_day = date.today()
    streak = 0

    while current_day in study_dates:
        streak += 1
        current_day = current_day - pd.Timedelta(days=1)

    with col3:
        st.metric(
            "🔥 Study Streak",
            f"{streak} days"
        )

    # -------------------------
    # Weekly Goal
    # -------------------------

    st.header("🎯 Weekly Goal")

    weekly_goal = st.number_input(
        "Weekly study goal (hours)",
        min_value=1,
        value=10,
        step=1
    )

    today = pd.Timestamp.today()

    start_of_week = today - pd.Timedelta(
        days=today.weekday()
    )

    this_week = df[
        df["Date"] >= start_of_week
    ]

    weekly_minutes = this_week["Minutes"].sum()

    weekly_hours = weekly_minutes / 60

    progress = min(
        weekly_hours / weekly_goal,
        1.0
    )

    st.progress(progress)

    st.write(
        f"**{weekly_hours:.1f} / {weekly_goal} hours** this week"
    )

    if weekly_hours >= weekly_goal:

        st.success(
            "🎉 You reached your weekly goal!"
        )

    else:

        remaining = weekly_goal - weekly_hours

        st.info(
            f"You're {remaining:.1f} hours away "
            f"from your weekly goal."
        )

    # -------------------------
    # Study Time by Subject
    # -------------------------

    st.header("📊 Study Time by Subject")

    subject_time = df.groupby(
        "Subject"
    )["Minutes"].sum()

    st.bar_chart(subject_time)

    # -------------------------
    # Confidence by Subject
    # -------------------------

    st.header("📈 Confidence by Subject")

    confidence_by_subject = df.groupby(
        "Subject"
    )["Confidence"].mean()

    st.bar_chart(confidence_by_subject)

    # -------------------------
    # StudySnap Insight
    # -------------------------

    lowest_confidence = confidence_by_subject.idxmin()

    lowest_score = confidence_by_subject.min()

    st.header("💡 StudySnap Insight")

    st.info(
        f"Your lowest average confidence is in "
        f"{lowest_confidence} "
        f"({lowest_score:.1f}/5). "
        f"Consider spending some extra study time "
        f"on this subject."
    )

    # -------------------------
    # Study Time Over Time
    # -------------------------

    st.header("📅 Study Time Over Time")

    daily_study = df.groupby(
        "Date"
    )["Minutes"].sum()

    st.line_chart(daily_study)

    # -------------------------
    # Study Sessions
    # -------------------------

    st.header("📝 Your Study Sessions")

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "Add your first study session above!"
    )
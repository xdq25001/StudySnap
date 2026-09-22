import csv
import os

filename = "study_sessions.csv"

if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Topic", "Minutes", "Confidence"])

subject = input("What subject did you study? ")
topic = input("What topic did you study? ")
minutes = int(input("How many minutes did you study? "))
confidence = int(input("How confident are you? (1-5): "))

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([subject, topic, minutes, confidence])

print("\nStudy session saved! 📚")
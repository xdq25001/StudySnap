import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("study_sessions.csv")

total_minutes = df["Minutes"].sum()
average_confidence = df["Confidence"].mean()

print("\n📚 STUDY SUMMARY")
print("----------------")
print(f"Total study time: {total_minutes} minutes")
print(f"Average confidence: {average_confidence:.1f}/5")

subject_time = df.groupby("Subject")["Minutes"].sum()

print("\nStudy time by subject:")

for subject, minutes in subject_time.items():
    print(f"{subject}: {minutes} minutes")

confidence_by_subject = df.groupby("Subject")["Confidence"].mean()

lowest_confidence = confidence_by_subject.idxmin()
lowest_score = confidence_by_subject.min()

print(f"\n💡 You may want to review: {lowest_confidence}")
print(f"Average confidence: {lowest_score:.1f}/5")

subject_time.plot(kind="bar")

plt.title("Study Time by Subject")
plt.xlabel("Subject")
plt.ylabel("Minutes")
plt.tight_layout()
plt.show()

confidence_by_subject.plot(kind="bar")

plt.title("Average Confidence by Subject")
plt.xlabel("Subject")
plt.ylabel("Confidence (1-5)")
plt.ylim(0, 5)
plt.tight_layout()
plt.show()
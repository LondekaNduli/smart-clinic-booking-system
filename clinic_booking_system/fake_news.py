from faker import Faker
from matplotlib.pylab import real
import pandas as pd
import random

fake = Faker()

topics = ["Politics", "Health", "Technology", "Sports", "Education", "Business", "Science"]

fake_templates = [
    "Shocking report claims {subject} causes unbelievable results",
    "Secret government plan about {subject} revealed online",
    "Experts allegedly hide truth about {subject}",
    "Viral rumor says {subject} will change next month",
    "Anonymous source exposes surprising facts about {subject}"
]

true_templates = [
    "{subject} department releases official update",
    "New research published on {subject}",
    "Authorities confirm developments in {subject}",
    "Industry report highlights trends in {subject}",
    "Government announces verified plans for {subject}"
]

def generate_rows(n, label):
    rows = []
    for _ in range(n):
        topic = random.choice(topics)
        subject = topic.lower()
        if label == "fake":
            title = random.choice(fake_templates).format(subject=subject)
            text = (
                f"{fake.paragraph(nb_sentences=4)} "
                f"Social media users continue discussing claims related to {subject}. "
                f"{fake.paragraph(nb_sentences=5)}"
            )
        else:
            title = random.choice(true_templates).format(subject=subject)
            text = (
                f"{fake.paragraph(nb_sentences=4)} "
                f"Officials and verified sources shared information related to {subject}. "
                f"{fake.paragraph(nb_sentences=5)}"
            )

        rows.append({
            "title": title,
            "text": text,
            "subject": topic,
            "date": fake.date_between(start_date="-3y", end_date="today").strftime("%Y-%m-%d")
        })
    return rows

fake_df = pd.DataFrame(generate_rows(1000, "fake"))
true_df = pd.DataFrame(generate_rows(1000, "true"))

fake_path = "Fake.csv"
true_path = "True.csv"

fake_df.to_csv(fake_path, index=False)
true_df.to_csv(true_path, index=False)

print(fake_path, true_path)


fake["label"] = 0
real["label"] = 1

import os
import yaml
import datetime as dt

TARGET_DIR = "test"
START_DATE = dt.date(2021, 1, 19)
END_DATE = dt.date(2021, 4, 30)
WEEKENDS = False

def semester_days(start, end, weekends=False):
    delta = dt.timedelta(days=1)
    date = start - delta
    while date <= end:
        date += delta
        if date.weekday() >= 5 and not weekends:
            continue
        yield date

def main():
    days = semester_days(START_DATE, END_DATE, WEEKENDS)
    weeks = [{"days": []}]
    for day in days:
        if (day.weekday() == 0 and not WEEKENDS) or (day.weekday() == 6 and WEEKENDS):
            weeks.append({"days": []})
        
        weeks[-1]["days"].append({"date": day, "events": {"": ""}})
    
    os.makedirs(TARGET_DIR, exist_ok=True)
    for i, week in enumerate(weeks):
        data = {"title": f"Week {i + 1}", "weekNumber": i + 1}
        data.update(weeks[i])

        with open(os.path.join(TARGET_DIR, f"week-{i+1:02}.md"), "w+") as f:
            f.write("---\n" + yaml.dump(data, indent=2, sort_keys=False) + "\n---\n")

if __name__ == "__main__":
    main()        

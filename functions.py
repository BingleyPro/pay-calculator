import datetime as dt

pay_rates = [
    {
        "name": "category_name",
        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "requirements": [],
        "time_range": (dt.time(6, 0, 0), dt.time(18, 0, 0)),
        "rate": 17.24
    },
    {
        "name": "public_holiday",
        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "requirements": ["public_holiday"],
        "time_range": (dt.time(6, 0, 0), dt.time(18, 0, 0)),
        "rate": 24.83
    }
]

def match_day(date: dt.datetime):
     match dt.datetime.isoweekday(date):
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return None

# Calculate Time
def calculate_pay(shift_data: dict):
    date = shift_data["date"]
    start_time = shift_data["start"]
    end_time = shift_data["end"]
    flags = shift_data["flags"]

    pay = 0.00
    for rate in pay_rates:
        if match_day(date) in rate["days"] and all(req in flags for req in rate["requirements"]):
            rate_start = dt.datetime.combine(date, rate["time_range"][0])
            rate_end = dt.datetime.combine(date, rate["time_range"][1])

            overlap_start = max(start_time, rate_start)
            overlap_end = min(end_time, rate_end)

            print(overlap_start)
            print(overlap_end)
            
            # Check if any time lays within the pay rate
            if overlap_start < overlap_end:
                print("hi")
                overlap = overlap_end - overlap_start
                hours = overlap.total_seconds() / 3600
                pay += hours * rate["rate"]
    return round(pay, 2)

pay = calculate_pay({
    "date": dt.datetime(2026, 5, 28),
    "start": dt.datetime(2026, 5, 28, 13, 0),
    "end": dt.datetime(2026, 5, 28, 15, 0),
    "flags": ["public_holiday"]
})

print(pay)
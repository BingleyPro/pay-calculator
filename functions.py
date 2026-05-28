from datetime import datetime as dt

pay_rates = [
    {
        "name": "category_name",
        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "requirements": [],
        "time_range": (600, 1800),
        "rate": 17.24
    },
    {
        "name": "public_holiday",
        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "requirements": ["public_holiday"],
        "time_range": (600, 1800),
        "rate": 24.83
    }
]

# Calculate Time
def calculate_pay(shift_data: dict):
    date = shift_data["date"]
    start_time = shift_data["start"]
    end_time = shift_data["end"]

    match dt.isoweekday(date):
        case 1:
            weekday = "Monday"
        case 2:
            weekday = "Tuesday"
        case 3:
            weekday = "Wednesday"
        case 4:
            weekday = "Thursday"
        case 5:
            weekday = "Friday"
        case 6:
            weekday = "Saturday"
        case 7:
            weekday = "Sunday"
        case _:
            weekday = None

    pay = 0.00
    for rate in pay_rates:
        if not weekday in rate["days"]:
            break

        # Get time between range
        if start_time >= rate["time_range"][0] and end_time <= rate["time_range"][1]:
            hours = end_time - start_time
            dt.time
            pay += rate["rate"] * (hours / 60)
            return pay
        
        if start_time >= rate["time_range"][0] and end_time > rate["time_range"][1]:
            hours = rate["time_range"][1] - start_time
            pay += rate["rate"] * (hours / 60)
            start_time = rate["time_range"][1]
            break

        if start_time < rate["time_range"][0] and end_time <= rate["time_range"][1]:
            hours = end_time - rate["time_range"][0]
            pay += rate["rate"] * (hours / 60)
            end_rate = rate["time_range"][0]
            break

        if start_time < rate["time_range"][0] and end_time > rate["time_range"][1]:
            break
    return pay

pay = calculate_pay({
    "date": dt.today(),
    "start": 1300,
    "end": 1500
})

print(pay)
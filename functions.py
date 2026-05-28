from datetime import datetime as dt

pay_rates = [
    {
        "name": "category_name",
        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "requirements": [],
        "time_range": ("6:00", "18:00"),
        "rate": 17.24
    },
    {
        "name": "public_holiday",
        "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "requirements": ["public_holiday"],
        "time_range": ("6:00", "18:00"),
        "rate": 24.83
    }
]

# Calculate Time
def calculate_time(shift_data: dict):
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
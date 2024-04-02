from datetime import datetime, timedelta

# Define a mapping of Spanish month names to their corresponding numerical values
spanish_month_mapping = {
    "Ene": "01", "Feb": "02", "Mar": "03", "Abr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Ago": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dic": "12"
}

def is_within_next_10_days(target_datetime):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=10)

    # Check if the target datetime is within the next 10 days
    return current_date <= target_datetime <= future_date


def parse_datetime(date_string:str):
    # Clean the string from '.'
    date_string = date_string.replace('.', '')
    # Extract the day, month abbreviation, and month from the input string
    _, day, _, month_abbrev = date_string.split()

    # Convert the month abbreviation to its numerical value
    month = spanish_month_mapping[month_abbrev]

    # Construct a new date string with the numerical month value
    formatted_date_string = f"{day} {month} {datetime.now().year}"
    #print(formatted_date_string)

    # Parse the formatted date string into a datetime object
    date_object = datetime.strptime(formatted_date_string, "%d %m %Y")

    return date_object

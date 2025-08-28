import re
import pandas as pd
from datetime import datetime

def preprocess(data):
    # Regex matches both "03/12/20, 11:40 pm - " and "4/16/25, 15:17 - "
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s?(?:am|pm))?\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    def parse_date(date_str):
        date_str = date_str.strip(" -")  # remove trailing " - "
        # Try both 24-hour and 12-hour formats
        for fmt in ("%d/%m/%Y, %H:%M", "%d/%m/%y, %H:%M",
                    "%d/%m/%Y, %I:%M %p", "%d/%m/%y, %I:%M %p"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None

    # Convert to datetime (will always be in 24-hour once parsed)
    df['message_date'] = df['message_date'].apply(parse_date)
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Split user and message
    users, messages = [], []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name exists
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # Extract date/time features
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Create time periods (hour bins)
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append("23:00-00:00")
        elif hour == 0:
            period.append("00:00-1:00")
        else:
            period.append(f"{hour}:00-{hour+1}:00")
    df['period'] = period

    return df

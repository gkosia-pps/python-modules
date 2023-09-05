from datetime import datetime

print(f"The current date and time is {datetime.now()}")
print(f"The current date and time as timestamp is {datetime.timestamp(datetime.now())}")


curr_ts = datetime.timestamp(datetime.now())
print(f"The timestamp {curr_ts} is {datetime.fromtimestamp(curr_ts)} as datetime")


print(f"To format {datetime.now()} as yyyy-mm-dd use {datetime.now().strftime('%Y-%m-%d')} ")

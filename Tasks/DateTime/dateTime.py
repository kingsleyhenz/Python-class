# DATE AND TIME
from datetime import datetime

now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
timestamp = now.timestamp()

# 1. Get the current day, month, year, hour, minute, and timestamp from datetime module
new_date = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(new_date)

# 2. Today is 10  JULY, 2023. Change this time string to time.
today_string = "10 JULY, 2023"
time_obj = datetime.strptime(today_string, "%d %B, %Y")
# print(time_obj)

# 3. Calculate the time difference between now and the new year
new_year = datetime(current_year + 1, 1, 1)
time_diff = new_year - now
# print(time_diff)

# 4. Calculate the time difference between 1 January 1970 and now
past_time = datetime(1970, 1, 1)
time_past = now - past_time
# print(time_past)

# Think, what can you use the datetime module for? Examples:
# a. Time series analysis
# The datetime module provides powerful tools for working with dates and times, making it suitable for time series analysis. You can use it to manipulate and analyze time series data and calculate time-based statistics
 
# b. To get a timestamp of any activities in an application
# The timestamps can be useful for tracking user behavior, measuring performance, and generating reports in an application.

# c. Adding posts on a blog
# When adding posts on a blog or content management system, the datetime module can help manage the publication date and time of the posts.

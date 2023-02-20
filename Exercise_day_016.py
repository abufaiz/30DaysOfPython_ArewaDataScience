# Day 16 - 30DaysOfPython Exercises

print("......................... Q. 1.......................................")

'''Get the current day, month, year, hour, minute and timestamp from datetime module'''

from datetime import datetime

# get current datetime object
now = datetime.now()

# extract day, month, year, hour, minute
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute

# create timestamp using strftime method
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# print the values
print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Hour:", hour)
print("Minute:", minute)
print("Timestamp:", timestamp)

print("......................... Q. 2.......................................")

'''Format the current date using this format: "%m/%d/%Y, %H:%M:%S")'''

from datetime import datetime

# get current datetime object
now = datetime.now()

# format the date using strftime method
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

# print the formatted date
print("Formatted date:", formatted_date)


print("......................... Q. 3.......................................")

'''Today is 5 December, 2019. Change this time string to time'''

from datetime import datetime

# time string to convert
time_str = "5 December, 2019"

# create datetime object from time string
time = datetime.strptime(time_str, "%d %B, %Y")

# print the datetime object
print(time)


print("......................... Q. 4.......................................")

'''Calculate the time difference between now and new year.'''

from datetime import datetime

# get current time and New Year's Day time
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)

# calculate time difference
time_difference = new_year - now

# print the time difference in days, hours, and minutes
days = time_difference.days
hours = time_difference.seconds // 3600
minutes = (time_difference.seconds // 60) % 60
print("Time until New Year's Day: {} days, {} hours, {} minutes".format(days, hours, minutes))


print("......................... Q. 5.......................................")

'''Calculate the time difference between 1 January 1970 and now'''

from datetime import datetime

# get Unix epoch time and current time
epoch = datetime.utcfromtimestamp(0)
now = datetime.now()

# calculate time difference
time_difference = now - epoch

# print the time difference in days, hours, minutes, and seconds
days = time_difference.days
hours = time_difference.seconds // 3600
minutes = (time_difference.seconds // 60) % 60
seconds = time_difference.seconds % 60
print("Time since Unix epoch: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))


print("......................... Q. 6.......................................")

'''Think, what can you use the datetime module for? Examples:
Time series analysis
To get a timestamp of any activities in an application
Adding posts on a blog'''

'''The datetime module is a versatile and powerful module that can be used
      for a wide range of tasks related to dates and times. Here are some more
      examples of what you can use the datetime module for:
          
Event scheduling: You can use the datetime module to schedule events, such as 
reminders or notifications, to occur at specific times and dates.

Data logging: You can use the datetime module to log the date and time of events,
such as errors or user actions, in a log file.

Time-based data filtering: If you have data that is time-stamped, such as stock
prices or weather data, you can use the datetime module to filter and analyze 
the data based on specific time periods.

Time zone conversion: The datetime module includes functionality for converting
between different time zones, which can be useful if you need to work with data
from different parts of the world.

Web development: You can use the datetime module to manage timestamps for web
applications, such as adding time stamps to user comments or blog posts.

Data analysis: The datetime module can be used to analyze time-series data, such
as customer behavior or website traffic, to identify trends and patterns over time.

Overall, the datetime module is a powerful tool for managing dates and times, 
and it can be used in a wide variety of applications, including those related 
to data analysis, event scheduling, and web development.'''






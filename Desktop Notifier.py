from plyer import notification
import time

# specify the title and message for the notification
title = 'Desktop Notifier'
message = 'This is a desktop notification! , Hello Venu'

# display the notification
notification.notify(title=title, message=message, timeout=10)

# wait for 5 seconds before exiting the program
time.sleep(5)

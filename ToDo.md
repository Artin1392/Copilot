[] Adding date (# TODO: Date
# Date
from datetime import date
def Date():
    today = date.today()
    date = today.strftime("%B %d, %Y")
    text = "Today is {date}."
    print(text))


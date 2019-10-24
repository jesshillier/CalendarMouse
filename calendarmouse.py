from datetime import datetime
from PIL import Image


def createImageFromDate(currentMonth, currentDay):
    topMonth = currentMonth
    previousDay = currentDay - 1
    print("top month", topMonth)
    print("prev day", previousDay)

    base = Image.open("images/cal_mouse_base.png")

    topMonthLayer = Image.open("images/month/top/" + str(topMonth) + ".png")
    midMonthLayer = Image.open("images/month/mid/" + str(currentMonth) + ".png")
    bottomMonthLayer = Image.open("images/month/bot/" + str(topMonth) + ".png")

    topDayLayer = Image.open("images/day/top/" + str(previousDay) + ".png")
    midDayLayer = Image.open("images/day/mid/" + str(currentDay) + ".png")
    bottomDayLayer = Image.open("images/day/bot/" + str(previousDay) + ".png")

    base.paste(topMonthLayer, (0, 0), topMonthLayer)
    base.paste(midMonthLayer, (0, 0), midMonthLayer)
    base.paste(bottomMonthLayer, (0, 0), bottomMonthLayer)
    base.paste(midDayLayer, (0, 0), midDayLayer)
    base.paste(topDayLayer, (0, 0), topDayLayer)
    base.paste(bottomDayLayer, (0, 0), bottomDayLayer)
    base.save("result.png")


currentDay = datetime.now().day
currentMonth = datetime.now().month
createImageFromDate(currentMonth, currentDay)

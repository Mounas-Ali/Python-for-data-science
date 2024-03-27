import time
import datetime

seconds_nbr = time.time()

scientific_nbr = "{:.7e}".format(seconds_nbr)
nbr_9 = "{:.9f}".format(seconds_nbr)

date = f"Seconds since January 1, 1970: {nbr_9} or {scientific_nbr} in scientific notation"

date_aujoudhui = datetime.date.today()
real = date_aujoudhui.strftime("%b %d %Y")


print(date)
print(real)
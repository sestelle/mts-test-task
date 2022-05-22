import gzip
import os
import random

from config import LOGS_DATE_START, LOGS_DATE_END, LOGS_AMOUNT_MIN, LOGS_AMOUNT_MAX
from datetime import datetime as dt, timedelta


def create_logs():
    os.mkdir("log")

    start_date = dt.strptime(LOGS_DATE_START, "%d-%m-%Y")
    end_date = dt.strptime(LOGS_DATE_END, "%d-%m-%Y")
    delta = timedelta(days=1)

    while start_date <= end_date:
        file_name = "smbp_" + dt.strftime(start_date, "%d%m%Y") + "_034106_app_01.log"
        file = open(f"log/{file_name}", "w+")
        for _ in range(random.randint(LOGS_AMOUNT_MIN, LOGS_AMOUNT_MAX)):
            if random.randint(1, 2) == 1:
                file.write("Error some string\n")
            else:
                file.write("Success some string\n")
        start_date += delta
        file.close()

        file = open(f"log/{file_name}", "rb")
        gzip_file = gzip.open(f"log/{file_name}.gz", "wb")
        gzip_file.writelines(file)
        file.close()
        os.remove(f"log/{file_name}")
        gzip_file.close()

import gzip
import os

from datetime import datetime as dt


def count_success():
    count = 0

    for _, _, files in os.walk("./log"):
        for filename in files:
            if filename.endswith(".log.gz"):
                filename_split = filename.split("_")

                date = dt.strptime(filename_split[1], "%d%m%Y")

                if date.date() == dt.today().date():
                    gzip_file = gzip.open(f"log/{filename}", "rb")
                    for line in gzip_file:
                        string = line.decode("utf-8")
                        if " Success " in (" " + string[:-1] + " "):
                            count += 1

                    gzip_file.close()

    print(f"Количество строк, которые содержат слово 'Success' = {count}")

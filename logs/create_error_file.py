import os
import gzip

from datetime import datetime as dt


def create_error_file():
    file = open(f"Error.log", "w+")

    for _, _, files in os.walk("./log"):
        for filename in files:
            if filename.endswith(".log.gz"):
                filename_split = filename.split("_")

                date = dt.strptime(filename_split[1], "%d%m%Y")

                if date.date().month == dt.today().date().month:
                    gzip_file = gzip.open(f"log/{filename}", "rb")
                    for line in gzip_file:
                        string = line.decode("utf-8")
                        if " Error " in (" " + string[:-1] + " "):
                            file.write(string)

                    gzip_file.close()

    file.close()

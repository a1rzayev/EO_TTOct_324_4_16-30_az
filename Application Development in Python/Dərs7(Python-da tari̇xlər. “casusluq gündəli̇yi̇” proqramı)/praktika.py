import os
import datetime


def collector(path, res_path):
    res_path = os.path.normpath(res_path)
    path = os.path.normpath(path)

    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_time = os.path.getmtime(f"{dirpath}\\{file}")
            datetime_file = datetime.datetime.fromtimestamp(file_time)
            file_date = datetime_file.strftime("%d.%m.%Y")

            if os.path.isdir(f"{res_path}\\{file_date}"):
                os.replace(
                    f"{dirpath}\\{file}",
                    f"{res_path}\\{file_date}\\{file}"
                )
            else:
                os.mkdir(f"{res_path}\\{file_date}\\")
                os.replace(
                    f"{dirpath}\\{file}",
                    f"{res_path}\\{file_date}\\{file}"
                )


path = "C:/Users/rzayev_a/EO_TTOct_324_4_16-30_az/Application Development in Python"
res_path = "C:/Users/rzayev_a/EO_TTOct_324_4_16-30_az/Application Development in Python"

collector(path, res_path)
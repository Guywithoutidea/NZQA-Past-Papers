# Script to download exams and schedules

import requests
import os

standards = ["91390", "91391", "91392"]
years = ["2017", "2018", "2019"]

for standard in standards:
    # Make the needed folders
    if not os.path.isdir(f"{standard}"):
        os.mkdir(f"{standard}")
    if not os.path.isdir(f"{standard}/exams"):
        os.mkdir(f"{standard}/exams")
    for year in years:
        if not os.path.isdir(f"{standard}/exams/{year}"):
            os.mkdir(f"{standard}/exams/{year}")
        url = f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/schedules/{year}/{standard}-ass-{year}.pdf"
        request = requests.get(url, allow_redirects=True)
        print("thing")
        open(f"{standard}/exams/{year}/{standard}-exm-{year}.pdf", "wb").write(request.content)
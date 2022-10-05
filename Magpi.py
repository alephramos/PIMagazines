import requests
import datetime
from pathlib import Path
from classes.variables import PATH_DOWNLOAD, FILENAME_PREFIX, URL_MAGPI, PREFIX_RE
import re


def obtain_issue():
    DATE = datetime.datetime.now()
    MONTH = d.strftime("%m")


def obtain_pdf(issue):
    url_issue = URL_MAGPI + "/issues/" + str(issue) + "/pdf/download"
    response = requests.get(url_issue)
    page = response.text
    filename_magpi = "/" + PREFIX_RE + str(issue) + ".pdf"
    end_url = page.find(filename_magpi)
    init_url = page.find("/downloads/")
    real_path = page[init_url + 1:end_url + len(filename_magpi)]
    real_url = URL_MAGPI + real_path
    print(real_url)
    pdf_file = requests.get(real_url)
    magpi_file = FILENAME_PREFIX + str(issue) + ".pdf"
    filename = Path(PATH_DOWNLOAD + "/" + magpi_file)
    filename.write_bytes(pdf_file.content)


if __name__ == "__main__":
    obtain_pdf(110)
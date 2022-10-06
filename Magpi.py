import requests
import datetime
from pathlib import Path
from classes.variables import PATH_DOWNLOAD, FILENAME_PREFIX, URL_MAGPI, PREFIX_RE
import argparse


def actual_issue():
    actual_date = datetime.datetime.now()
    num_month = int(actual_date.strftime("%m"))
    num_year = int(actual_date.strftime("%y"))
    last_issue_21 = 112
    actual_num = ((num_year - 22) * 12) + num_month + last_issue_21
    return actual_num


def obtain_pdf(issue):
    url_issue = URL_MAGPI + "/issues/" + str(issue) + "/pdf/download"
    response = requests.get(url_issue)
    page = response.text
    if int(issue) < 10:
        issue = "0" + issue

    filename_magpi = "/" + PREFIX_RE + str(issue) + ".pdf"
    end_url = page.find(filename_magpi)
    init_url = page.find("/downloads/")
    real_path = page[init_url + 1:end_url + len(filename_magpi)]
    real_url = URL_MAGPI + "/" + real_path
    pdf_file = requests.get(real_url)
    magpi_file = FILENAME_PREFIX + str(issue) + ".pdf"
    filename = Path(PATH_DOWNLOAD + "/" + magpi_file)
    filename.write_bytes(pdf_file.content)


if __name__ == "__main__":
    max_num = str(actual_issue())
    parser = argparse.ArgumentParser(prog='MagPi', usage='%(prog)s [options]')
    parser.add_argument('-i', '--issue', required=False, type=int, help='Number of Issue to download'
                                                                        'if case of missing the actual number is #' +
                                                                        max_num)
    parser.add_argument('-a', '--all', required=False, type=str, help='This option is to download all the numbers of '
                                                                      'MagPi until  #' + max_num)

    args = parser.parse_args()
    if args.issue and args.all:
        print("Only is possible use one of the options or issue or all")
    else:
        if not args.issue:
            print("Obtaining actual number #" + max_num)
            obtain_pdf(max_num)

    if args.issue:
        print("Obtaining the number #" + str(args.issue))
        obtain_pdf(str(args.issue))

    if args.all:
        print("Obtaining all the numbers until #" + max_num)
        for i in range(1, int(max_num)):
            obtain_pdf(str(i))

from dotenv import load_dotenv
import os

ROOT_DIR = os.path.abspath(os.curdir)
load_dotenv(ROOT_DIR + "/.env")

PATH_DOWNLOAD = os.getenv('PATH_DOWNLOAD')
FILENAME_PREFIX = os.getenv('FILENAME_PREFIX')
URL_MAGPI = os.getenv('URL_MAGPI')
PREFIX_RE = "MagPi"
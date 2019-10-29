import sys
from .kintone import Kintone

def main():
    domain = sys.argv[1]
    login_name = sys.argv[2]
    password = sys.argv[3]
    app_ids = sys.argv[4].split(',')
    return Kintone(domain, login_name, password).export(app_ids)

import argparse
from .kintone import Kintone


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", type=str)
    parser.add_argument("login_name", type=str)
    parser.add_argument("password", type=str)
    parser.add_argument("--app", nargs='+', type=int, dest='app')
    args = parser.parse_args()
    return Kintone(args.domain, args.login_name, args.password).export(args.app)

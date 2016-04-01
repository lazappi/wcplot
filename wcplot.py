#!/usr/bin/env python
"""
Produce plots from prettytc log files
"""

import argparse
import pandas as pd

def read_log(logpath):
    """
    Read prettytc log file
    """

    log = pd.read_table(logpath)

    return log


def get_args():
    """
    Get arguments from the command line using argparse
    """

    parser = argparse.ArgumentParser(prog="wcprint",
                                     description="""Produce plots from prettytc
                                                    log files""")
    parser.add_argument("logfile", help="prettytc log file to plot")

    arguments = parser.parse_args()

    return arguments


if __name__ == "__main__":

    args = get_args()

    data = read_log(args.logfile)

    print(data)

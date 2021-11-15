# ---------------------------------

# File          : RegexExample.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 15/11/2021
# Modified Date : 15/11/2021
# Description   : Sample example to run a regex ssh
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import re

lines = open("sshd_logon_attempt.txt").readlines()
for line in lines:
    regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$', line)
    print("{}".format(regex.count("218.49.183.17")))

    for match in regex:
        print("Example {}".format(match))

    if regex is not None:
        for match in regex:
            print("Example matched {0}".format(match))
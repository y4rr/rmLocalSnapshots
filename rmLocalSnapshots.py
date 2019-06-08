#!/usr/bin/env python3
"""rmltm

    Removes local TimeMachine snapshots

    (c) 2019 Alex Merkel, y4rr
    See LICENSE file
"""


import os
import subprocess

# ---------------------------------------------------------------------------- #
def main():
    """The main function"""

    if isroot():
        snapshots = getsnapshots()
        if snapshots:
            print("The following local snapshots were found:")
            print("\n".join(list(map(lambda x: str(x,encoding="utf8"), snapshots))))
            msg = "Are you sure you want to delete all local snapshots?"
            if confirm(msg):
                if deletesnapshots(snapshots):
                    print("All local snapshots removed")
        else:
            print("No local snapshots to remove")
    else:
        print("You need to have root privileges to run this script")
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def isroot():
    """Checks if the script is executed as root

    returns:
        true if root, else false
    """
    return os.geteuid() == 0
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def getsnapshots():
    """Reads all current local snapshots

    returns:
        List of snapshots
    """
    cmd = subprocess.Popen(['tmutil', 'listlocalsnapshotdates'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    snapshots, _ = cmd.communicate()

    snapshots = snapshots.splitlines()
    return snapshots[1:]
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def deletesnapshots(snapshots):
    """Deletes all snapshots in given list

    Args:
        snapshots (list): List of snapshots

    returns:
        True if successful
    """
    i = 0
    count = len(snapshots)
    for item in snapshots:
        i += 1
        print("Removing snapshot {:d} of {:d}".format(i, count))
        subprocess.check_output(['tmutil', 'deletelocalsnapshots', item])

    return True
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def confirm(msg):
    """
    Ask the user to confirm by pressing Y or N (case-insensitive)

    Args:
        msg (string): The question to ask the user

    returns:
        True if the answer is Y
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(msg + " [Y/N] ").lower()

    return answer == "y"
# ############################################################################ #


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    """Default"""
    main()
# ############################################################################ #

#!/usr/bin/env python3
"""rmltm

    Removes local TimeMachine snapshots

    (c) 2018 Alex Merkel
    See LICENSE file
"""


import os
import subprocess
from pprint import pprint

# ---------------------------------------------------------------------------- #
def main():
    """The main function"""

    if isroot():
        snapshots = getsnapshots()
        if snapshots:
            print("The following local snapshots were found:")
            print("\n".join(list(map(lambda x: str(x,encoding="utf8"), snapshots))))
            msg = "Are you sure you want to delete all local snapshots?"
            if confirm(msg):
                if deletesnapshots(snapshots):
                    print("All local snapshots removed")
        else:
            print("No local snapshots to remove")
    else:
        print("You need to have root privileges to run this script")
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def isroot():
    """Checks if the script is executed as root

    returns:
        true if root, else false
    """
    return os.geteuid() == 0
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def getsnapshots():
    """Reads all current local snapshots

    returns:
        List of snapshots
    """
    cmd = subprocess.Popen(['tmutil', 'listlocalsnapshotdates'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    snapshots, _ = cmd.communicate()

    snapshots = snapshots.splitlines()
    return snapshots[1:]
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def deletesnapshots(snapshots):
    """Deletes all snapshots in given list

    Args:
        snapshots (list): List of snapshots

    returns:
        True if successful
    """
    i = 0
    count = len(snapshots)
    for item in snapshots:
        i += 1
        print("Removing snapshot {:d} of {:d}".format(i, count))
        subprocess.check_output(['tmutil', 'deletelocalsnapshots', item])

    return True
# ############################################################################ #

# ---------------------------------------------------------------------------- #
def confirm(msg):
    """
    Ask the user to confirm by pressing Y or N (case-insensitive)

    Args:
        msg (string): The question to ask the user

    returns:
        True if the answer is Y
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(msg + " [Y/N] ").lower()

    return answer == "y"
# ############################################################################ #


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    """Default"""
    main()
# ############################################################################ #


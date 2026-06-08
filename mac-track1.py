#!/usr/bin/env python
# mac_tracker.py

import os
import time
import subprocess
import sys
from datetime import datetime

# ─────────────────────────────────────────────────────

MAC_ADDRESS = "44:1e:a1:3b:13:0c"

LOG_FILE = "/flash/mac_tracker.log"

POLL_INTERVAL = 1

MAX_LOG_SIZE = 5 * 1024 * 1024

# ─────────────────────────────────────────────────────


def timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )[:-3]


def rotate_log():

    rotated = LOG_FILE + ".1"

    try:

        if os.path.exists(rotated):
            os.remove(rotated)

        os.rename(LOG_FILE, rotated)

    except:
        pass


def run_command(cmd):

    try:

        proc = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = proc.communicate()

        try:
            stdout = stdout.decode("utf-8")
        except:
            pass

        return stdout

    except Exception as e:

        return "ERROR: " + str(e)


def parse_mac_output(output, mac):

    mac_lower = mac.lower().replace("-", ":")

    for line in output.splitlines():

        if mac_lower in line.lower():

            parts = line.split()

            # Beispiel:
            # VLAN 1000 44:1e:a1:3b:13:0c dynamic bridging 1/1/11

            if len(parts) >= 6:

                vlan = parts[1]

                port = parts[-1]

                return (
                    "port = " + port
                    + " | vlan = " + vlan
                )

    return "mac not found"


def write_log(entry):

    try:

        if os.path.exists(LOG_FILE):

            if os.path.getsize(LOG_FILE) >= MAX_LOG_SIZE:
                rotate_log()

        with open(LOG_FILE, "a") as f:

            f.write(entry + "\n")

            f.flush()

    except IOError as e:

        sys.stderr.write(
            "Log write error: " + str(e) + "\n"
        )


def main():

    header = (
        "\n"
        + "=" * 60 + "\n"
        + "MAC Tracker started : " + timestamp() + "\n"
        + "Target MAC address  : " + MAC_ADDRESS + "\n"
        + "Log file            : " + LOG_FILE + "\n"
        + "Poll interval       : " + str(POLL_INTERVAL) + "s\n"
        + "=" * 60
    )

    write_log(header)

    print(header)

    iteration = 0

    while True:

        iteration += 1

        raw_output = run_command(
            "show mac-learning"
        )

        result = parse_mac_output(
            raw_output,
            MAC_ADDRESS
        )

        log_entry = (
            "[" + timestamp() + "] "
            + "#" + str(iteration).zfill(6)
            + " | "
            + result
        )

        write_log(log_entry)

        print(log_entry)

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":

    main()
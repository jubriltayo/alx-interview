#!/usr/bin/python3

import sys

possible_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
total_file_size = 0
number_of_lines = 0
status_code_map = {}


def print_stats():
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_code_map.items()):
        print(f"{status_code}: {count}")


try:
    for line in sys.stdin:
        try:
            line = line.split()

            file_size = int(line[-1])
            total_file_size += file_size

            status_code = int(line[-2])
            if status_code in possible_status_code:
                if status_code in status_code_map:
                    status_code_map[status_code] += 1
                else:
                    status_code_map[status_code] = 1

            number_of_lines += 1

            if (number_of_lines % 10) == 0:
                print_stats()

        except ValueError:
            pass
    if (number_of_lines == 0) or (number_of_lines % 10 != 0):
        print_stats()

except KeyboardInterrupt:
    print_stats()

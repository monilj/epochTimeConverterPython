import datetime
from numpy.compat import long


def read_from_log_file():
    global input_file
    input_file = open(r"storage/input.log", 'r')


def write_to_log_file():
    global output_file
    output_file = open(r'storage\output.log', 'w')


def convert_time_to_readable_format():
    for line in input_file:
        parts = line.strip().split(':')
        epoch_data_object = float(parts[0])
        datetime_object = datetime.datetime.fromtimestamp(epoch_data_object)
        date_string = datetime_object.strftime("%a %B %d %Y %H:%M:%S.%f")
        parts.insert(0, date_string)
        seperator = ': '
        my_logs = seperator.join(parts)
        output_file.write(my_logs + "\n")


def close_file_connection():
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    read_from_log_file()
    write_to_log_file()
    convert_time_to_readable_format()
    close_file_connection()

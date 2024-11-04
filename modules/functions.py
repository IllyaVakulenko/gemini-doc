from datetime import datetime


def print_separator(symbol="=", length=20):
    print(symbol * length)


def write_usage(filename, data):
    with open(filename, 'a') as f:
        f.write(f"\n\n# {datetime.now().strftime("%Y-%m-%d %H-%M-%S")}\n\n{data}")

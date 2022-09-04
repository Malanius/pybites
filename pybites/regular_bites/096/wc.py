def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        lines = f.readlines()
        lines_count = len(lines)
        words_count = sum(len(line.split()) for line in lines)
        chars_count = sum(len(line) for line in lines)
    return f"{lines_count}\t{words_count}\t{chars_count}\t{file_}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))

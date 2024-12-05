def execute_spp_script(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace

        # Skip empty lines
        if not line:
            continue

        # Skip single-line comments (lines starting with #)
        if line.startswith('#'):
            continue

        # Remove inline comments (anything after #)
        line = line.split('#')[0].strip()

        # Handle println >> (with a newline)
        if line.startswith('println >>'):
            text_to_print = line[len('println >> '):].strip('";')
            print(text_to_print)  # Prints with a newline

        # Handle print >> (without a newline)
        elif line.startswith('print >>'):
            text_to_print = line[len('print >> '):].strip('";')
            print(text_to_print, end='')  # Prints without a newline

if __name__ == "__main__":
    execute_spp_script('main.spp')

import sys

def load_configuration(config_file):
    replacements = {}
    with open(config_file, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                replacements[key] = value
    return replacements

def replace_and_count(line, replacements):
    original_line = line
    total_replaced = 0
    
    for key, value in replacements.items():
        line = line.replace(key, value)
        total_replaced += original_line.count(key) * len(key)
    
    return line, total_replaced

def process_text_file(text_file, replacements):
    lines_with_replacements = []
    
    with open(text_file, 'r') as file:
        for line in file:
            new_line, replaced_count = replace_and_count(line, replacements)
            lines_with_replacements.append((new_line, replaced_count))
    
    # Sort by the number of symbols replaced in descending order
    lines_with_replacements.sort(key=lambda x: x[1], reverse=True)
    
    return [line for line, _ in lines_with_replacements]

def main(config_file, text_file):
    replacements = load_configuration(config_file)
    sorted_lines = process_text_file(text_file, replacements)
    
    for line in sorted_lines:
        print(line, end='')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <config_file> <text_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    text_file = sys.argv[2]
    
    main(config_file, text_file)

def get_unit_descriptor(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data.splitlines()

def find_matching_rule(descriptor, rules):
    in_rule = False
    matching_rule = []

    for line in rules:
        if f"UnitDescriptor = ~/Descriptor_Unit_{descriptor}" in line:
            in_rule = True
            matching_rule.append(line)
        elif in_rule and '),' in line:
            matching_rule.append(line)
            return matching_rule
        elif in_rule:
            matching_rule.append(line)

    return None

def main():
    unit_data = get_unit_descriptor('Unit.txt')
    unit_descriptor_data = get_unit_descriptor('Unit Descriptor.txt')

    with open('result', 'w') as result_file:
        for unit_line in unit_data:
            start_index = unit_line.find("multi_") + len("multi_")
            end_index = unit_line.find(",", start_index)
            descriptor = unit_line[start_index:end_index]
            matching_rule = find_matching_rule(descriptor, unit_descriptor_data)

            if matching_rule:
                result_file.write("                    TDeckUniteRule"+ '\n')
                result_file.write("                    ("+ '\n')
                for line in matching_rule:
                    result_file.write(line + '\n')


if __name__ == "__main__":
    main()
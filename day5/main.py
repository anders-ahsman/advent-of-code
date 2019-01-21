with open('input.txt', 'r') as f:
    polymer = f.read()

while True:
    print(len(polymer))
    for idx, char in enumerate(polymer):
        at_last_element = idx + 1 == len(polymer)
        if not at_last_element:
            next_char = polymer[idx + 1]
            if char.lower() == next_char.lower():
                # Remove this and next char from polymer and restart
                polymer = polymer[0:idx] + polymer[idx + 2:]
                break

    reached_last_element = idx == len(polymer) - 1
    if reached_last_element:
        print('Final length:', len(polymer))
        break
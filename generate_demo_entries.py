from itertools import cycle
import string

# Load original 100 lines from your file
with open('inputDocs/hscdata', 'r') as f:
    base_lines = [line.rstrip('\n') for line in f.readlines()]  # Preserve trailing spaces

output_file = 'output/generated_entries_hsc.txt'
total_per_letter = 80000
serial_template_range = [f"{ch}{i:06}" for ch in string.ascii_uppercase for i in range(1, total_per_letter + 1)]

with open(output_file, 'w') as out:
    base_cycle = cycle(base_lines)  # Cycle over the 100 lines

    for new_serial, line in zip(serial_template_range, base_cycle):
        original_serial = line[:15]
        modified_serial = original_serial[:8] + new_serial  # Replace 9th to 15th character
        modified_line = modified_serial + line[15:]
        out.write(modified_line + '\n')  # Add newline only

print(f"✅ Done! Generated {len(serial_template_range)} entries in '{output_file}'")

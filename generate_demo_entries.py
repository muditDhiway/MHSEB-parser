# from itertools import cycle
# import string

# # Load original 100 lines from your file
# with open('inputDocs/sscdata', 'r') as f:
#     base_lines = [line.rstrip('\n') for line in f.readlines()]  # Preserve trailing spaces

# output_file = 'output/generated_entries_ssc.txt'
# total_per_letter = 80000
# serial_template_range = [f"{ch}{i:06}" for ch in string.ascii_uppercase for i in range(1, total_per_letter + 1)]

# with open(output_file, 'w') as out:
#     base_cycle = cycle(base_lines)  # Cycle over the 100 lines

#     for new_serial, line in zip(serial_template_range, base_cycle):
#         original_serial = line[:15]
#         modified_serial = original_serial[:8] + new_serial  # Replace 9th to 15th character
#         modified_line = modified_serial + line[15:]
#         out.write(modified_line + '\n')  # Add newline only

# print(f"✅ Done! Generated {len(serial_template_range)} entries in '{output_file}'")

from itertools import cycle
import string

# Choose the mode: either 'SSC' or 'HSC'
MODE = 'HSC'  # Change to 'HSC' if needed

# Define custom alphabets for each mode
ALPHABETS = {
    'SSC': ['C', 'J', 'K', 'A', 'F', 'H', 'D', 'L', 'B'],
    'HSC': ['P', 'N', 'R', 'M', 'X', 'V', 'S', 'T', 'W']
}

# Validate mode
if MODE not in ALPHABETS:
    raise ValueError("Invalid MODE. Choose either 'SSC' or 'HSC'.")

selected_letters = ALPHABETS[MODE]
total_per_letter = 10000  # New range per letter
serial_template_range = [f"{ch}{i:06}" for ch in selected_letters for i in range(1, total_per_letter + 1)]

# Load base lines
with open('inputDocs/hscdata_100', 'r') as f:
    base_lines = [line.rstrip('\n') for line in f.readlines()]  # Preserve trailing space

output_file = f'output/generated_entries_{MODE.lower()}_new.txt'

with open(output_file, 'w') as out:
    base_cycle = cycle(base_lines)

    for new_serial, line in zip(serial_template_range, base_cycle):
        original_serial = line[:15]
        modified_serial = original_serial[:8] + new_serial  # Replace 9th to 15th character
        modified_line = modified_serial + line[15:]
        out.write(modified_line + '\n')  # Keep final newline, preserve trailing spaces

print(f"✅ Done! Generated {len(serial_template_range)} entries in '{output_file}'")


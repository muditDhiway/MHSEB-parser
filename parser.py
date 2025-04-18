import json
import pandas as pd
from datetime import datetime

# HSC Parsing
HSC_FIELD_WIDTHS = [
    ("div", 1),
    ("sch", 7),
    ("seat", 7),
    ("name", 65),
    ("sub1", 2), ("mark1", 3),
    ("sub2", 2), ("mark2", 3),
    ("sub3", 2), ("mark3", 3),
    ("sub4", 2), ("mark4", 3),
    ("sub5", 2), ("mark5", 3),
    ("sub6", 2), ("mark6", 3),
    ("sub7", 2), ("mark7", 3),
    ("Sub8", 2), ("mark8", 3),
    ("result", 3),
    ("outof", 3),
    ("sign", 1),
    ("grace", 2),
    ("course", 1),
    ("mother", 30),
    ("ptotal", 3),
    ("percent", 6)
]
HSC_TOTAL_LENGTH = 169

def parse_line_hsc(line: str) -> dict:
    if len(line) != HSC_TOTAL_LENGTH:
        raise ValueError(f"Line length is {len(line)} but expected 169: {line}")

    record = {}
    index = 0
    for field, width in HSC_FIELD_WIDTHS:
        value = line[index:index + width]
        record[field] = value.strip()  # remove padding
        index += width
    return record

# outputs data not in key-value fashion, converts each entry into a JSON object. 
def parseHSC(file_path: str, output_file_name: str, output_format: str):
    start_time = datetime.now()
    outputFormat = output_format.lower()
    if outputFormat not in ["json", "csv"]:
        raise ValueError("Invalid output format. Choose 'json' or 'csv'.")
    
    parsed_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            try:
                parsed_data.append(parse_line_hsc(line))
            except ValueError as e:
                print(f"Error on line {line_number}: {e}")
    
    df = pd.DataFrame(parsed_data)
    output_file = f"output/{output_file_name}.{output_format}"

    if outputFormat == "json":
        df.to_json(output_file, orient="records", indent=4)
    else:
        df.to_csv(output_file, index=False)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Parsing completed in {elapsed_time.total_seconds()} seconds.")
    
    print(f"Output written to {output_file}")

# outputs data in key value pair where key is 'seat' and value is the rest of the data + 'parse-type'
def parseHSC_New(file_path: str, output_file_name: str, output_format: str):
    start_time = datetime.now()
    output_format = output_format.lower()
    if output_format not in ["json", "csv"]:
        raise ValueError("Invalid output format. Choose 'json' or 'csv'.")

    parsed_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            try:
                record = parse_line_hsc(line)
                seat_no = record.pop("seat")

                # Reorder dict to insert "parse-type" before "div"
                reordered = {"parse-type": "hsc"}
                for key, value in record.items():
                    reordered[key] = value
                record = reordered

                parsed_data.append({seat_no: record})
            except ValueError as e:
                print(f"Error on line {line_number}: {e}")

    output_file = f"output/{output_file_name}.{output_format}"

    if output_format == "json":
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=4)
    else:
        # For CSV: flatten the nested structure
        flat_records = [
            {"seat": seat_no, **fields}
            for record in parsed_data
            for seat_no, fields in record.items()
        ]
        df = pd.DataFrame(flat_records)
        df.to_csv(output_file, index=False)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Parsing completed in {elapsed_time.total_seconds()} seconds.")
    print(f"Output written to {output_file}")


# SSC Parsing
SSC_FIELD_WIDTHS = [
    ("div", 1),
    ("sch", 7),
    ("seat", 7),
    ("name", 65),
    ("sub1", 2), ("mark1", 3),
    ("sub2", 2), ("mark2", 3),
    ("sub3", 2), ("mark3", 3),
    ("sub4", 2), ("mark4", 3),
    ("sub5", 2), ("mark5", 3),
    ("sub6", 2), ("mark6", 3),
    ("total", 3),
    ("outof", 3),
    ("perc", 5),
    ("result", 1),
    ("sign", 1),
    ("sport", 2),
    ("course", 1),
    ("mother", 30)
]
SSC_TOTAL_LENGTH = 156

def parse_line_ssc(line: str) -> dict:
    if len(line) != SSC_TOTAL_LENGTH:
        raise ValueError(f"Line length is {len(line)} but expected 156: {line}")

    record = {}
    index = 0
    for field, width in SSC_FIELD_WIDTHS:
        value = line[index:index + width]
        record[field] = value.strip() 
        index += width
    return record

# outputs data not in key-value fashion, converts each entry into a JSON object.
def parseSSC(file_path: str, output_file_name: str, output_format: str):
    start_time = datetime.now()
    outputFormat = output_format.lower()
    if outputFormat not in ["json", "csv"]:
        raise ValueError("Invalid output format. Choose 'json' or 'csv'.")
    
    parsed_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            try:
                parsed_data.append(parse_line_ssc(line))
            except ValueError as e:
                print(f"Error on line {line_number}: {e}")
    
    df = pd.DataFrame(parsed_data)
    output_file = f"output/{output_file_name}.{output_format}"

    if outputFormat == "json":
        df.to_json(output_file, orient="records", indent=4)
    else:
        df.to_csv(output_file, index=False)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Parsing completed in {elapsed_time.total_seconds()} seconds.")
    
    print(f"Output written to {output_file}")

# outputs data in key value pair where key is 'seat' and value is the rest of the data + 'parse-type'
def parseSSC_New(file_path: str, output_file_name: str, output_format: str):
    start_time = datetime.now()
    output_format = output_format.lower()
    if output_format not in ["json", "csv"]:
        raise ValueError("Invalid output format. Choose 'json' or 'csv'.")

    parsed_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            try:
                record = parse_line_ssc(line)
                seat_no = record.pop("seat")  # Ensure field name matches the one in SSC field list

                # Reorder dict to insert "parse-type" before "div"
                reordered = {"parse-type": "ssc"}
                for key, value in record.items():
                    reordered[key] = value
                record = reordered

                parsed_data.append({seat_no: record})
            except ValueError as e:
                print(f"Error on line {line_number}: {e}")

    output_file = f"output/{output_file_name}.{output_format}"

    if output_format == "json":
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=4)
    else:
        # For CSV: flatten the nested structure
        flat_records = [
            {"seat": seat_no, **fields}
            for record in parsed_data
            for seat_no, fields in record.items()
        ]
        df = pd.DataFrame(flat_records)
        df.to_csv(output_file, index=False)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Parsing completed in {elapsed_time.total_seconds()} seconds.")
    print(f"Output written to {output_file}")

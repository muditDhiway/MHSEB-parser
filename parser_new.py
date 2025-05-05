import csv
import json
from pathlib import Path

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with_seat = []
#    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
#        json.dump(data, json_file, indent=4)

    for row in data:
        obj = {}
        seat = row['seat']
        row['parse-type'] = 'hsc'
        obj[seat] = row
        with_seat.append(obj)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(with_seat, json_file, indent=4)

    write_redis_resp(with_seat, "H9-MRK.txt")
    

def write_redis_resp(parsed_data, output_path):
    def to_resp_frame(key: str, val: str) -> str:
        key_bytes = key.encode("utf-8")
        val_bytes = val.encode("utf-8")
        frame = (
            f"*3\r\n"
            f"$3\r\nSET\r\n"
            f"${len(key_bytes)}\r\n{key}\r\n"
            f"${len(val_bytes)}\r\n{val}"
        )
        return frame

    output_path = Path(output_path).with_suffix(".txt")
    with output_path.open("w", encoding="utf-8") as f:
        first = True
        for item in parsed_data:
            for seat_no, record in item.items():
                val = json.dumps(record, separators=(",", ":"))  # compact JSON
                if not first:
                    f.write("\r\n")
                first = False
                frame = to_resp_frame(seat_no, val)
                f.write(frame)

    print(f"✔ Redis RESP data written to: {output_path}")

# Example usage
csv_to_json('inputDocs/H9-MRK.CSV', 'output/H9.json')

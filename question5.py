import json

def compute_total_revenue(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            data = json.load(f)

        results = []
        for record in data:
            try:
                item = record["item"]
                price = record["price"]
                qty = record["qty"]
                total = price * qty
                results.append((item,total))
            except KeyError as e:
                print(f"missing key {e} in record: {record}")
            except TypeError:
                print(f"Invalid type")
    
        with open(output_file,"w") as f:
            f.write("revenue")
            for item,total in results:
                f.write(f"Item:{item}, Total Revenue {total:,.2f}\n")
    except FileNotFoundError:
        print(f"{input_file} not found")

if __name__ == "__main__":
    compute_total_revenue("sales.json", "report.txt")

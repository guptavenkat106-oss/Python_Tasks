import numpy as np
import pandas as pd
import time
import os

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end = time.time()
            print(f"Execution time: {end - start:.6f} seconds")
    return wrapper


def read_numbers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            try:
                yield float(line.strip())
            except ValueError:
                print(f"Skipping invalid data: {line.strip()}")


def create_file_if_missing(file_path):
    if not os.path.exists(file_path):
        print("data.txt not found. Creating a sample file...")
        with open(file_path, 'w') as f:
            f.write("10\n20\n30\nabc\n40\n50\n")


@time_logger
def process_data(file_path):
    create_file_if_missing(file_path)

    numbers = []

    for num in read_numbers(file_path):
        numbers.append(num)

    if not numbers:
        raise ValueError("No valid numeric data found.")

    mean_val = np.mean(numbers)
    std_val = np.std(numbers)

    df = pd.DataFrame({
        "Metric": ["Mean", "Standard Deviation"],
        "Value": [mean_val, std_val]
    })

    return df

if __name__ == "__main__":
    file_path = "data.txt"

    try:
        result = process_data(file_path)
        print("\nResult DataFrame:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
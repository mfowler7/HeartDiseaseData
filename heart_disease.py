import numpy as np
import pandas as pd
import argparse

class HeartDiseasePatientRecord:
    pass


def process_file(file_path):
    print(f"Processing file: {file_path}")
    df = pd.read_csv(file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="Input data filename")
    args = parser.parse_args()
    
    process_file(args.f)

if __name__ == "__main__":
    main()
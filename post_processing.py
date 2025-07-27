import pandas as pd
import argparse
import os

def clean_caption(text):
    if pd.isna(text):
        return ""
    return ' '.join(text.strip().replace('\n', ' ').split())

def post_process_csv(input_csv_path, output_csv_path=None):
    df = pd.read_csv(input_csv_path)
    
    if 'generate_caption' not in df.columns:
        raise ValueError("CSV must contain a 'generate_caption' column.")

    df['generate_caption'] = df['generate_caption'].apply(clean_caption)
    
    if output_csv_path:
        df.to_csv(output_csv_path, index=False)
        print(f"Post-processed CSV saved to {output_csv_path}")
    else:
        print(df.to_csv(index=False))  # If no output path, just print

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_csv", type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument("--output_csv", type=str, help="Path to save the cleaned CSV file.")
    args = parser.parse_args()

    post_process_csv(args.input_csv, args.output_csv)

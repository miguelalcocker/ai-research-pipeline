#!/usr/bin/env python3
"""
Fix CSV formatting issues:
1. Properly escape titles and abstracts with special characters (semicolons, commas, quotes)
2. Remove newlines from abstracts that cause PowerBI row splitting
"""

import pandas as pd
import os
from pathlib import Path

def clean_text_field(text):
    """Clean text by removing newlines and extra whitespace."""
    if pd.isna(text):
        return text

    # Convert to string if not already
    text = str(text)

    # Replace all types of newlines with spaces
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\r\n', ' ')

    # Replace multiple spaces with single space
    text = ' '.join(text.split())

    return text

def fix_csv_file(file_path, text_columns):
    """Fix CSV formatting by properly handling text fields with special characters."""
    print(f"\n{'='*70}")
    print(f"Processing: {file_path}")
    print(f"{'='*70}")

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    # Read the CSV
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        print(f"✅ Read {len(df)} rows")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

    # Clean specified text columns
    for col in text_columns:
        if col in df.columns:
            print(f"   Cleaning column: {col}")
            df[col] = df[col].apply(clean_text_field)

    # Save with proper quoting to handle special characters
    try:
        df.to_csv(
            file_path,
            index=False,
            encoding='utf-8',
            quoting=1,  # QUOTE_ALL - Quote all fields
            escapechar='\\',
            doublequote=True
        )
        print(f"✅ Saved cleaned CSV with proper quoting")
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

def main():
    """Fix all CSV files in the output/data directory."""
    print("="*70)
    print("CSV FORMATTING FIX")
    print("="*70)
    print("\nThis script will:")
    print("  1. Remove newlines from text fields (titles, abstracts)")
    print("  2. Properly quote and escape all fields")
    print("  3. Ensure PowerBI compatibility")
    print()

    # Define files and their text columns that need cleaning
    files_to_fix = {
        'output/data/fact_publications.csv': ['title', 'abstract', 'keywords', 'doi', 'publication_url'],
        'output/data/dim_authors.csv': ['author_name'],
        'output/data/dim_institutions.csv': ['institution_name', 'country'],
        'output/data/dim_venues.csv': ['venue_name', 'publisher'],
        'output/data/bridge_subfields.csv': ['ai_subfield']
    }

    success_count = 0
    for file_path, text_cols in files_to_fix.items():
        if fix_csv_file(file_path, text_cols):
            success_count += 1

    print()
    print("="*70)
    print(f"COMPLETED: {success_count}/{len(files_to_fix)} files fixed successfully")
    print("="*70)
    print()
    print("✅ All CSV files have been reformatted for PowerBI compatibility")
    print()

if __name__ == "__main__":
    main()

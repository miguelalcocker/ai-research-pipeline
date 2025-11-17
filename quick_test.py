#!/usr/bin/env python3
"""
Quick test script to verify the pipeline works with a small dataset.
This is useful for testing without waiting 30 minutes for full extraction.
"""

import yaml
import sys

print("="*70)
print("Quick Test Mode - AI Research Data Extraction")
print("="*70)
print("\nThis will extract a small dataset (~500 papers) for testing purposes.")
print("Estimated time: 5-10 minutes\n")

# Modify config for quick test
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Store original values
original_min = config['data_collection']['min_papers']
original_max = config['data_collection']['max_papers']

# Set test values
config['data_collection']['min_papers'] = 100
config['data_collection']['max_papers'] = 500

# Save modified config
with open('config_test.yaml', 'w') as f:
    yaml.dump(config, f)

print(f"Original config: {original_min}-{original_max} papers")
print(f"Test config: 100-500 papers")
print("\nStarting extraction...\n")

# Temporarily replace config.yaml
import os
os.rename('config.yaml', 'config.yaml.bak')
os.rename('config_test.yaml', 'config.yaml')

try:
    # Run the main script
    exec(open('extract_ai_research_data.py').read())
finally:
    # Restore original config
    os.rename('config.yaml', 'config_test.yaml')
    os.rename('config.yaml.bak', 'config.yaml')
    print("\nOriginal config restored.")

print("\n" + "="*70)
print("Quick test completed!")
print("="*70)
print("\nReview the output files:")
print("  - output/data/*.csv")
print("  - output/logs/data_quality_report.html")
print("\nIf everything looks good, run the full extraction:")
print("  python extract_ai_research_data.py")
print("="*70)

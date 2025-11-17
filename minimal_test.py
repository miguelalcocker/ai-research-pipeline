#!/usr/bin/env python3
"""
Minimal test - extracts only 100 papers to verify the fix works
"""

import yaml
import os

print("="*70)
print("MINIMAL TEST - Verifying Abstract Extraction Fix")
print("="*70)
print("\nThis will extract ~100 papers to verify the fix works.")
print("Estimated time: 2-3 minutes\n")

# Temporarily replace config
os.rename('config.yaml', 'config.yaml.bak')
os.rename('config_quick_test.yaml', 'config.yaml')

try:
    # Run the main script
    exec(open('extract_ai_research_data.py').read())
except Exception as e:
    print(f"\n\nERROR: {e}")
    import traceback
    traceback.print_exc()
finally:
    # Restore original config
    if os.path.exists('config.yaml'):
        os.rename('config.yaml', 'config_quick_test.yaml')
    if os.path.exists('config.yaml.bak'):
        os.rename('config.yaml.bak', 'config.yaml')
    print("\nOriginal config restored.")

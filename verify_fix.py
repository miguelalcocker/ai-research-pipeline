#!/usr/bin/env python3
"""
Quick verification that the abstract extraction fix works
Extracts just 25 papers to test the pipeline
"""

import yaml
import os
import sys

# Modify config for super quick test
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

config['data_collection']['min_papers'] = 10
config['data_collection']['max_papers'] = 25

with open('config_verify.yaml', 'w') as f:
    yaml.dump(config, f)

print("="*70)
print("VERIFICATION TEST - Super Quick (25 papers)")
print("="*70)
print()

# Temporarily replace config
if os.path.exists('config.yaml'):
    os.rename('config.yaml', 'config.yaml.bak')
os.rename('config_verify.yaml', 'config.yaml')

try:
    exec(open('extract_ai_research_data.py').read())
    print("\n" + "="*70)
    print("✓ VERIFICATION SUCCESSFUL!")
    print("="*70)
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    # Restore original config
    if os.path.exists('config.yaml'):
        os.rename('config.yaml', 'config_verify.yaml')
    if os.path.exists('config.yaml.bak'):
        os.rename('config.yaml.bak', 'config.yaml')

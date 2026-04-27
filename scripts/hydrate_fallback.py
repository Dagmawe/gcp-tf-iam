#!/usr/bin/env python3
"""
hydrate_fallback.py - Hydrate fallback_map.json from Magic Modules source.

Usage:
  python3 hydrate_fallback.py <path_to_magic_modules>
"""

import os
import sys
import json
import os
import sys
import json
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hydrate_fallback.py <path_to_magic_modules>")
        sys.exit(1)

    mm_path = sys.argv[1]
    if not os.path.exists(mm_path):
        print(f"Error: Magic Modules path '{mm_path}' not found.")
        sys.exit(1)

    print(f"Scanning Magic Modules at '{mm_path}'...")
    
    products_dir = os.path.join(mm_path, "mmv1", "products")
    if not os.path.exists(products_dir):
        products_dir = os.path.join(mm_path, "products")
        if not os.path.exists(products_dir):
            print(f"Error: Could not find 'products' directory in '{mm_path}'.")
            sys.exit(1)

    found_count = 0
    fallback_map = {}

    # Regex patterns
    name_pattern = re.compile(r"^name:\s*'([^']+)'")
    base_url_pattern = re.compile(r"^base_url:\s*'([^']+)'")

    for root, dirs, files in os.walk(products_dir):
        rel_path = os.path.relpath(root, products_dir)
        path_parts = rel_path.split(os.sep)
        if not path_parts or path_parts[0] == '.':
             continue
        service = path_parts[0].lower()
        
        for file in files:
            if file.endswith(".yaml") and file != "product.yaml":
                filepath = os.path.join(root, file)
                try:
                     with open(filepath, 'r') as f:
                         name = None
                         base_url = None
                         for line in f:
                             line = line.strip()
                             if not name:
                                 m = name_pattern.match(line)
                                 if m:
                                     name = m.group(1)
                             if not base_url:
                                 m = base_url_pattern.match(line)
                                 if m:
                                     base_url = m.group(1)
                             if name and base_url:
                                 break
                         
                         if name and base_url:
                             parts = base_url.split('/')
                             if parts:
                                 collection = parts[-1].lower()
                                 if '{{' not in collection and '{' not in collection:
                                      method_id = f"{service}.{collection}.insert"
                                      permission = f"{service}.{collection}.create"
                                      
                                      if method_id not in fallback_map:
                                          fallback_map[method_id] = [permission]
                                          found_count += 1
                except Exception:
                     pass

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "tf_iam", "fallback_map.json")
    try:
         with open(output_path, 'r') as f:
              existing_map = json.load(f)
              for k, v in fallback_map.items():
                  if k not in existing_map:
                      existing_map[k] = v
              fallback_map = existing_map
    except FileNotFoundError:
         pass

    try:
         with open(output_path, 'w') as f:
              json.dump(fallback_map, f, indent=2)
         print(f"\n✅ Hydration complete! Updated {output_path} with {found_count} new inferred mappings.")
    except Exception as e:
         print(f"Error saving output: {e}")

if __name__ == "__main__":
    main()

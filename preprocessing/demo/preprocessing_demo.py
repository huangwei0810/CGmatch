#!/usr/bin/env python3
"""Simple test for preprocessing ablation."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from registration_benchmark_methods import load_gray_image
import numpy as np

# Test with a sample image
test_image = Path("datasets/raw/MSRS/train/vi")
images = list(test_image.glob("*.png")) + list(test_image.glob("*.jpg"))

if images:
    test_img = images[0]
    print(f"Testing with image: {test_img.name}")
    
    # Test each preprocessing method
    for method in ["none", "clahe", "clahe_gradient"]:
        print(f"\n{method.upper()}:")
        try:
            img = load_gray_image(str(test_img), preprocessing=method)
            print(f"  Shape: {img.shape}")
            print(f"  Dtype: {img.dtype}")
            print(f"  Min: {img.min()}, Max: {img.max()}")
        except Exception as e:
            print(f"  Error: {e}")
else:
    print("No test images found!")

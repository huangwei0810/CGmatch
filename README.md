<img width="3280" height="2083" alt="4-1" src="https://github.com/user-attachments/assets/3ec50c82-9cb8-4069-beca-6062dc692284" /><img width="4352" height="952" alt="SSM2 0" src="https://github.com/user-attachments/assets/dc623233-c1b3-4626-9963-e809190ae9c7" /># CGMatch 

CGMatch is a visible-infrared image matching and registration project. 

<img width="4316" height="1600" alt="3-1" src="https://github.com/user-attachments/assets/e4f822ed-8bc2-454b-81e7-afdeeca2ef99" />

<img width="2340" height="2320" alt="3-3" src="https://github.com/user-attachments/assets/1deeefc7-5904-48bc-97e6-cb3712e71cc1" />

<img width="4352" height="952" alt="SSM2 0" src="https://github.com/user-attachments/assets/a5bdb4a7-0024-4230-abfd-4a23e6390bc1" />

<img width="2168" height="2484" alt="3-4" src="https://github.com/user-attachments/assets/19871eb0-bc85-4f14-a9b3-556b42c03362" />

<img width="3280" height="2083" alt="4-1" src="https://github.com/user-attachments/assets/428c22a1-ef19-4198-9567-0bd042999519" />

<img width="3284" height="2083" alt="4-1b" src="https://github.com/user-attachments/assets/683e055b-e612-45fa-bdf8-5afc58aac530" />

## Repository Contents

- `dataset/LPC-Set`: LPC-Set (local photometric change dataset) real collected data
- `requirements.txt`: summarized dependencies used by the full private research codebase.

## Full Project Environment

The full private codebase uses Python 3.8+ and the dependencies listed in `requirements.txt`.

Core dependencies:

- PyTorch and torchvision for model training and inference
- OpenCV, Kornia, NumPy, and SciPy for image processing and geometry
- Transformers for loading the SuperPoint frontend
- tqdm and matplotlib for training utilities and visualization
- nibabel for optional medical/NIfTI registration tests

For GPU training, install a PyTorch build matching the local CUDA runtime before installing the rest of the environment.

## Expected Dataset Layout

The full training pipeline expects paired visible/infrared data, for example:

```text
datasets/
  vi/
  ir_transformed/
  cache/
```

For generated affine-supervised pairs, each target usually has:

- a visible image under `datasets/vi/`
- warped infrared images under `datasets/ir_transformed/`
- affine matrix files for geometric supervision

## Typical Private Commands

Training:

```bash
python train.py --data_path datasets --epochs 100 --use_amp
```

Single-pair testing:

```bash
python registration_testing.py --visible path/to/visible.png --infrared path/to/infrared.png --model checkpoints/best_model.pth
```

Benchmarking and ablations:

```bash
python run_comprehensive_benchmark.py --model-path checkpoints/best_model.pth
python run_complete_ablation.py --all --model-path checkpoints/best_model.pth
```

These commands require the private code, datasets, and checkpoints.

## To Do List

1.Upload the source code

2.Upload the Weight

3.Update the complete dataset

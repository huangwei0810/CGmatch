# CGMatch 

CGMatch is a visible-infrared image matching and registration project. 

<img width="3684" height="2016" alt="模型结构 drawio" src="https://github.com/user-attachments/assets/f31e4446-fb40-4d58-a7b8-76dc63501b3c" />

<img width="2612" height="1096" alt="SSM drawio" src="https://github.com/user-attachments/assets/e4a0a37c-31cc-40ee-86eb-a8aa138bb4d5" />

<img width="1300" height="960" alt="效果图 drawio" src="https://github.com/user-attachments/assets/52556ec2-92fe-421f-9832-6eb231de3b6a" />

<img width="3927" height="1590" alt="量化图 drawio" src="https://github.com/user-attachments/assets/f25f569f-3c0c-4a9d-a9dc-a25f257d142e" />

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

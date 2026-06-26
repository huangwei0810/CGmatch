# CGMatch Demo

This repository is a lightweight public demo for CGMatch, a visible-infrared image matching and registration project.

The full research code, trained weights, private datasets, benchmark scripts, ablation runs, and paper artifacts are intentionally not included here. This demo only shows the expected project interface and a mock visualization workflow.

## What is Included

- `demo.py`: a runnable placeholder demo that creates a toy match visualization.
- `cgmatch_demo/`: a small public API skeleton showing how the real project can be called.
- `requirements.txt`: minimal dependencies for the placeholder demo.

## What is Not Included

- Model implementation
- Training code
- Trained checkpoints
- Private or third-party datasets
- Benchmark reports and ablation scripts
- Paper drafts and experiment logs

## Quick Start

```bash
pip install -r requirements.txt
python demo.py
```

The demo writes a visualization to:

```text
outputs/mock_matches.png
```

You can also pass two local images:

```bash
python demo.py --image0 path/to/visible.png --image1 path/to/infrared.png
```

## Intended Full Pipeline

```python
from cgmatch_demo import CGMatch

matcher = CGMatch()
result = matcher.match("visible.png", "infrared.png")
print(result.matches)
```

In this public demo, `CGMatch.match()` is an interface stub. The production implementation is kept private.

## Project Status

This is a display-only demo repository for academic/project presentation. It is not intended to reproduce the full experimental results.

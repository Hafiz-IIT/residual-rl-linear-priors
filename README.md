# Residual RL with Linear Priors

> **Research prototype:** studying whether a learned residual controller can improve a transparent linear control prior without replacing its structure.

## Research question
Can a residual policy learn a useful correction to a known linear controller while preserving an interpretable baseline?

## Implemented
- scalar linear baseline controller
- residual correction
- configurable action bounds
- deterministic rollout
- baseline-vs-residual comparison

## Quickstart
```bash
python demo.py
python -m unittest discover -s tests -v
```

## Boundary
This repository is a reproducible control experiment, not a claim of safe deployment, benchmark superiority, or published research.

Related: [Safe RL Action Gate](https://github.com/Hafiz-IIT/safe-rl-action-gate) · [Hybrid LQR + RL Control](https://github.com/Hafiz-IIT/hybrid-lqr-rl-control)

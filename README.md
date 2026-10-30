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
\n\n## Evidence status\n\nThis repository is the **primary executable prototype** for the residual-control idea. The companion manuscript lives in [residual-rl-linear-priors-paper](https://github.com/Hafiz-IIT/residual-rl-linear-priors-paper).\n\n## Results and limitations\n\nThe included demo and tests define the reproducible experiment. They do not establish empirical superiority over a broad control benchmark. The current implementation is intentionally small and deterministic; real robotic dynamics, disturbance distributions, and hardware validation are outside scope.\n\n## What is implemented vs planned\n\n**Implemented:** scalar linear prior, residual correction, action bounds, deterministic rollout, comparison scaffolding.\n\n**Not claimed:** learned-policy deployment, formal safety guarantees, benchmark-wide superiority, or physical validation.\n
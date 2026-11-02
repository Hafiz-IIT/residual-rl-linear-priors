# Residual RL with Linear Priors

A deterministic scalar residual-control prototype exploring how a bounded nonlinear correction changes a transparent linear baseline.

## Research question
Can a residual term complement a nominal linear controller while keeping the correction bounded and the baseline inspectable?

## Implemented
- scalar linear baseline controller
- configurable nonlinear residual correction
- residual and total-action saturation
- matched nominal-only versus residual-enabled rollout
- state, action, and stage-cost traces
- input validation and deterministic regression tests

## Run
    python demo.py
    python -m unittest discover -s tests -v

## Important terminology boundary
Despite the research direction's connection to residual reinforcement learning, the current implementation does **not** train an RL policy. The residual is a fixed nonlinear function. This repository is a control scaffold for future experiments, not a trained agent, robotic deployment, or safety guarantee.

## Evaluation
See [EVALUATION.md](EVALUATION.md) for proposed matched-baseline comparisons, metrics, and stress tests.

## Related work
- [Safe RL Action Gate](https://github.com/Hafiz-IIT/safe-rl-action-gate)
- [Koopman Control Lab](https://github.com/Hafiz-IIT/koopman-control-lab)
- [Hybrid LQR + RL Control](https://github.com/Hafiz-IIT/hybrid-lqr-rl-control)
- [Manuscript in preparation](https://github.com/Hafiz-IIT/residual-rl-linear-priors-paper)

"""Residual-control experiment with an explicit nominal baseline.

The residual is a fixed diagnostic function, not a trained reinforcement-
learning policy. The scalar plant is synthetic and intended for controlled
ablation and regression tests only.
"""
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Config:
    baseline_gain: float = 0.8
    residual_weight: float = 0.1
    residual_limit: float = 0.25
    action_limit: float = 1.0
    damping: float = 0.15

    def __post_init__(self):
        vals = (self.baseline_gain, self.residual_weight, self.residual_limit, self.action_limit, self.damping)
        if not all(math.isfinite(v) for v in vals):
            raise ValueError("configuration values must be finite")
        if self.residual_limit < 0 or self.action_limit <= 0 or not 0 <= self.damping <= 1:
            raise ValueError("invalid residual/action limit or damping")


def baseline(state: float, gain: float = 0.8) -> float:
    if not math.isfinite(state) or not math.isfinite(gain):
        raise ValueError("state and gain must be finite")
    return -gain * state


def residual(state: float, weight: float = 0.1, limit: float = 0.25) -> float:
    if not all(math.isfinite(v) for v in (state, weight, limit)) or limit < 0:
        raise ValueError("finite inputs and non-negative limit required")
    raw = -weight * state * abs(state)
    return max(-limit, min(limit, raw))


def control(state: float, config: Config | None = None, use_residual: bool = True) -> float:
    config = config or Config()
    correction = residual(state, config.residual_weight, config.residual_limit) if use_residual else 0.0
    raw = baseline(state, config.baseline_gain) + correction
    return max(-config.action_limit, min(config.action_limit, raw))


def rollout(initial: float, steps: int = 20, config: Config | None = None, use_residual: bool = True):
    if not math.isfinite(initial) or steps < 0:
        raise ValueError("initial state must be finite and steps non-negative")
    config = config or Config()
    states, actions, costs = [float(initial)], [], []
    for _ in range(steps):
        state = states[-1]
        action = control(state, config, use_residual=use_residual)
        actions.append(action)
        costs.append(state * state + 0.01 * action * action)
        states.append((1.0 - config.damping) * state + action)
    return {"states": states, "actions": actions, "costs": costs}

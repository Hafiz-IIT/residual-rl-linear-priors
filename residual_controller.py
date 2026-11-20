"""Residual-control experiment with an explicit nominal baseline.

The residual is a fixed diagnostic function, not a trained reinforcement-
learning policy. The scalar plant is synthetic and intended for controlled
ablation and regression tests only.
"""
from dataclasses import dataclass
import math


def _finite(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    try:
        normalized = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(normalized):
        raise ValueError(f"{name} must be a finite number")
    return normalized


@dataclass(frozen=True)
class Config:
    baseline_gain: float = 0.8
    residual_weight: float = 0.1
    residual_limit: float = 0.25
    action_limit: float = 1.0
    damping: float = 0.15

    def __post_init__(self):
        vals = (self.baseline_gain, self.residual_weight, self.residual_limit, self.action_limit, self.damping)
        for name, value in zip(("baseline_gain", "residual_weight", "residual_limit", "action_limit", "damping"), vals):
            _finite(name, value)
        if self.residual_limit < 0 or self.action_limit <= 0 or not 0 <= self.damping <= 1:
            raise ValueError("invalid residual/action limit or damping")


def baseline(state: float, gain: float = 0.8) -> float:
    state = _finite("state", state)
    gain = _finite("gain", gain)
    return -gain * state


def residual(state: float, weight: float = 0.1, limit: float = 0.25) -> float:
    state = _finite("state", state)
    weight = _finite("weight", weight)
    limit = _finite("limit", limit)
    if limit < 0:
        raise ValueError("limit must be non-negative")
    raw = -weight * state * abs(state)
    return max(-limit, min(limit, raw))


def control(state: float, config: Config | None = None, use_residual: bool = True) -> float:
    if not isinstance(use_residual, bool):
        raise ValueError("use_residual must be boolean")
    config = Config() if config is None else config
    if not isinstance(config, Config):
        raise TypeError("config must be a Config")
    correction = residual(state, config.residual_weight, config.residual_limit) if use_residual else 0.0
    raw = baseline(state, config.baseline_gain) + correction
    return max(-config.action_limit, min(config.action_limit, raw))


def rollout(initial: float, steps: int = 20, config: Config | None = None, use_residual: bool = True):
    initial = _finite("initial", initial)
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    config = Config() if config is None else config
    if not isinstance(config, Config):
        raise TypeError("config must be a Config")
    if not isinstance(use_residual, bool):
        raise ValueError("use_residual must be boolean")
    states, actions, costs = [float(initial)], [], []
    for _ in range(steps):
        state = states[-1]
        action = control(state, config, use_residual=use_residual)
        actions.append(action)
        cost = state * state + 0.01 * action * action
        next_state = (1.0 - config.damping) * state + action
        if not math.isfinite(cost) or not math.isfinite(next_state):
            raise OverflowError("rollout produced a non-finite state or cost")
        costs.append(cost)
        states.append(next_state)
    return {"states": states, "actions": actions, "costs": costs}

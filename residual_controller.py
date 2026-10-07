"""Minimal deterministic residual-control experiment."""

def baseline(state: float, gain: float = 0.8) -> float:
    return -gain * state

def residual(state: float, weight: float = 0.1) -> float:
    return weight * state * state if state < 0 else -weight * state * state

def control(state: float) -> float:
    return baseline(state) + residual(state)

def rollout(initial: float, steps: int = 20, damping: float = 0.15):
    state = float(initial)
    trace = [state]
    for _ in range(steps):
        action = control(state)
        state = (1.0 - damping) * state + action
        trace.append(state)
    return trace

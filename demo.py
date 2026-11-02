"""Compare nominal-only and nominal-plus-residual rollouts."""
from residual_controller import Config, rollout

config = Config()
prior = rollout(1.0, steps=20, config=config, use_residual=False)
hybrid = rollout(1.0, steps=20, config=config, use_residual=True)
print("Residual-control prototype (fixed residual; no trained RL policy)")
print("prior final state:", round(prior["states"][-1], 6))
print("hybrid final state:", round(hybrid["states"][-1], 6))
print("prior cumulative cost:", round(sum(prior["costs"]), 6))
print("hybrid cumulative cost:", round(sum(hybrid["costs"]), 6))

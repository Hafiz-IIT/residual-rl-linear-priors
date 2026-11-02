import unittest
from residual_controller import Config, baseline, control, residual, rollout

class ResidualRolloutTests(unittest.TestCase):
    def test_residual_is_bounded(self):
        cfg = Config(residual_limit=0.1)
        self.assertLessEqual(abs(residual(100.0, cfg.residual_weight, cfg.residual_limit)), 0.1 + 1e-12)

    def test_prior_only_ablation(self):
        cfg = Config()
        self.assertAlmostEqual(control(0.5, cfg, use_residual=False), baseline(0.5, cfg.baseline_gain))

    def test_rollout_shapes(self):
        result = rollout(1.0, steps=5)
        self.assertEqual(len(result["states"]), 6)
        self.assertEqual(len(result["actions"]), 5)
        self.assertEqual(len(result["costs"]), 5)

    def test_invalid_steps(self):
        with self.assertRaises(ValueError):
            rollout(1.0, steps=-1)

if __name__ == "__main__": unittest.main()

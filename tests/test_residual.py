import unittest
from residual_controller import baseline, control, rollout

class ResidualTests(unittest.TestCase):
    def test_residual_changes_action(self):
        self.assertNotEqual(baseline(1.0), control(1.0))

    def test_rollout_is_deterministic(self):
        self.assertEqual(rollout(1.0), rollout(1.0))

if __name__ == "__main__":
    unittest.main()

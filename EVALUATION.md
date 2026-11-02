# Evaluation protocol

## Objective
Compare the nominal linear baseline against the same controller with a bounded nonlinear residual under matched scalar-plant conditions.

## Policies
1. Nominal-only: residual disabled.
2. Residual-enabled: nominal controller plus fixed residual.
3. Residual-only diagnostic: disable the nominal term in a future controlled extension; do not treat this as a recommended controller.

## Metrics
Cumulative stage cost, final absolute state, peak absolute state, action saturation frequency, and divergence/non-finite rate.

## Ablations
Sweep baseline gain, residual coefficient, residual bound, action bound, damping, initial-state magnitude, and disturbance level. Use identical initial conditions and disturbances across policy variants.

## Current evidence
The code implements a fixed nonlinear residual, not a trained RL policy. The demo and tests are deterministic. No robotic experiment, benchmark superiority, or formal safety/stability result is claimed.

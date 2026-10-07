from residual_controller import baseline, control, rollout

initial = 1.0
base_action = baseline(initial)
res_action = control(initial)
trace = rollout(initial)

print("Residual-control research prototype")
print(f"initial_state={initial:.3f}")
print(f"baseline_action={base_action:.3f}")
print(f"residual_action={res_action:.3f}")
print(f"final_state={trace[-1]:.6f}")

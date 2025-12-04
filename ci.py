import wandb

print(f"The wandb version is {wandb.__version__}")
assert wandb.__version__=='0.23.1', f"Expected 2.1.01 but got {wandb.__version__}"

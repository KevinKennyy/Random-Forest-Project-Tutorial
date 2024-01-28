import subprocess

try:
    result = subprocess.run(["dot", "-V"], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
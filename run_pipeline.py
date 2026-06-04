import subprocess
import sys

def run_script(script_path):
    print(f"running script {script_path}")
    result = subprocess.run([sys.executable, script_path])
    if result.returncode == 0:
        print("no problem with output")
    else:
        print("we have an error")
        sys.exit(1)

run_script("src/ingest_bronze.py")
run_script("src/transform_silver.py")
run_script("src/transform_gold.py")
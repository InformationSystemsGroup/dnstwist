import sys, subprocess
from subprocess import Popen

def handler(event, context):

    domain_name = event.get('domain_name')

    print('================= STARTING DNSTWIST =================')

    print(f"Domain to Scan: {domain_name}")

    cmd = f"python ./dnstwist.py --r {domain_name}"
    print(f"Scan Command: {cmd}")

    try:
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Command executed successfully:")
            print(stdout.decode())
        else:
            print(f"Command failed with return code: {process.returncode}")
            print(stderr.decode())

    except:
        print("ERROR:")

    finally:
        print('================= DNSTWIST COMPLETE =================')
        return process.returncode

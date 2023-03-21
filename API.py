import subprocess


def get_chain_policy(chain):
    """
    Returns the policy of the specified chain in iptables.
    :param chain: name of chain
    :return: policy of chain
    """
    command = f'iptables -L {chain} -nv'
    output = run_command(command).split('\n')

    for line in output:
        if line.startswith('Chain'):
            if 'policy' in line:
                return line.split()[3]


def run_command(command):
    """
    Runs a shell command.
    :param command: command to run
    :return: output from the command
    """
    process = subprocess.Popen(command,
                               shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0].decode()

    return output


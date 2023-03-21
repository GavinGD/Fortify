import subprocess
import re


def get_chain_policy(chain):
    """
    Returns the policy of the specified chain in iptables.
    :param chain: name of chain
    :return: policy of chain
    """
    command = f'iptables -L {chain} -nv'
    output = __run_command(command).split('\n')

    for line in output:
        if line.startswith('Chain'):
            if 'policy' in line:
                return line.split()[3]


def get_iptables_rules(chain):
    """
    Gets rules from a chain in iptables and stores each rule in a list.
    :param chain: name of the chain to get rules from
    :return: list of iptables rules
    """
    # Build the iptables command to get the rules for the specified chain
    command = f'iptables -S {chain}'

    # Run the command and get the output
    output = __run_command(command)

    # Split the output by line to get each rule
    rules = output.strip().split('\n')

    # Return the list of rules
    return rules[1:]


def __extract_rule_field(rule, rule_dict, field, field_flag):
    """
    Extracts values from rules using regex.
    Ex:
        rule: -A INPUT -s 1.1.1.1/32 -p tcp -m tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
        To find '--state' use re.match(r'--state\b', rule)
        \b means word boundary
        r means raw string, normal escaping rules get suspended
        This would return the index that '--state' starts
        Then split the string and grab the next index in the split list

    :param rule: iptables rule
    :param rule_dict:  dictionary that holds values
    :param field: key for dictionary
    :param field_flag: regex pattern to use in re
    """
    match = re.search(field_flag, rule)

    if match:
        index = match.start()
        value = rule[index:].split()[1]
        rule_dict[field] = value
    else:
        rule_dict[field] = '-'


def __run_command(command):
    """
    Runs a shell command.
    :param command: command to run
    :return: output from the command
    """
    process = subprocess.Popen(command,
                               shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0].decode()

    return output


rules = get_iptables_rules("INPUT")
rules2 = []

for rule in rules:
    rule_dict = {}
    __extract_rule_field(rule, rule_dict, 'protocol', r'-p\b')
    __extract_rule_field(rule, rule_dict, 'source', r'-s\b')
    __extract_rule_field(rule, rule_dict, 'destination', r'-d\b')
    __extract_rule_field(rule, rule_dict, 'sport', r'--sport\b')
    __extract_rule_field(rule, rule_dict, 'dport', r'--dport\b')
    __extract_rule_field(rule, rule_dict, 'state', r'--state\b')
    __extract_rule_field(rule, rule_dict, 'target', r'-j\b')

    rules2.append(rule_dict)

for rule in rules2:
    print(rule)


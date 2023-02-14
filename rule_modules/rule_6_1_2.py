from . import common

def rule_6_1_2_check(filename, start_line, end_line, code_block):
    """
    rule_6_1_2: there must be an empty line after {
    """
    with open(filename, 'r') as fp:
        text = fp.readlines()
        if end_line >= len(text) - 1:
            return

        line = text[end_line+1]

        # file line number start from 1
        #print("line = {}".format(line))
        if common.check_empty_line(line):
        #if line != '\n':
            print("{}:{} '{}' violates rule rule 6.1.2. [!Change line here]".format(filename, end_line+2, line.replace('\n', '')))

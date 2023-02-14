def rule_6_1_1_check(filename, start_line, end_line, code_block):
    if code_block:
        lines = code_block.splitlines()
    else:
        with open(filename, 'r') as fp:
            text = fp.readlines()
            lines = text[start_line, end_line+1]

    for i in range(1, len(lines)-1):
        if len(lines[i]) >= 4 and lines[i][:4] != '    ':
            print("{}:{} '{}' violates rule rule 6.1.1 [!Indent error: Number of spaces]".format(filename, start_line+i+1, lines[i]))

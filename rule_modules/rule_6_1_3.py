from . import common
def rule_6_1_3_check(filename, start_line, func_name):
    with open(filename, 'r') as fp:
        text = fp.readlines()
        pos = start_line
        
        common.DEBUG_LOG(text[pos])
        while '(' not in text[pos]:
            pos += 1
        startline = text[pos]

        while ')' not in text[pos]:
            pos += 1
        endline = text[pos]

        start_pos = startline.find('(')
        end_pos = endline.find(')')
        
        common.DEBUG_LOG(startline, start_pos)
        if startline[start_pos+1] == ' ' or endline[end_pos-1] == ' ' :
            print("{}:{} '{}' violates rule rule 6.1.3 [!There should be no space before the first or after the last parameter]".format(filename, start_line+1, text[start_line].replace('\n', '')))

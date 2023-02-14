import ctags
from ctags import CTags, TagEntry

global DEBUG_LEVEL
DEBUG_LEVEL = 0

def DEBUG_LOG(*args):
    if DEBUG_LEVEL:
        print(*args)
        
def check_empty_line(l):
    if l != '\n' and l != '':
        return 1
    return 0

def L1_code_block_list(filename):
    ret  = []
    block_item = []
    bracket = 0
    check_tag = 0

    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for i in range(len(lines)):
            if '{' in lines[i]:
                bracket += 1
                if not check_tag:
                    block_item.append(i)
                    check_tag = 1

            if '}' in lines[i]:
                bracket -= 1
                if not bracket and check_tag:
                    block_item.append(i)
                    block_item.append(''.join(lines[block_item[0]:block_item[1]+1]))
                    ret.append(block_item)
                    block_item = []
                    check_tag = 0

    # return [begin_line, end_line, code_block_text] tuples
    #print(ret)
    return ret

def func_list(filename, tagFile):
    DEBUG_LOG(filename, tagFile)
    ret = []
    entry = TagEntry()
    while tagFile.next(entry):
        """
        print(entry['name'])
        print(entry['kind'])
        print(entry['file'])
        print(entry['pattern'])
        print(entry['lineNumber'])
        print(entry['fileScope'])
        """
        if entry['file'].decode("utf-8") == filename and entry['kind'] == b'function':
            ret.append([filename, entry['lineNumber']-1, entry['name'].decode("utf-8")])

    return ret


#L1_code_block_list("sample_c_files/sample.c")

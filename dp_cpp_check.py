import ctags
from ctags import CTags, TagEntry
import sys

from rule_modules import common
from rule_modules import rule_6_1_1
from rule_modules import rule_6_1_2
from rule_modules import rule_6_1_3

global tagFile

common.DEBUG_LEVEL = 0


try:
    tagFile = CTags('tags')
except:
    sys.exit(1)

"""
print(tagFile['name'])
print(tagFile['author'])
print(tagFile['format'])
"""

# entry = TagEntry()
# #status = tagFile.first(entry)
# 
# while tagFile.next(entry):
# #    if status:
#     # Available TagEntry keys:
#     #  name - name of tag
#     #  file - path of source file containing definition of tag
#     #  pattern - pattern for locating source line (None if no pattern)
#     #  lineNumber - line number in source file of tag definition (may be zero if not known)
#     #  kind - kind of tag (none if not known)
#     #  fileScope - is tag of file-limited scope?
#  
#     # Note: other keys will be assumed as an extension key and will
#     # return None if no such key is found
#  
#     #help(entry)
#     """
#     print(entry['name'])
#     print(entry['kind'])
#     print(entry['kind'] == b'function')
#     print(entry['file'])
#     print(entry['pattern'])
#     print(entry['lineNumber'])
#     print(entry['fileScope'])
#     """
#     #print(entry[b'Function_one']['count'])
#     #print(entry['list'])


def rule_6_1_1_run(filename):
    code_blocks = common.L1_code_block_list(filename)
    for cb in code_blocks:
        rule_6_1_1.rule_6_1_1_check(filename, cb[0], cb[1], cb[2])

def rule_6_1_2_run(filename):
    code_blocks = common.L1_code_block_list(filename)
    for cb in code_blocks:
        rule_6_1_2.rule_6_1_2_check(filename, cb[0], cb[1], cb[2])

def rule_6_1_3_run(tagFile, filename):
    func_list = common.func_list(filename, tagFile)
    common.DEBUG_LOG(func_list)
    for f in func_list:
        rule_6_1_3.rule_6_1_3_check(f[0], f[1], f[2])


rule_6_1_1_run("sample_c_files/sample.c")
rule_6_1_2_run("sample_c_files/sample.c")
rule_6_1_3_run(tagFile, "sample_c_files/sample.c")


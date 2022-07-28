from utils import buildCFG

fpCfiles='/home/hungphd/git/llvm-cfg-to-json/testCFiles/example.cpp'
cfgs = buildCFG(fpCfiles)

for cfg in cfgs:
    print "\n[+] Function: ", cfg[0]
    print cfg[1].printer()
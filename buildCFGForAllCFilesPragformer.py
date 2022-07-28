from utils import buildCFG
from glob import glob
import os,traceback

def getStringDisplayCFG(cfgs):
    lstStrCFGs=[]
    for cfg in cfgs:
        try:
            lstStrCFGs.append('#Function::: {}'.format(cfg[0]))
            lstStrCFGs.append(cfg[1].printer())
            lstStrCFGs.append('#EndGraph for Function {}'.format(cfg[0]))
        except Exception as e:
            pass

    return lstStrCFGs


fpCfiles='/home/hungphd/git/llvm-cfg-to-json/testCFiles/example.cpp'
fopCFiles='/home/hungphd/git/Open_OMP/Parallel_Augmented/'
fopCFG='/home/hungphd/git/Open_OMP/cfg_pycparser/'
fpLogPycParserCFG='/home/hungphd/git/Open_OMP/log_pycparser_cfg.txt'
# os.mkdir(fopCFG)
lstFpCFiles=glob(fopCFiles+'*.c')
indexProgram=0
indexCorrect=0
indexIncorrect=0
f1 = open(fpLogPycParserCFG, 'w')
f1.write('')
f1.close()
import pickle
for fpItem in lstFpCFiles:
    nameCFile=os.path.basename(fpItem)
    indexProgram+=1
    try:

        indexCorrect += 1
        strMessage='{}\t{}\t{}'.format(indexCorrect,nameCFile,'OK')
        f1 = open(fpLogPycParserCFG, 'a')
        f1.write(strMessage + '\n')
        f1.close()
        cfgs = buildCFG(fpItem)
        lstItemStrCFGs=getStringDisplayCFG(cfgs)
        fpItemPKL=fopCFG+nameCFile.replace('.c','.pkl.txt')
        # fSave=open(fpItemPKL,'wb')
        # pickle.dump(cfgs,fSave)
        # fSave.close()
        f1=open(fpItemPKL,'w')
        f1.write('\n'.join(lstItemStrCFGs))
        f1.close()
        print('OK {} {}/{}'.format(nameCFile,indexCorrect,indexProgram))
    except Exception as e:
        traceback.print_exc()
        input('aaa ')
        indexIncorrect += 1
        strExceptionMessage='{}\t{}\t{}'.format(indexIncorrect,nameCFile,traceback.format_exc().replace('\n',' _EL_ '))
        f1=open(fpLogPycParserCFG,'a')
        f1.write(strExceptionMessage+'\n')
        f1.close()
        print('Failed {} {}/{}'.format(nameCFile,indexCorrect, indexProgram))



# cfgs = buildCFG(fpCfiles)
#
# for cfg in cfgs:
#     print "\n[+] Function: ", cfg[0]
#     print cfg[1].printer()
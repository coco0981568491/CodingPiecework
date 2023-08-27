"""
我可以自己在code中手動更改A_B資料夾檔名（input1, -folder “folder name”）、NAVD第一張“SeriesNumber"(input2, -NAVDsn “a1,b1,c1,d1”)、"InstanceNumber(input3, -NAVDin “a2,b2,c2,d2”)"、每個NAVD需求的影像張數(input4, -NAVDfillenum “c1,c2,c3,c4”)（如想要IM-0002-0006.dcm為第一張，資料夾需要10張影像，那麼最後資料夾內會自動收入IM-0002-0006.dcm～IM-0002-0015.dcm）
最後自動生成四個“N”,"A","V","D"資料夾
"""

import os
import time
from argparse import ArgumentParser

def main(FOLDER, NAVD_SN, NAVD_IN, NAVD_FN):
    
    # get NAVD inputs and pad the numbers with zeros.
    N_SN, A_SN, V_SN, D_SN = NAVD_SN[0].zfill(4),NAVD_SN[1].zfill(4),NAVD_SN[2].zfill(4),NAVD_SN[3].zfill(4)
    N_IN, A_IN, V_IN, D_IN = int(NAVD_IN[0]),int(NAVD_IN[1]),int(NAVD_IN[2]),int(NAVD_IN[3])
    N_FN, A_FN, V_FN, D_FN = int(NAVD_FN[0]),int(NAVD_FN[1]),int(NAVD_FN[2]),int(NAVD_FN[3])
#     N_INend,A_INend,V_INend,D_INend = str(N_IN+N_FN-1).zfill(4),str(A_IN+A_FN-1).zfill(4),str(V_IN+V_FN-1).zfill(4),str(D_IN+D_FN-1).zfill(4)
#     N_INst,A_INst,V_INst,D_INst = str(N_IN).zfill(4),str(A_IN).zfill(4),str(V_IN).zfill(4),str(D_IN).zfill(4)

    N_INend,A_INend,V_INend,D_INend = N_IN+N_FN-1,A_IN+A_FN-1,V_IN+V_FN-1,D_IN+D_FN-1
    
#     print(N_INend,A_INend,V_INend,D_INend)
#     print(N_INst,A_INst,V_INst,D_INst)
    
    # enter the folder to find the .dcm filles.
    # dcms = [f for f in os.listdir(f"./{FOLDER}")]
    
    # for folder N
    os.system(f"mkdir ./{FOLDER}/N")
    # os.system("for i in {%d..%d}; do mv ./%s/IM-%s-$(printf %04d $i).dcm ./%s/N; done"%(N_IN,N_INend,FOLDER,N_SN,FOLDER))
    for i in range(N_IN, N_INend+1):
        os.system("mv ./%s/IM-%s-%s.dcm ./%s/N"%(FOLDER,N_SN,str(i).zfill(4),FOLDER))
    
    # for folder A
    os.system(f"mkdir ./{FOLDER}/A")
    # os.system("for i in 'seq %d 1 %d'; do mv ./%s/IM-%s-$(printf %04d $i).dcm ./%s/A; done"%(A_IN,A_INend,FOLDER,A_SN,FOLDER))
    for i in range(A_IN, A_INend+1):
        os.system("mv ./%s/IM-%s-%s.dcm ./%s/A"%(FOLDER,A_SN,str(i).zfill(4),FOLDER))
    
    # for folder V
    os.system(f"mkdir ./{FOLDER}/V")
    # os.system("for i in 'seq %d 1 %d'; do mv ./%s/IM-%s-$(printf %04d $i).dcm ./%s/V; done"%(V_IN,V_INend,FOLDER,V_SN,FOLDER))
    for i in range(V_IN, V_INend+1):
        os.system("mv ./%s/IM-%s-%s.dcm ./%s/V"%(FOLDER,V_SN,str(i).zfill(4),FOLDER))
        
    # for folder D
    os.system(f"mkdir ./{FOLDER}/D")
    # os.system("for i in 'seq %d 1 %d'; do mv ./%s/IM-%s-$(printf %04d $i).dcm ./%s/D; done"%(D_IN,D_INend,FOLDER,D_SN,FOLDER))
    for i in range(D_IN, D_INend+1):
        os.system("mv ./%s/IM-%s-%s.dcm ./%s/D"%(FOLDER,D_SN,str(i).zfill(4),FOLDER))
        
# input parser
parser=ArgumentParser()
parser.add_argument('-folder', dest='folder', help='資料夾名稱')

parser.add_argument('-NAVDsn', dest='NAVDsn', help='依照N,A,V,D順序將對應指定的SeriesNumber寫成一個逗號分隔字串。舉例：假設N指定SeriesNumber為2，A指定5，V指定4，D指定3，這裡就輸入2,5,4,3，並注意中間不可以空格，僅用逗號分開。')

parser.add_argument('-NAVDin', dest='NAVDin', help='依照N,A,V,D順序將對應指定的InstanceNumber寫成一個逗號分隔字串。舉例：假設N指定InstanceNumber為2，A指定5，V指定4，D指定3，這裡就輸入2,5,4,3，並注意中間不可以空格，僅用逗號分開。')

parser.add_argument('-NAVDfilenum', dest='NAVDfilenum', help='依照N,A,V,D順序將對應指定的影像數量寫成一個逗號分隔字串。舉例：假設N指定要2張，A指定5張，V指定4張，D指定3張，這裡就輸入2,5,4,3，並注意中間不可以空格，僅用逗號分開。')

# extract the args values.
args = parser.parse_args()
FOLDER = args.folder
NAVD_SN = [i for i in args.NAVDsn.split(",")]
NAVD_IN = [i for i in args.NAVDin.split(",")]
NAVD_FN = [i for i in args.NAVDfilenum.split(",")]

# execute the main func.
main(FOLDER, NAVD_SN, NAVD_IN, NAVD_FN)
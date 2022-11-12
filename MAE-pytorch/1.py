import numpy as np
import pandas as pd

fi = open('output/mae_pretraining/log.txt',"r",encoding="utf-8")
fo = open("log-提取版.txt","w",encoding="utf-8")

wflag =False                #写标记
newline = []                #创建一个新的列表


for line in fi :            #按行读入文件，此时line的type是str
    if "【" in line:        #重置写标记
        wflag =False
    print(line)
    if "train_loss" in line:     #检验是否到了要写入的内容
        print('yes')
        wflag = True
        print(line[line.index("train_loss"):line.index("train_loss_scale")-3])
        newline.append(line[line.index("train_loss"):line.index("train_loss_scale")-3])
        fo.write(line[line.index("train_loss"):line.index("train_loss_scale")-3])
        # fo.write('\n')

strlist = "".join(newline)      #合并列表元素
newlines = str(strlist)         #list转化成str



fo.close()
fi.close()
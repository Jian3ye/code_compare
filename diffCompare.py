#!/usr/bin/python
#coding=utf-8

import difflib
def compare(a1,a2):
    result = []
        # 读取两文件1.txt与2.txt
    with open(a1, "rb") as f:
        data1 = f.read()
    with open(a2, "rb") as f:
        data2 = f.read()
    text1_lines = data1.splitlines() #以行进行分割
    text2_lines = data2.splitlines()
    #d = difflib.Differ()#创建Differ对象
    #diff = (d.compare(text1_lines, text2_lines))
    #return'\n'.join(list(str(diff)))
    ratio1 = difflib.SequenceMatcher(None,text1_lines,text2_lines).ratio()
    if ratio1 == 1:
        result.append(a1+"和"+a2+"一致")
    else:
        result.append(a1 + "和" + a2 + "不一致")

    return "\n".join(result)
if __name__ == '__main__':
    a = compare("C:\\Users\\liyangmei\\Desktop\\test\\sge800app","C:\\Users\\liyangmei\\Desktop\\test1\\sge800app")
    print(a)


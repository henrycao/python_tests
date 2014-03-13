#!/usr/bin/env python

from hashlib import md5

dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z',36:'A',37:'B',38:'C',39:'D',40:'E',41:'F',42:'G',43:'H',44:'I',45:'J',46:'K',47:'L',48:'M',49:'N',50:'O',51:'P',52:'Q',53:'R',54:'S',55:'T',56:'U',57:'V',58:'W',59:'X',60:'Y',61:'Z',62:'!',63:'@',64:'#',65:'$',66:'%',67:'^',68:'&',69:'*',70:'(',71:')',72:'_',73:'+',74:'-',75:'=',76:'[',77:']',78:'\\',79:'{',80:'}',81:'|',82:';',83:'\'',84:':',85:'"',86:',',87:'.',88:'/',89:'<',90:'>',91:'?',92:'`',93:'~'}

def convert(num,base):
    num = abs(num)
    remainder = num % base
    if num >= base:
        convert(num / base, base)
    converted_list.append(remainder)

def format_print(num,base,len):
    if num < 0:
        result = '-'
    else:
        result = ''
    convert(num, base)

    for item in converted_list:
        if item in dic.keys():
            item = dic[item]
        item = str(item)
        result += item
    return result.zfill(len)

def calc_md5(string):
	m = md5()
	m.update(string)
	return m.hexdigest()	

file_obj = open('./md5_result','a')
base = 94
len = 6
for num in range(0,100000):
	converted_list = []
	string = format_print(num,base,len)
	file_obj.write(string + " " + calc_md5(string) + "\n")
file_obj.close()

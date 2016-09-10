import os
import codecs
import re

p=re.compile('<table class="simple" width="100%" cellpadding="0" cellspacing="0">[\s\S]*</table>[\s]<table width="100%">',re.IGNORECASE)

# находит названия и нужную информацию
p2=re.compile('<td class="simple"[ \S]*</td>',re.IGNORECASE)

# находит годы планируемого ремонта
p3=re.compile('<strong[ \S]*</strong></p><p class="date">[\S]+',re.IGNORECASE)

fout = codecs.open(u'База данных.txt','w','utf-8')

p4=re.compile('<td class="simple"[ \S]*">')
p5=re.compile('<td class="simple">')

p6=re.compile('<strong>')
p7=re.compile('</strong></p><p class="date">')

# Получить список файлов из папки
folder='data'
files=os.listdir(path=folder)

for f in files:
    d=open(folder+'\\'+f,'r')
    c=d.read()
    tables=p.findall(c);
    if len(tables)>=1:
        data=p2.findall(tables[0])

        additional=p3.findall(tables[0])
        # numbers=sum(list(map((lambda x: x[8:-5].split(',')), p2.findall(tables[0]))),[])
        # Найти в файле вторую таблицу <table>...</table>
        # Распарсить и вытащить первый стоблец "Интервалы домов"
        # Распарсить их в список
        
        ndata=[]
        for x in data:
            t=(re.sub(p4,r'',x))[:-5]
            ndata.append(re.sub(p5,r'',t))

        ndata[1]='\t'.join(ndata[1].split(','))

        nadd=[]
        for x in additional:
            t=(re.sub(p6,r'',x))
            nadd.append(re.sub(p7,r'\t',t))

        #print (nadd)
        # Сохранить в формате
        # УЛИЦА\tномер дома\tКапитальный ремонт жилого дома\tГод постройки\tКоличество этажей\tКоличество подъездов\tИнформация о наличии лифтов, шт.\tВсего квартир в доме, шт.\tПолезная площадь дома, кв.м.\tПроцент износа по оценке БТИ\tПроцент износа по техпаспорту\tУправляющая компания\tКонтактный телефон\t
        fout.write('\t'.join(ndata)+'\t'+'\t'.join(nadd))
        fout.write('\n')
    
    d.close()

fout.close()

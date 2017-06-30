'''
Created on 2017年6月28日

@author: wyq
'''
import csv
import codecs

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)

    
    def output_html(self):
        fout = open("output.html","w", encoding="utf-8")
        
        fout.write("<html>\n")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>\n")
        fout.write("<body>\n")
        fout.write("<div>\n")
        
        for data in self.datas:
            fout.write("<tr>\n")
            for element in data:
                fout.write("<tr>\n")
#                 print(len(element))
#                 print(element)
                if len(element) == 2:
                    fout.write("<p>%s</p>\n"%element[0])
                    fout.write("<p><img src=%s></p>\n"%element[1].replace("//","http://"))
                else:
                    fout.write("<p>%s</p>\n" %element)
                fout.write("</tr>\n")
                fout.write("<br/>")
            fout.write("</tr>\n")
        
        fout.write("</div>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")
        
        fout.close()

    
    def output_excel(self):
        with codecs.open("test1.csv", "w+", "utf_8_sig") as csvfile:
            cfile = csv.writer(csvfile, dialect="excel")
            for data in self.datas:
                cfile.writerow(data.pop())

    
    def output_txt(self):
        f = open("duanzi.txt","w")
        for data in self.datas:
            f.write(str(data))
            
        f.close()
    
    
            
    
    
    
    
    




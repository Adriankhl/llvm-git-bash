import csv
import pandas as pd
import sys

pd.set_option('display.max_rows', 100)

def read_file(env = 'Env.csv'):
    a = []
    with open(env) as f:
        data = csv.reader(f)
        for i, row in enumerate(data):
            a.append([])
            for j, column in enumerate(row):
                if j < 5:
                    continue
                elif j == 5:
                    a[i].append(column)
                    a[i].append("")
                else:
                    a[i][1] += column
    return a 
    
def process_string(a):
    df = pd.DataFrame(a).dropna()
    s = pd.Series(df[1].values,index=df[0].values)
    s = s.drop("Key")
    #s = s.drop("CommonProgramFiles(x86)")
    #s = s.drop("ProgramFiles(x86)")
    s = '\'' + s + '\''

    s1 = s.copy(deep=True)
    s1 = s1.str.replace('C:\\','/c/', regex=False)
    s1 = s1.str.replace('D:\\','/d/', regex=False)
    s1 = s1.str.replace('\\','/', regex=False)
    s1 = s1.str.replace(';','\':\'', regex=False)
    s1 = s1.str.replace(":\'\'", '', regex=False)
    s1 = s1.str.replace("\'\'", '', regex=False)
    s1 = s1.rename({"Path":"PATH"})
    s1['PATH'] = s1['PATH']

    s2 = s1[['PATH', 'LIB', 'INCLUDE']].copy(deep=True)
    s2['PATH'] = '\'' + s1['VSINSTALLDIR'].replace("'", '') + 'VC/Tools/Llvm/bin' + '\':' + s2['PATH']
    

    s3 = s2.copy(deep=True)
    s3 = s3.str.replace('x86','x64', regex=False)
    s3 = s3.str.replace('(x64)','(x86)', regex=False)
    return s, s1, s2, s3
    

def save_export(s, f, original_path=False):
    if original_path:
        file = open(f,'w')
        for items in s.iteritems():
            if (items[0] == 'PATH'):
                file.write('export ' + items[0] + '=' + items[1] + ':$' + items[0] + '\n')
            else:
                file.write('export ' + items[0] + '=' + items[1] + '\n')
        file.close()
        return original_path
    else: 
        file = open(f,'w')
        for items in s.iteritems():
            file.write('export ' + items[0] + '=' + items[1] + '\n')
        file.close()
        return original_path
         


def save_files(s, s1, s2, s3, f='env_original.sh', f1='env_all.sh', f2='env.sh', f3='env64.sh'):
    save_export(s, f, original_path=False)
    save_export(s1, f1, original_path=False)
    save_export(s2, f2, original_path=True)
    save_export(s3, f3, original_path=True)
    return True


if __name__ == "__main__":
    infile = sys.argv[1]
    data = read_file(env=infile)
    out1, out2, out3, out4 = process_string(data) 
    save_files(s=out1, s1=out2, s2=out3, s3=out4, f='env_original.sh', f1='env_all.sh', f2='env.sh', f3='env64.sh')

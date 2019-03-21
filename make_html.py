import pandas as pd
import sys

df = pd.read_csv(sys.argv[1],sep="\t",index_col=0)

def output_row(mlist):
	out = "<tr>\n"
	ss = list(map(lambda x:"\t<td>"+str(x)+"</td>",mlist))
	out += "\n".join(ss)
	out += "</tr>\n"
	return out


def output_table(csv_file,motif_logo_dict):
	rows = []
	for line in open(csv_file).readlines()[1:]:
		line = line.strip()
		line = line.split(",")
		motif_name = line[0]
		motif_name = motif_name.replace("_",".")
		path = motif_logo_dict[motif_name]
		line = ['<img src="'+path+'" height=40 width=100></img>'] + line
		rows.append(output_row(line))
	return rows
lines = []
for i in df.index:
	motif_name = i
	motif_logo = "./"+sys.argv[2]+"/"+i+".png"
	line = [motif_name,df.at[i,'p-value'],df.at[i,'PosMatches'],df.at[i,'PosNonMatches'],df.at[i,'NegMatches'],df.at[i,'NegNonMatches'],df.at[i,'Enrichment']]
	line = ['<img src="'+motif_logo+'" height=40 width=100></img>'] + line
	lines.append(output_row(line))


def write_file(file_name,message):
	out = open(file_name,"wt")
	out.write(message)
	out.close()

template_html = open("template.html").readlines()


template_html[36] = "\n".join(lines)

write_file(sys.argv[3],"".join(template_html))






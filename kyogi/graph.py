import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

#グラフをプロットするための関数
def Plot_Graph_ranking(x,y,a,b,c,d,e,f,g,h,l,m,n,o):
	plt.switch_backend("AGG")        #スクリプトを出力させない

	fig,ax = plt.subplots(2,4,figsize=(13.5,6))
	#ランキング
	ax[0,0].set_title('Ranking')
	ax[0,0].set_xlabel('Name')
	ax[0,0].set_ylabel('Correct')
	ax[0,0].set_yticks(np.arange(1, 11, 1))
	ax[0,0].bar(x[0:5], y[0:5])

	#各問題のクリア数
	ax[0,1].set_title('Clear_Question')
	ax[0,1].set_xlabel('Qnumber')
	ax[0,1].set_xticks(np.arange(1, 6, 1))
	ax[0,1].set_ylabel('Correct')
	ax[0,1].set_yticks(np.arange(1, 50, 1))
	ax[0,1].bar(a, b)

	#Q1のクリア数
	for xval, yval in zip(c[0:5],d):
		ax[0,2].text(xval, yval, yval, ha='center', va='bottom')
	ax[0,2].set_title('Question1_time')
	ax[0,2].set_xlabel('Name')
	ax[0,2].set_ylabel('Time(sec)')
	ax[0,2].set_yticks(np.arange(0, 500, 50))
	ax[0,2].bar(c[0:5], d[0:5])

	#Q2のクリア数
	for xval, yval in zip(e[0:5],f):
		ax[0,3].text(xval, yval, yval, ha='center', va='bottom')
	ax[0,3].set_title('Question2_time')
	ax[0,3].set_xlabel('Name')
	ax[0,3].set_ylabel('Time(sec)')
	ax[0,3].set_yticks(np.arange(0, 500, 50))
	ax[0,3].bar(e[0:5], f[0:5])

	#Q3のクリア数
	for xval, yval in zip(g[0:5],h):
		ax[1,0].text(xval, yval, yval, ha='center', va='bottom')
	ax[1,0].set_title('Question3_time')
	ax[1,0].set_xlabel('Name')
	ax[1,0].set_ylabel('Time(sec)')
	ax[1,0].set_yticks(np.arange(0, 500, 50))
	ax[1,0].bar(g[0:5], h[0:5])

	#Q4のクリア数
	for xval, yval in zip(l[0:5],m):
		ax[1,1].text(xval, yval, yval, ha='center', va='bottom')
	ax[1,1].set_title('Question4_time')
	ax[1,1].set_xlabel('Name')
	ax[1,1].set_ylabel('Time(sec)')
	ax[1,1].set_yticks(np.arange(0, 500, 50))
	ax[1,1].bar(l[0:5], m[0:5])

	#Q5のクリア数
	for xval, yval in zip(n[0:5],o):
		ax[1,2].text(xval, yval, yval, ha='center', va='bottom')
	ax[1,2].set_title('Question5_time')
	ax[1,2].set_xlabel('Name')
	ax[1,2].set_ylabel('Time(sec)')
	ax[1,2].set_yticks(np.arange(0, 500, 50))
	ax[1,2].bar(n[0:5], o[0:5])

	plt.tight_layout()               #レイアウト
	graph = Output_Graph()           #グラフプロット
	return graph

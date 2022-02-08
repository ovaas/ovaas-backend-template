import os, json, zipfile

# jsonファイルの階層にあったファイルをzipに圧縮する

# json読み込み
fileName = 'fileMap'

# zipファイル名
zipName = 'zipData'

f = open(f'{fileName}.json', 'r', encoding="utf-8_sig")
json_dict = json.load(f)

folders = []
files = []

# jsonを再帰的に探索してリストを作成する
def scan(json,path):
    i = True
    for mykey in json['folder'].keys():
        i = False
        if path == '':
            scan(json['folder'][mykey],mykey)
        else:
            scan(json['folder'][mykey],f"{path}\{mykey}")
    if i :# これ以上、下が無ければ追加
        folders.append(path)
    for file in json['file']:
        if path == '':
            files.append(file)
        else:
            files.append(f"{path}\{file}")
    return json

scan(json_dict,'')


# 確認用
# for i in folders:
#     print(i)
# for i in files:
#     print(i)

# リスト上のファイルをすべて圧縮
with zipfile.ZipFile(f'{zipName}.zip','w', compression=zipfile.ZIP_DEFLATED) as myzip:
    for i in folders:
        myzip.write(os.path.join(json_dict['filePath'], i),arcname=i)
    for i in files:
        myzip.write(os.path.join(json_dict['filePath'], i),arcname=i)

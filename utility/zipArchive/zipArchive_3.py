import os, json, zipfile,filecmp
import argparse

# jsonファイルの階層にあったファイルを除外してzipに圧縮する
# フォルダーの場合は階層下を全て除外

# 実行
# Python zipArchive.py . .fileBlackList.json dataZip
# Python zipArchive.py -h

parser = argparse.ArgumentParser()

# 引数
parser.add_argument('readBestination', help='圧縮するディレクトリーパス') 
parser.add_argument('blackListJson', help='blackリストjsonファイル名パス') 
parser.add_argument('zipName', help='圧縮後のファイル名')

args = parser.parse_args()

# json読み込み
blackListJson = args.blackListJson

# zipファイル名
zipName = args.zipName

# 読み込み先
readBestination = args.readBestination

f = open(blackListJson, 'r', encoding="utf-8_sig")
json_dict = json.load(f)


json_blackFolderList = json_dict['folder']
json_blackFileList = json_dict['file']

blackFolderList = set([])
blackFileList = set([])

FolderList = set([])
FileList = set([])

# 存在するか確認する
for i in json_blackFolderList:
    if os.path.isdir(os.path.join(readBestination, i)):
        blackFolderList.add(os.path.join(readBestination, i))
for i in json_blackFileList:
    if os.path.isfile(os.path.join(readBestination, i)):
        blackFileList.add(os.path.join(readBestination, i))

# blackFolderの階層下のディレクトリーを取得
for blackFolder in json_blackFolderList:
    for folder, subfolders, files in os.walk(os.path.join(readBestination, blackFolder)):
        blackFolderList.add(folder)
        for file in files:
            blackFileList.add(os.path.join(folder,file))

# すべでのディレクトリーを取得
for folder, subfolders, files in os.walk(readBestination):
    FolderList.add(folder)
    for file in files:
        FileList.add(os.path.join(folder,file))

#差集合
FolderList = FolderList.difference(blackFolderList)
FileList = FileList.difference(blackFileList)


# for Folder in FolderList:
#     print(Folder)
# for File in json_blackFileList:
#     print(File)


# ファイルを圧縮
with zipfile.ZipFile(f'{zipName}.zip','w', compression=zipfile.ZIP_DEFLATED) as myzip:
    for Folder in FolderList:
        myzip.write(Folder)
    for File in FileList:
        myzip.write(File)
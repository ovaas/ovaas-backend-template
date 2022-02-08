# zip圧縮pyファイルの説明

## fileBlackList.json
archiveFileScan.pyでファイルをfileMap.jsonに書き込む際除外するファイルを書き込む

## fileMap.json
archiveFileScan.pyでファイルを読み込んだ際fileMap.jsonに書きこまれる

## archiveFileScan.py
archiveFileScan.py自分の階層から含まれる下のファイル・ディレクトリーをfileMap.jsonに書き込む

## zipArchive.py
fileMap.jsonの内容のファイル・ディレクトリーを圧縮

## zipArchive_2.py
fileMap.jsonの内容以外のファイル・ディレクトリーを圧縮

## zipArchive_3.py
zipArchive_2.pyをオプションでをで指定できるようにした

## writeConfiguration.py
コンフィグ関数の試し、

## modelAdd.py
writeConfiguration.pyで生成したjsonをターゲットjsonに追加するプログラム

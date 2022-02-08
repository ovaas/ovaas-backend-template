import os, json

# 実行した場所のファイル階層をjaonにまとめる

folder = os.getcwd()
fileName = 'fileMap'
json_data = {'filePath':folder}


def scan_unit(folder):
    files = os.listdir(folder)
    files_dir = [f for f in files if os.path.isdir(os.path.join(folder, f))]
    files_file = [f for f in files if os.path.isfile(os.path.join(folder, f))]
    return files_dir, files_file

# 再帰的に探索
def scan(folder):
    json_data = {}
    files_dir, files_file = scan_unit(folder)
    json_data['file'] = files_file
    json_data['folder'] = {}
    for fil in files_dir:
        files_path = f"{folder}\{fil}"
        json_data['folder'][fil] = scan(files_path)
    return json_data

json_data.update(scan(folder))

# JSONオブジェクトを作成
j = json.dumps(json_data)

# 保存
with open(f'{fileName}.json', mode='wt', encoding='utf-8') as f:
  json.dump(json_data, f, ensure_ascii=False, indent=2)



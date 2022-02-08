import json
import ndjson
# コンフィグ関数

# y/n 関数


def yes_no_input(explanation):
    while True:
        choice = input(f"{explanation} [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


information = {}

redo = False
while(not redo):
    information.clear()

    # 新しいfunction_name を入れる
    # ・ モデルの name と path を入力 複数可
    information["function_name"] = input('function_name:')
    models = []
    loop = True
    while(loop):
        models.append({
            "model_name": input('model_name:'),
            "mode_path": input('mode_path:')
        })
        loop = yes_no_input('Is there still?')
    information["models"] = models

    # env の name host と name port を入力
    # ・ key と value を入力 複数可
    information["env_name_ip"] = input('env_name_ip:')
    information["env_name_port"] = input('env_name_port:')
    envs = []
    loop = True
    while(loop):
        envs.append({
            "key": input('key:'),
            "value": input('value:')
        })
        loop = yes_no_input('Is there still?')
    information["envs"] = envs

    print(information)
    redo = yes_no_input('Is this okay?')

# JSONオブジェクトを作成
j = json.dumps(information)

# 保存
with open('test_new.json', mode='wt', encoding='utf-8') as f:
    json.dump(information, f, ensure_ascii=False, indent=2)


######
# 生成フォーマット
'''
{
  "function_name": "function_name",
  "models": [
    {
      "model_name": "model_name",
      "mode_path": "mode_path"
    }
  ],
  "env_name_ip": "env_name_ip",
  "env_name_port": "env_name_port",
  "envs": [
    {
      "key": "XXXXXXX",
      "value": "PPPPPPP"
    }
  ]
}
'''
######

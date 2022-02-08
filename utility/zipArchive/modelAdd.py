import json
import argparse
from os import remove

#writeConfiguration.pyで生成したjsonをターゲットjsonに追加するプログラム


# C:/Users/swnzx/AppData/Local/Programs/Python/Python39/python.exe c:/VisualStudioWorkspace/code/OVaaS_2/ovaas-backend/modelAdd.py C:\VisualStudioWorkspace\code\OVaaS_2\ovaas-backend\target.json C:\VisualStudioWorkspace\code\OVaaS_2\ovaas-backend\test_new.json

parser = argparse.ArgumentParser(
    description='ターゲットjsonにaddjsonの要素をmodelsに入れるプログラム')

parser.add_argument('target_json', help='ターゲットjsonパス')    # 必須の引数を追加
parser.add_argument('add_json', help='modelsに入れるjsonパス')
parser.add_argument('--model_server_version',default="latest", help="モデルのバージョン(デフォルト:latest)")


args = parser.parse_args()
model_server_version = args.model_server_version

# json読み込み
f = open(args.target_json, 'r')
target_dict = json.load(f)
f = open(args.add_json, 'r')
add_json = json.load(f)

# print(target_dict)
# print(add_json)

############################################################
# backend_config最後尾を取得
backend_config_end = target_dict['backend_config'][-1]

# backend_config最後尾のmodels取得
models = backend_config_end['models']

# backend_config最後尾のapps取得
apps = backend_config_end['apps']

############################################################

# add_jsonのモデル数を取得
add_json_models_num = len(add_json['models'])

# port_number:の最大値を取得
port_number_list = []
for model in models:
    port_number_list.append(model['port_number'])

port_number_vacant = max(port_number_list)

# print(port_number_vacant)
# print(model_server_version)

############################################################

# modelsにmodelを記述
add_json_models = add_json['models']
model_add = []
for port_number, add_json_model in enumerate(add_json_models, port_number_vacant+1):
    models.append({
        "function_name": add_json['function_name'],
        "model_name": add_json_model['model_name'],
        "env_name_ip": add_json['env_name_ip'],
        "env_name_port": add_json['env_name_port'],

        # port_number : "models上最大値にプラス"
        "port_number": port_number,
        # model_path_on_azure_storage : "az://ovms/{mode_name}"
        "model_path_on_azure_storage": f"az://ovms/{add_json_model['model_name']}",
        "model_server_version": model_server_version
    })

# appsにenvsを記述
apps.append({
    "function_name": add_json['function_name'],
    "envs": add_json['envs']
})

############################################################

# 保存
with open(args.target_json, mode='wt', encoding='utf-8') as file:
    json.dump(target_dict, file, ensure_ascii=False, indent=2)

# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import requests
import configparser
import traceback
global token
global instance_
global server_

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "assets_noc" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

import traceback
from orchestator import OrchestatorCommon

"""
    Obtengo el modulo que fue invocado
"""
global orchestator_service
global path_ini_assetnoc_
global instance_key_ini

module = GetParams("module")

def get_process_and_instance_id_from_token_and_key(process_token, instance_key):
    if process_token is None:
        if instance_key:
            raise Exception("Cannot specify an instance for an Asset without a specified process")
        return 0, 0

    headers = {'Authorization': 'Bearer {token}'.format(token=token)}
    res = requests.post(f'{server_}' + f'/api/process/{process_token}', headers=headers)

    if res.status_code == 200:
        res = res.json()
        data = res['data']
        process_id = data['id']

        if instance_key is None:
            return process_id, 0
        else:
            for instance in data['instances']:
                if instance_key == instance['key']:
                    return process_id, instance['id']
            
            raise Exception("The instance hasn't been added to the process")

    else:
        raise Exception(res.json()['message'])

def get_user_ids_from_mails(user_mails):
    if user_mails is None or user_mails == "[]":
        return []
    
    headers = {'Authorization': 'Bearer {token}'.format(token=token)}
    res = requests.post(f'{server_}' + '/api/users/list', headers=headers)

    if res.status_code == 200:
        res = res.json()
        mails = [i for i in user_mails.strip("[]").split(", ")]
        user_ids = []
        
        for user_mail in mails:
            user_not_found = True

            for user in res['data']:
                if user_mail == user['email']:
                    user_ids.append(user['id'])
                    user_not_found = False

            if user_not_found:
                raise Exception(f"{user_mail} has not been added as a user")
        return user_ids
    else:
        raise Exception(res.json()['message'])

def get_process_token_and_instance_key_from_ids(process_id, instance_id):
    if process_id == 0:
        if instance_id != 0:
            raise Exception("Cannot specify instance ID if asset is global")
        return None, None
    
    headers = {'Authorization': 'Bearer {token}'.format(token=token)}
    res = requests.post(f'{server_}' + '/api/process/list', headers=headers)
    if res.status_code == 200:
        data = res.json()["data"]

        for process in data:
            if process['id'] == process_id:
                process_token = process['token']
                if instance_id == 0:
                    return process_token, None
                
                for instance in process['instances']:
                    if instance['id'] == instance_id:
                        return process_token, instance['key']
                raise Exception("The instance hasn't been added to the process")
            
        raise Exception("Invalid process ID")
    
    else:
        raise Exception(res.json()['message'])

#instance_key_ini may not be defined
def select_instance_key(instance_key, is_looking_for_global_assets):
        try: 
            if instance_key_ini and not instance_key:
                return instance_key_ini
            
        finally:
            return instance_key
        

if module == "loginNOC":
    
    conx =""
    
    try:
        server_ = GetParams("server_url")
        var_ = GetParams('var_')
        iframe = GetParams("iframe")
        iframe = eval(iframe) if iframe is not None else {}
        username = iframe.get("user", "")
        password = iframe.get("password", "")
        apikey = iframe.get("apikey", "")
        path = iframe.get("path_ini", GetParams("ruta_"))
        ignore_ssl = iframe.get("ignore_ssl", False)
        if isinstance(ignore_ssl, str):
            ignore_ssl = ignore_ssl.lower() == "true"
        verify_ssl = not ignore_ssl
        path_ini_assetnoc_ = path

        if password and username:
            try:
                orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=apikey)
                if server_ is None:
                    server_ = orchestrator_service.server
                token = orchestrator_service.get_authorization_token()
                headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
                res = requests.post(server_ + '/api/assets/list',
                                    headers=headers, verify=verify_ssl)
                conx = True
                SetVar(var_, conx)
            except:
                raise Exception("Password o E-mail incorrectos")
            
        elif apikey:
                    
            orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=apikey)
            if server_ is None:
                server_ = orchestrator_service.server
            token = orchestrator_service.get_authorization_token()
            headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
            res = requests.post(server_ + '/api/assets/list',
                                headers=headers, verify=verify_ssl)

            if res.status_code != 200:

                raise Exception("El API Key es incorrecto")
            else:
                conx = True
            SetVar(var_, conx)

        elif path:
            try:
                config = configparser.ConfigParser()
                if not config.read(path):
                    raise FileNotFoundError(f"No se pudo encontrar o leer el archivo .ini en la ruta: {path}")


                instance_key_ini = config['USER']['key']
                orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=apikey)
                if server_ is None:
                    server_ = orchestrator_service.server
                token = orchestrator_service.get_authorization_token()
                headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
                res = requests.post(server_ + '/api/assets/list',
                                    headers=headers, verify=verify_ssl)
                res.raise_for_status()
                conx = True
                SetVar(var_, conx)
            except FileNotFoundError as e:
                raise Exception(f"Error con el archivo de configuración: {e}")
            except KeyError as e:
                raise Exception(f"El archivo .ini no tiene el formato correcto. Falta la sección [USER] o la clave 'key'.")
            except requests.exceptions.RequestException as e:
                raise Exception(f"Error de conexión al intentar autenticar: {e}")
            except Exception as e:
                # Captura cualquier otro error inesperado
                print(traceback.format_exc())
                raise Exception(f"Ocurrió un error inesperado durante el login con .ini: {e}")
            
    except Exception as e:
        PrintException()
        conx = False
        print("Traceback: ", traceback.print_exc())
        SetVar(var_, conx)
        raise (e)

if module == "getData":
    name_ = GetParams("name_")
    var_ = GetParams("var_")
    process_token = GetParams("process_")
    instance_key = GetParams("instance_")
    extra_data = GetParams("extra_data_")

    instance_key = select_instance_key(instance_key=instance_key)
    try:
        data = {'name': name_, 'instance': instance_key,}
        if process_token:
            data['process'] = process_token
        
        headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(server_ + '/api/assets/get', data,
                            headers=headers)
        if res.status_code == 200:
            res = res.json()
            if res['success']:
                if extra_data is None:
                    if 'data' in res:
                        tmp = res['data']['value']
                        if var_:
                            SetVar(var_,tmp)
                else:
                    asset = res['data']
                    data = {}
                    data['name'] = asset['name']
                    data['id'] = asset['id']
                    data['type'] = asset['type']
                    data['value'] = asset['value']
                    process_id = asset.get('process_id', 0)
                    instance_id = asset.get('instance_id', 0)
                
                    data['process_token'], data['instance_key'] = get_process_token_and_instance_key_from_ids(process_id, instance_id)

                    data['users'] = [user['email'] for user in asset.get('users', [])]

                    SetVar(var_, data)                    
            else:
                raise Exception(res['message'])
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise (e)

if module == "getAllData":
    var_ = GetParams("var_")
    extra_data = GetParams("extra_data_")

    try:
        headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(server_ + '/api/assets/list',
                            headers=headers)

        if res.status_code == 200:
            res = res.json()
            if res['success']:
                if extra_data is None:
                    tmp = [{'name':a['name'],'value':a['value']} for a in res['data']]
                    SetVar(var_,tmp)
                    for b in tmp:
                        SetVar(b['name'],b['value'])
                else:
                    received_data = res['data']
                    data_list = []
                    i = 1
                    for asset in received_data:

                        data = {}
                        data['name'] = asset['name']
                        data['id'] = asset['id']
                        data['type'] = asset['type']
                        data['value'] = asset['value']

                        process = asset['process']
                        data['process_token'] = process['token'] if process is not None else None

                        instance = asset['instance']
                        data['instance_key'] = instance['key'] if instance is not None else None

                        data['users'] = [user['email'] for user in asset.get('users', [])]

                        data_list.append(data)

                    SetVar(var_, data_list)
            else:
                raise Exception(res['message'])
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise (e)

if module == "addAsset":
    name = GetParams("name_")
    type_ = GetParams("type_")
    value = GetParams("value_")
    result = GetParams('result_')
    process_token = GetParams("process_token_")
    instance_key = GetParams("instance_key_")
    users_mails = GetParams("users_")

    if type_ is None:
        type_ = "text"
    
    try:
        user_list = get_user_ids_from_mails(users_mails)
        process_id, instance_id = get_process_and_instance_id_from_token_and_key(process_token, instance_key)

        data = {'name': name, 'type': type_, 'value': value, 'process_id': process_id, 'users': user_list, 'instance_id': instance_id}

        headers = {'Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(f'{server_}' + '/api/assets/add', json=data,
                            headers=headers)
        
        if res.status_code == 200:
            res = res.json()
            SetVar(result, res)
            
        else:
            raise Exception(res.json()['message'])
        
    except Exception as e:
        PrintException()
        raise(e)
    
if module == "editData":
    name = GetParams("name_")
    type_ = GetParams("type_")
    value = GetParams("value_")
    result = GetParams('result_')
    process_token = GetParams("process_token_")
    instance_key = GetParams("instance_key_")
    users_mails = GetParams("users_")
    asset_id = GetParams("Asset_id")

    if type_ is None:
        type_ = "text"


    try:
        process_id, instance_id = get_process_and_instance_id_from_token_and_key(process_token, instance_key)
        user_list = get_user_ids_from_mails(users_mails)

        data = {'name': name, 'type': type_, 'value': value, 'process_id': process_id, 'users': user_list, 'instance_id': instance_id, 'id': asset_id}

        headers = {'Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(f'{server_}' + '/api/assets/edit', json=data,
                            headers=headers)
        
        if res.status_code == 200:
            res = res.json()
            SetVar(result, res)
            
        else:
            raise Exception(res.json()['message'])
        
    except Exception as e:
        PrintException()
        raise(e)
    

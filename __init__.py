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

module = GetParams("module")

if module == "loginNOC":
    username = GetParams("username")
    password = GetParams("password")
    server_ = GetParams("server_url")
    api_key = GetParams("api_key")
    ruta_ = GetParams("ruta_")
    instance_ = GetParams("instance_")
    try:
        orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=ruta_, apikey=api_key)
        if server_ is None:
            server_ = orchestrator_service.server
        token = orchestrator_service.get_authorization_token()
        headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(server_ + '/api/assets/list',
                            headers=headers)

        if res.status_code != 200:
            raise Exception("El API Key es incorrecto")
        
    except Exception as e:
        PrintException()
        print("Traceback: ", traceback.print_exc())
        raise (e)

if module == "getData":

    name_ = GetParams("name_")
    var_ = GetParams("var_")
    process_ = GetParams("process_")

    try:
        data = {'name': name_, 'instance': instance_}
        if process_:
            data['process'] = process_
        headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(server_ + '/api/assets/get', data,
                            headers=headers)

        print('RES',res)
        if res.status_code == 200:
            res = res.json()
            if res['success']:
                
                if 'data' in res:
                    print(res)
                    tmp = res['data']['value']
                    if var_:
                        SetVar(var_,tmp)

            else:
                raise Exception(res['message'])
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise (e)

if module == "getAllData":

    # name_ = GetParams("name_")
    var_ = GetParams("var_")

    try:
        headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
        res = requests.post(server_ + '/api/assets/list',
                            headers=headers)

        if res.status_code == 200:
            res = res.json()
            if res['success']:
                #print('RES',[a['name'] for a in res['data']])
                tmp = [{'name':a['name'],'value':a['value']} for a in res['data']]
                for b in tmp:
                    SetVar(b['name'],b['value'])
            else:
                raise Exception(res['message'])
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise (e)



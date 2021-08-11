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
global token
global instance_
global server_

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "loginNOC":

    ruta_ = GetParams("ruta_")

    config = configparser.ConfigParser()
    config.read(ruta_)
    email_ = config.get('USER', 'user')
    pass_ = config.get('USER', 'password')
    instance_ = config.get('USER', 'key')
    apikey_ = config.get('USER', 'apiKey')
    server_ = config.get('NOC', 'server')

    try:
        if apikey_ is not None:
            token = apikey_
        else:
            data = {'email': email_, 'password': pass_}
            res = requests.post(server_ + '/api/auth/login', data,
                                headers={'content-type': 'application/x-www-form-urlencoded'})

            if res.status_code == 200:
                res = res.json()
                if res['success']:
                    token = res['data']
                else:
                    raise Exception(res['message'])
            else:
                raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
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

    name_ = GetParams("name_")
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



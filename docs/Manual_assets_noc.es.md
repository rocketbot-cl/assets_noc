



# Assets_NOC

Módulo para obtener asset de Rocketbot NOC

*Read this in other languages: [English](Manual_assets_noc.md), [Português](Manual_assets_noc.pr.md), [Español](Manual_assets_noc.es.md)*

![banner](imgs/Banner_assets_noc.png)
## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.




# How to use

We must have enabled the use of the orchestrator as well as the e-mail, password, URL of the server.



## Descripción de los comandos

### Login NOC

Inicie sesión en NOC utilizando e-mail o contraseña, clave API y archivo noc.ini.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL Servidor|URL del servidor a donde se conecta|https://roc.myrb.io/|
|Seleccione un metodo para conectarse al Orquestador|Opciones para iniciar sesión en R.O.C, se puede usar las credenciales del usuario, API Key o seleccionando archivo noc.ini||
|Ignorar SSL|Marcar si desea ignorar la verificación del certificado SSL||
|Asignar resultado a Variable|Variable donde se almacenara el estado de la conexion, devuelve True si es exitosa o False en el caso contrario|Variable|

### Obtener Asset Específico

Obtiene el asset especifico que se le indique
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Asset|Nombre del asset a obtener|Test|
|Token del proceso|Token del proceso. Si se especifica, hay que tambien especificar la key de instancia.|27FEXKIXFRFDUNVD|
|Key de Instancia|Key de instancia del proceso|6241c3a1dd96f8f92f|
|Obtener datos adicionales|Marca para obtener datos extra de los Assets|True|
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|

### Obtener Todos los Assets

Obtiene todos los Assets y los asigna a la variable correspondiente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|
|Obtener datos adicionales|Marca para obtener datos extra de los Assets|True|

### Agregar Asset

Agrega un Asset a tu Orquestador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Asset|Nombre del Asset a agregar|NuevoAsset|
|Token del proceso|Token del proceso al que se le agregara el Asset|27FEXKIXFRFDUNVD|
|Key de Instancia|Key de la instancia al que se le agregara el Asset|6241c3a1dd96f8f92f|
|Mail de usuarios|Lista de mails de usuarios a los que se le agregara el Asset|[usuario1@mail.com, usuario2@mail.com, ...]|
|Tipo del Asset|Tipo del Asset a agregar|General|
|Valor del Asset|Valor del Asset a agregar|Un valor|
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|

### Modificar Asset

Modifica el asset especifico que se le indique
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Id del Asset|Id del Asset a modificar|Id_Asset|
|Nuevo nombre de Asset|Nuevo nombre del Asset modificado. Si existe otro Asset con el mismo nombre, no se podra modificar el asset sin cambiar tambien el nombre|NuevoAsset|
|Nuevo token del proceso|Token del proceso que tendrá el Asset|27FEXKIXFRFDUNVD|
|Nueva key de la instancia|Key de la instancia que tendrá el Asset|6241c3a1dd96f8f92f|
|Nuevos mails de usuarios|Lista de Mails de usuarios que tendrán el Asset|[MailUsuario1, MailUsuario2, ...]|
|Nuevo tipo del Asset|Nuevo tipo del Asset a modificar|General|
|Nuevo valor del Asset|Nuevo valor del Asset a modificar|Un valor|
|Asignar resultado a Variable|Variable donde se guardara el resultado. Nombre de variable sin llaves {}|Variable|

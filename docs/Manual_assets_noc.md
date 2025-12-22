## assets_noc




# Assets_NOC
  
Module to get assets from Rocketbot NOC  

*Read this in other languages: [English](Manual_assets_noc.md), [Português](Manual_assets_noc.pr.md), [Español](Manual_assets_noc.es.md)*
  
![banner](imgs/Banner_assets_noc.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

# Como usar este modulo

Debemos tener habilitado el uso del orquestador asi como el e-mail, contraseña, URL del servidor.


## Description of the commands

### Login NOC
  
Login NOC using credentials such as e-mail and password, API Key and noc.ini file.
|Parameters|Description|example|
| --- | --- | --- |
|URL Server|Server URL|https://roc.myrb.io/|
|Select a method to connect to the Orchestrator|Options to login to R.O.C, you can use user credentials, API Key or by selecting noc.ini file||
|Ignore SSL|Check if you want to ignore SSL certificate verification||
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Get an Specific Asset
  
Obtains the specific asset that is indicated
|Parameters|Description|example|
| --- | --- | --- |
|Asset Name|Name of the asset to get|Test|
|Process token|Process token|27FEXKIXFRFDUNVD|
|Instance Key|Instance ID of the process|6241c3a1dd96f8f92f|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

### Get All Assets
  
Get all the Assets and assign them to the corresponding variable
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

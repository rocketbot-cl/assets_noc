



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
|Instance Key|Instance key of the process|6241c3a1dd96f8f92f|
|Obtain extra data|Check to obtain extra data from the Assets|True|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

### Get All Assets

Get all the Assets and assign them to the corresponding variable
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|
|Obtain extra data|Check to obtain extra data from the Assets|True|

### Add Asset

Add an Asset to your Orchestrator
|Parameters|Description|example|
| --- | --- | --- |
|Asset Name|Name of the Asset to add|NewAsset|
|Process token|Process Token to which the Asset will be modified|27FEXKIXFRFDUNVD|
|Instance Key|Instance Key to which the Asset will be added|6241c3a1dd96f8f92f|
|User mails|List of user mails to which the Asset will be added|[UserMail1, UserMail2, ...]|
|Asset type|Type of the Asset to add|General|
|Asset Value|Value of the Asset to add|A value|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

### Modify Asset

Modifies the specific asset that is indicated
|Parameters|Description|example|
| --- | --- | --- |
|Asset Id|Id of the Asset to modify|Id_Asset|
|Asset Name|New name of the Asset|NewAsset|
|Process token|Process Token to which the Asset will be modified|27FEXKIXFRFDUNVD|
|Instance Key|Instance Key to which the Asset will be modified|6241c3a1dd96f8f92f|
|User Mails|List of user Mails who will have the Asset|[UserMail1, UserMail2, ...]|
|Asset type|Type of the Asset to modify|General|
|Asset Value|Value of the Asset to modify|A value|
|Assign result to Variable|Variable where the result will be saved. Name of variable without {}|Variable|

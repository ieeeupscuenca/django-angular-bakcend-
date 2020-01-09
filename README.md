## Django + Angular [Proceso para Backend (Django)]

<img alt="Covalent" src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" width="150">


Django es un framework de aplicaciones web gratuito y de código abierto (open source) escrito en Python. Un framework web es un conjunto de componentes que te ayudan a desarrollar sitios web más fácil y rápidamente. El objetivo es unir el framework django como backend y al framework Angular como frontend.

**Nota: En este repositorio se muesrtra los pasos a seguir para descargar e instalar este proyecto django. La parte de frotned se puede encontrar en: https://github.com/ieeeupscuenca/django-angular-frontend**

## Requisitos
* Tener instalado la versión del python 3.7
* Tener instalado git
* Instalar pycharm: https://www.jetbrains.com/es-es/pycharm/download/#section=windows **[Indispensable este IDE, sera de mucha ayuda]**
---

## Instalación de Django

* **Descargar el proyecto de git**
Para poder realizar este proceso mediante el terminal se va a utilizar la siguiente linea para clonar el repositorio del github.
```bash
git clone https://github.com/ieeeupscuenca/django-angular-bakcend-.git
```
* **Instalación de django**

Una vez descargado la carpeta de django se procede a realizar el siguiente comando para la instalación del framework. Usamos la siguiente linea de comando
```bash
pip install -r requirements.txt
```
El archivo **requirements.txt** es un documento en donde se tiene la linea de instalación de django con su respectiva versión


* **Creación del entorno virtual**

Otra parte importante del proyecto es que se debe crear un entorno virtual para poder trabajar con django. No se subio el entorno que habiamos creado debido a que puede generar problemas. Por tanto con las siguientes lineas puede crear y activar el entorno virtual.
```bash
## Creación del entorno virtual
python -m venv myvenv
## Activación del entorno virtual
myvenv\Scripts\activate
```

* **Resolviendo dependencias**

Una vez instalado y descargado django, en Pycharm procedemos a abrir el proyecto para realizar los siguientes comandos. PyCharm nos permite tener un terminal el cual permite ingresar comando python para django puesto que ademas nos activa el entorno virtual creado automaticamente y nos sera de mucha ayuda de ahora en adelante. En dicha terminal aplicamos los siguientes comandos.

```bash
python manage.py makemigrations
python manage.py migrate
```
En este caso estamos migrando los modelos y las configuraciones de nuestra app para resolver todos los problemas de dependencias. Una vez hecho procedemos a instalar djangoRestFramework.


* **Intalación de DjangorestFramework**

Este módulo es muy importante ya que este nos permitira  hacer una conexión con el frontend, en este caso con angular. Para ello utilizamos la siguiente linea en el terminal de pycharm.

```bash
pip install djangorestFramework
```
* **Cración de superusuario y correr el servidor**

Por ultimo debemos crear un superusuario para entrar a la administración. Para ello ejecutamos las siguientes lineas.
```bash
python manage.py createsuperuser
  Nombre de usuario (leave blank to use 'bvega'): <ingrese_usuario_admin>
  Dirección de correo electrónico: <ingrese_correo_electronico>
  password: <ingrese_contraseña>
  Password (again): <confirme_contraseña>
  ## En caso de que su contraseña sea similar aparecera ese mensaje
  La contraseña es demasiado similar a la de nombre de usuario.
  Bypass password validation and create user anyway? [y/N]: y

## Con esta linea corremos el servidor django
python manage.py runserver
```
Realizado estos dos ultimos comando podremos acceder a nuestro sitio web mediante:
* pagina principal:      http://127.0.0.1:8000/
* pagina rest_personas:  http://127.0.0.1:8000/persona
* pagina rest_direccion: http://127.0.0.1:8000/direccion
* pagina administrador:  http://127.0.0.1:8000/admin
 

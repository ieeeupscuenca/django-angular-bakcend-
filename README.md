## Django + Angular [Proceso para Backend (Django)]

<img alt="Covalent" src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" width="150">


Django es un framework de aplicaciones web gratuito y de código abierto (open source) escrito en Python. Un framework web es un conjunto de componentes que te ayudan a desarrollar sitios web más fácil y rápidamente. El objetivo es unir el framework django como backend y al framework Angular como frontend.

**Nota: En este repositorio se muesrtra los pasos a seguir para descargar e instalar este proyecto django. La parte de frotned se puede encontrar en: https://github.com/ieeeupscuenca/django-angular-frontend**

## Requisitos
* Tener instalado la versión del python 3.7
* Tener instalado git
* Instalar pycharm para correr el programa sin problema **(indispensable)**
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


* **Resolviendo dependencias**

Una vez instalado y descargado django, en Pycharm procedemos a abrir el proyecto para realizar los siguientes comandos. PyCharm nos permite tener un terminal el cual permite ingresar comando python para django y nos sera de mucha ayuda de ahora en adelante. En dicha terminal aplicamos los siguientes comandos.

```bash
python manage.py makemigrations
python manage.py migrate
```
En este caso estamos migrando los modelos y las configuraciones de nuestra app para resolver todos los problemas de dependencias. Una vez hecho esto corremos el siguiente comando.

```bash
python manage.py createsuperuser
  Nombre de usuario (leave blank to use 'bvega'): <ingrese_usuario_admin>
  Dirección de correo electrónico: <ingrese_correo_electronico>
  password: <ingrese_contraseña>
  Password (again): <confirme_contraseña>
  ## En caso de que su contraseña sea similar aparecera ese mensaje
  La contraseña es demasiado similar a la de nombre de usuario.
  Bypass password validation and create user anyway? [y/N]: y
python manage.py runserver
```
Realizado estos dos ultimos comando podremos acceder a nuestro sitio web mediante http://127.0.0.1:8000/

 

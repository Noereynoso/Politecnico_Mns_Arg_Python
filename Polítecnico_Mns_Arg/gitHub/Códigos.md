# 🚀 Cómo conectar tu carpeta local a GitHub

Este instructivo te guía paso a paso para conectar tu carpeta local con el repositorio de GitHub:  
**https://github.com/Noereynoso/Politecnico_Mns_Arg_Python.git**

---

## A. Empezar a subir archivos.

- **1️⃣ Abre la terminal en la carpeta de tu proyecto**

- **2️⃣ Inicializa el repositorio local (si aún no lo hiciste)**
    ```bash
    git init


- **3️⃣ Agrega tus archivos al área de preparación**
    ```bash
    git add .

- **5️⃣ Conecta tu carpeta local con el repositorio de GitHub**
    ```bash
    git remote add origin https://github.com/Noereynoso/Politecnico_Mns_Arg_Python.git

## B. Sube tus archivos a GitHub.
- **6️⃣ Si tu rama principal se llama master:**
    ```bash 
    git push -u origin master

## C. Si tu rama principal se llama main: 
    git push -u origin main

---

##  7️⃣ ¡Listo!
- **Ahora tus archivos están conectados y subidos a tu repositorio de GitHub.**
- **Para futuros cambios, solo necesitas usar:**
    ```bash 
    git add .
    git commit -m "Descripción de los cambios"
    git push

- **Consejo: Si ves algún error sobre "non-fast-forward" o "unrelated histories", primero haz:**
    ```bash 
    git pull origin master --allow-unrelated-histories

- **Luego repite el git push.**
    ```bash 
    git push
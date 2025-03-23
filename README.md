README - Instrucciones para Ejecutar el Programa
Este README proporciona las instrucciones necesarias para configurar, ejecutar y compilar el programa. A continuación, se detallan los pasos para activar el entorno virtual, instalar dependencias, ejecutar el programa y crear un ejecutable.
________________________________________
1. Configuración del Entorno Virtual
Antes de ejecutar el programa, es necesario activar el entorno virtual. Sigue estos pasos:
Primer Comando: Activar el entorno virtual nuevo_entorno
bash
Copy
.\nuevo_entorno\Scripts\Activate
Segundo Comando: Activar el entorno virtual entornodownload
bash
Copy
.\entornodownload\Scripts\Activate
________________________________________
2. Instalación de Dependencias
Una vez activado el entorno virtual, instala las dependencias necesarias para ejecutar el programa. Las dependencias incluyen librerías como wx, yt_dlp, pandas, entre otras.
Ejecuta el siguiente comando para instalar las dependencias:
bash
Copy
pip install wxPython yt-dlp pandas pyinstaller
________________________________________
3. Ejecutar el Programa
El programa está diseñado para descargar videos de YouTube utilizando una interfaz gráfica. Para ejecutarlo, asegúrate de que todas las dependencias estén instaladas y luego ejecuta el archivo principal main.py.
bash
Copy
python main.py
________________________________________
4. Crear un Ejecutable con PyInstaller
Si deseas crear un archivo ejecutable del programa, puedes usar PyInstaller. Este comando generará un archivo .exe que podrás distribuir.
Comando para crear el ejecutable:
bash
Copy
pyinstaller --onefile --name DownloadJD --noconsole main.py
Explicación de los parámetros:
•	--onefile: Crea un único archivo ejecutable.
•	--name DownloadJD: Asigna el nombre DownloadJD al ejecutable.
•	--noconsole: Oculta la consola al ejecutar el programa (útil para aplicaciones con interfaz gráfica).
Ubicación del Ejecutable:
El archivo ejecutable se guardará en la carpeta dist que se crea automáticamente dentro del directorio del proyecto.
________________________________________
5. Crear un Instalador con Inno Setup
Si deseas crear un instalador para distribuir el programa, puedes usar Inno Setup. Ya se ha proporcionado un archivo de configuración de Inno Setup en la carpeta app.
Pasos para crear el instalador:
1.	Abre el archivo de configuración de Inno Setup (.iss) que se encuentra en la carpeta app.
2.	Compila el script en Inno Setup para generar el instalador.
3.	El instalador se generará en la carpeta especificada en el script de Inno Setup.
________________________________________
6. Estructura del Proyecto
•	nuevo_entorno/: Carpeta del entorno virtual.
•	entornodownload/: Carpeta del segundo entorno virtual.
•	utils/: Contiene módulos y utilidades del programa.
•	app/: Carpeta con el archivo de configuración de Inno Setup para crear el instalador.
•	main.py: Archivo principal del programa.
•	dist/: Carpeta donde se guarda el ejecutable generado por PyInstaller.
________________________________________
7. Notas Adicionales
•	Asegúrate de tener Python instalado en tu sistema.
•	Si encuentras algún error al activar los entornos virtuales, verifica que estén correctamente configurados.
•	Para más información sobre PyInstaller, consulta la documentación oficial.
•	Para más información sobre Inno Setup, consulta la documentación oficial.

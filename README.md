# Descargador y medidor de archivos

## Funcion
Descargar archivos de una pagina de prueba https://repo.jellyfin.org/jellyfish/ (20 archivos en total) y anota sus tamaños en megaBytes y sus tiempos de descarga en segundos en un archivo json llamado ajustes.json.
Estos pares de datos seran transportados al excel para aplicar ajustes.

## Como utilizarlo
- Tener python instalado
- Instalar los requerimientos
- ejecutar `python main.py`

## Requerimientos
- `pip install requests`

## Configuraciones
- Se pueden configurar los links de descarga en el archivo `config.py`

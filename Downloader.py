import os
import config
import json
import requests
from urllib.parse import urlsplit
import time
import math

class Downloader():
    def __init__(self) -> None:
        pass

    def download(self,urls:set[str],headers:dict,cookies:dict,json_path:str):
        
        data = [] # Lista de diccionarios
        numero = 0 # Cantidad de descargas

        for url in urls:
            numero += 1
            print(f"Descargando archivo {numero}/{len(urls)}")
            start_time = time.time()  # Iniciamos el temporizador
            try:
                response = requests.get(url, headers=headers, cookies=cookies, stream=True)
            except:
                print(f"error al conectarse a {url}")
                continue
            
                
            # Verificamos si la solicitud fue exitosa (código 200)
            if response.status_code == 200:            
                
                # Tamaño del archivo en bytes (tamaño del contenido)
                file_size = int(response.headers.get('Content-Length', 0))  # Algunas veces no se incluye Content-Length

                if file_size == 0:
                    print(f"la url no devuelve el tamaño del archivo: {url}")
                    continue
                
                # Obtener el nombre del archivo desde la URL o cabeceras
                # Si el nombre no está en la URL, se intenta obtener del encabezado Content-Disposition
                content_disposition = response.headers.get('Content-Disposition', '')
                if 'filename=' in content_disposition:
                    file_name = content_disposition.split('filename=')[1].strip('"')
                else:
                    file_name = os.path.basename(urlsplit(url).path)  # Usamos la parte de la URL como nombre del archivo

                # Guardamos el archivo en disco
                
                if not os.path.exists(config.foldername):
                    os.mkdir(config.foldername)

                destination = os.path.join(config.foldername,file_name)
                with open(destination, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):  # Descargamos en bloques
                        f.write(chunk)

                download_time = time.time() - start_time
                # parar el temporizador luego de escribir el archivo en disco

                size = math.trunc(file_size / 1024 / 1024 * 10000) / 10000
                dTime = math.trunc(download_time * 10000) / 10000
                velMedia = size/dTime

                data.append({'numero':numero,'nombre':file_name,'size':size,'tiempo_descarga':dTime,'velocidad_media':velMedia})
        
                # Imprimimos los resultados
                print(f"Archivo descargado: {file_name}")
                print(f"size del archivo: {size} MegaBytes")
                print(f"Tiempo de descarga: {dTime} segundos")

                # Data: lista de diccionarios
                with open(json_path, 'w') as file:
                    json.dump(data, file,ensure_ascii=False, indent=4)
            else:
                print(f'Error {response.status_code}: No se pudo descargar el archivo.')

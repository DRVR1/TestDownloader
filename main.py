import Downloader
import config

d = Downloader.Downloader()

d.download(config.urls,config.headers,config.cookies,config.file_path)


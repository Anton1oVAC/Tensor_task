from log import logger
import os
import json

f = ('.py', '.cpp', '.c', '.h', '.js', '.sh', 'Makefile')

def create_json(source_path, version):
	logger.info(f"Создание json файла")

	files = [file for file in os.listdir(source_path) if file.endswith(f)]

	version_info = {
		"name": "hello world",
		"version": version,
		"files": files
	}

	version_file_path = os.path.join(source_path, 'version.json')
	with open(version_file_path, 'w') as version_file:
		json.dump(version_info, version_file, indent=4)

	logger.info(f"Файл json {version_file_path} создан!")
from log import logger
import os
import shutil

def clean_directory(repo_path, source_path):
	full_source_path = os.path.join(repo_path, source_path)

	if not os.path.exists(full_source_path):
		logger.error(f"Путь {full_source_path} не найден")
		raise FileNotFoundError(f"Путь {full_source_path} не найден!")
	
	# Нужно ли? Или можно заного перезаписать? 
	if os.path.exists(source_path):
		logger.error(f"Директория {full_source_path} уже существует")
		return None
	
	logger.info(f"Удаление, остается {source_path}")

	temp_dir = source_path
	if os.path.exists(temp_dir):
		shutil.rmtree(temp_dir)

	shutil.copytree(full_source_path, temp_dir)

	shutil.rmtree(repo_path)

	logger.info(f"Все исходные файлы тут - {temp_dir}")
	return temp_dir

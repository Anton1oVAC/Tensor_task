from log import logger
import os
from datetime import datetime
import shutil

def create_archive(source_path):
	
	dir_name = os.path.basename(os.path.normpath(source_path))
	date_str = datetime.now().strftime("%d%m%Y")
	archive_name = f"{dir_name}{date_str}.zip"

	logger.info(f"Создание архива {archive_name}")

	shutil.make_archive(dir_name, 'zip', source_path)

	if os.path.exists(f"{dir_name}.zip"):
		os.rename(f"{dir_name}.zip", archive_name)

	logger.info(f"Архив создан {archive_name}")
	return archive_name
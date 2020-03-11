#!/usr/bin/python3


import os

import jk_utils
import jk_pwdinput

import thaniya_client




LOCAL_MOUNT_DIR_PATH = os.path.abspath("tmp")
os.makedirs(LOCAL_MOUNT_DIR_PATH, exist_ok=True)




driver = thaniya_client.ThaniyaBackupDriver(
	thaniya_client.BackupConnector_Local(),
	{},
	LOCAL_MOUNT_DIR_PATH,
	thaniya_client.TargetDirectoryStrategy_DateDefault(),
)



driver.testConnector()






#!/usr/bin/python3


import os

import jk_utils
import jk_pwdinput

import thaniya_client




LOCAL_MOUNT_DIR_PATH = os.path.abspath("/mnt")

REMOTE_USERNAME = "thaniya_user1"
REMOTE_PASSWORD = ""
REMOTE_HOST = "192.168.11.42"
#REMOTE_HOST = "localhost"
REMOTE_SHARE_NAME = "thaniya_user1"
REMOTE_DESTINATION_SUBDIR_PATH = "data"



pwd = REMOTE_PASSWORD if REMOTE_PASSWORD else jk_pwdinput.readpwd("Connection password for user " + REMOTE_USERNAME + ": ")

driver = thaniya_client.ThaniyaBackupDriver(
	thaniya_client.BackupConnector_CIFSMount(),
	{
		"cifs_hostAddress": REMOTE_HOST,
		"cifs_login": REMOTE_USERNAME,
		"cifs_password": pwd,
		#"cifs_port": 445,
		#"cifs_version": "2.1",
		"cifs_shareName": REMOTE_SHARE_NAME,
	},
	LOCAL_MOUNT_DIR_PATH,
	thaniya_client.TargetDirectoryStrategy_DateDefault(REMOTE_DESTINATION_SUBDIR_PATH),
)



driver.testConnector()






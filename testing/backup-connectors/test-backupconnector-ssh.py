#!/usr/bin/python3


import os

import jk_utils
import jk_pwdinput

import thaniya_client




LOCAL_MOUNT_DIR_PATH = os.path.abspath("tmp")

REMOTE_USERNAME = "thaniya_user1"
REMOTE_PASSWORD = ""
REMOTE_HOST = "192.168.11.42"
#REMOTE_HOST = "localhost"
REMOTE_DESTINATION_BASE_PATH = "/home/thaniya_user1/data"




pwd = REMOTE_PASSWORD if REMOTE_PASSWORD else jk_pwdinput.readpwd("Connection password for user " + REMOTE_USERNAME + ": ")
driver = thaniya_client.ThaniyaBackupDriver(
	thaniya_client.BackupConnector_SSHMount(),
	{
		"ssh_hostAddress": REMOTE_HOST,
		"ssh_login": REMOTE_USERNAME,
		"ssh_password": pwd,
		"ssh_port": 22,
		"ssh_dirPath": REMOTE_DESTINATION_BASE_PATH,
	},
	LOCAL_MOUNT_DIR_PATH,
	thaniya_client.TargetDirectoryStrategy_DateDefault(),
)



driver.testConnector()






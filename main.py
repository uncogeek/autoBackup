import datetime
import os
import jdatetime
import functions
import mailer
import constant as C


jalaliDate = jdatetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # 1401-06-23_17-10-25
# gregorianDate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # 2022-09-15_13-27-46

DESTINATION_FOLDER = C.BACKUP_DESTINATION_BACKUP_FOLDER
ORIGIN_DESTINATION = DESTINATION_FOLDER

source_folders = C.BACKUP_SOURCEFOLDERS_TO_BACKUP

# create folder for backup
folder_name_backup = jalaliDate
DESTINATION_FOLDER = os.path.join(DESTINATION_FOLDER, folder_name_backup)
os.mkdir(DESTINATION_FOLDER)

folder_names = C.BACKUP_FOLDER_NAMES_TO_BACKUP

counter = 0
for i in folder_names:
    functions.createFolderForBackup(DESTINATION_FOLDER, i)
    functions.copyfile(source_folders[counter], os.path.join(DESTINATION_FOLDER, i))
    counter += 1

functions.rarBackUpFolders(ORIGIN_DESTINATION + folder_name_backup +  ".rar", DESTINATION_FOLDER, folder_name_backup + '.rar')
functions.ftpUploadBackupRarFile(ORIGIN_DESTINATION + folder_name_backup +  ".rar", folder_name_backup)

try:
    mailer.send_mail(send_from=C.EMAIL_USER,
                    subject="Backup | " + folder_name_backup,
                    text=f"{folder_name_backup} backup completed.",
                    send_to=None,
                    files=[DESTINATION_FOLDER  + ".rar"]
                    )   
except ValueError as exc:
    raise ValueError("Mailer got error") from exc

print("\n program has been finished")

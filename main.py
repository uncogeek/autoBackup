import datetime
import os
import jdatetime
import functions
import mailer
import constant as C


jalaliDate = jdatetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # 1401-06-23_17-10-25
# gregorianDate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # 2022-09-15_13-27-46

destination_folder = C.BACKUP_DESTINATION_BACKUP_FOLDER
origin_dst = destination_folder

source_folders = C.BACKUP_SOURCEFOLDERS_TO_BACKUP

# create folder for backup
folder_name_backup = jalaliDate
destination_folder = os.path.join(destination_folder, folder_name_backup)
os.mkdir(destination_folder)

folder_names = C.BACKUP_FOLDER_NAMES_TO_BACKUP

counter = 0
for i in folder_names:
    functions.createFolderForBackup(destination_folder, i)
    functions.copyfile(source_folders[counter], os.path.join(destination_folder, i))
    counter += 1

functions.rarBackUpFolders(origin_dst + folder_name_backup +  ".rar", destination_folder, folder_name_backup + '.rar')
functions.ftpUploadBackupRarFile(origin_dst + folder_name_backup +  ".rar", folder_name_backup)
mailer.send_mail(send_from=C.EMAIL_USER,
                 subject="Backup | " + folder_name_backup,
                 text="backup completed.",
                 send_to=None,
                 files=[destination_folder  + ".rar"]
                 )


print("app done.")

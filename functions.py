import os
import shutil
import patoolib
import ftplib
import constant as C


def createFolderForBackup(dst, folder_name):
    try:
        tmp_variable = os.path.join(dst, folder_name)
        os.mkdir(tmp_variable)
        print(f"Create Folder | {tmp_variable} Created.")
    except Exception as e:
        print("Create Folder | Error: ", e)


def copyfile(src, dst):
    # fetch all files
    try:
        for file_name in os.listdir(src):
            # construct full file path
            source = src + file_name
            # copy only files
            if os.path.isfile(source):
                shutil.copy(source, dst)
        print(f"File | {file_name} copied.")
    except Exception as e:
        print("Copy File | Error: ", e)



def rarBackUpFolders(file_name, path, rar_file_name):
    try:
        patoolib.create_archive(file_name, (path,))
        print(f"RAR | created. file name: {rar_file_name}")
    except Exception as e:
        print("RAR | Error: " , e)


def ftpUploadBackupRarFile(file, file_name):
    try:
        session = ftplib.FTP(C.FTP_SERVER, C.FTP_USER, C.FTP_PASSWORD)
        file = open(file,'rb')                  # file to send
        session.storbinary(f'STOR {file_name}.rar', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        print("FTP | uploaded to server.")
    except Exception as e:
        print("FTP | Error: ", e)



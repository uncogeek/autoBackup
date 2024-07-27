# Automated Backup System

This Python project provides an automated backup solution for files and folders. It performs several actions to ensure your data is safely backed up and easily accessible.

## Features

- Backs up specified files and folders from a defined directory
- Moves backup files to an archive directory
- Compresses all backed-up files into a RAR file
- Sends the RAR file via email
- Uploads the RAR file to an FTP server
- Uses Jalali (Shamsi) calendar for naming backup folders and RAR files
- Configurable to use Gregorian calendar for date naming

## Configuration
change the backup source path, destination of files to backup and where to archive, email settings, and FTP settings in constant.py

## Usage
1. Install Requirements
2. Configure path
> constant.py line 14 (BACKUP_DESTINATION_BACKUP_FOLDER)
> path to copy files into it as an archive folder [where you want make a backup]
> line 16 BACKUP_SOURCEFOLDERS_TO_BACKUP is a list of paths that you want to make backup of them (can be single path or a list)
> line 20 BACKUP_FOLDER_NAMES_TO_BACKUP is name of paths (a shortcut of the paths name in line 16)
3. Email setting
constant.py:
 - line 7 EMAIL_USER is your email account that will send files by
 - line 8 EMAIL_PASSWORD password of your email account
 - line 11 EMAIL_ADRRESS_TO target email address to send files
4.ftp setting
 constant.py:
line 2-4 configure your Ftp server account

```pytohn
 python main.py
```

## Requirements

(List the required Python libraries and any system dependencies)

## Planned Features

The following features are planned for future updates:

- Send backup notifications to a Telegram bot
- Password protection for RAR files
- Upload backups to cloud storage services (Google Drive, Mega, Dropbox, etc.)
- Code refactoring for improved performance and maintainability

## Contributing

Contributions to this project are welcome. Please feel free to submit a Pull Request.

## License

MIT License


#!/bin/bash

# Variables
SOURCE_DIR="/path/to/source"
BACKUP_DIR="/path/to/backup"
BACKUP_FILE="backup_$(date +%Y%m%d%H%M%S).tar.gz"
LOG_FILE="/var/log/backup.log"

# Create backup
echo "$(date): Starting backup of $SOURCE_DIR" >> $LOG_FILE
tar -czf $BACKUP_DIR/$BACKUP_FILE $SOURCE_DIR 2>> $LOG_FILE

if [ $? -eq 0 ]; then
  echo "$(date): Backup successful. File: $BACKUP_DIR/$BACKUP_FILE" >> $LOG_FILE
else
  echo "$(date): Backup failed!" >> $LOG_FILE
fi

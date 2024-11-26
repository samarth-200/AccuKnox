
import psutil
import logging

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Logging setup
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu > CPU_THRESHOLD:
        logging.warning(f"High CPU usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage: {memory}%")
    if disk > DISK_THRESHOLD:
        logging.warning(f"Low disk space: {disk}% used")

    print(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

if __name__ == "__main__":
    check_system_health()

# To Start, In PowerShell Run As Admis -> wsl
# Linux Commands Learning Roadmap
# [sudo] password for suresh: krish123

# sudo apt update

linux_cmds = [
    # 1️⃣ Basic Commands
    ("pwd", "Show current working directory"),
    ("ls", "List files and directories"),
    ("cd <dir>", "Change directory"),
    ("touch file.txt", "Create empty file"),
    ("mkdir folder", "Create new folder"),
    ("rm file.txt", "Remove file"),
    ("rmdir folder", "Remove empty folder"),
    ("cp source.txt dest.txt", "Copy file"),
    ("mv old.txt new.txt", "Move/Rename file"),
    ("cat file.txt", "Show file contents"),
    ("less file.txt", "View file page by page"),
    ("head -n 10 file.txt", "Show first 10 lines"),
    ("tail -f log.txt", "Live view last lines of a file"),
    ("clear", "Clear terminal screen"),
    ("history", "Show previously used commands"),
    ("man ls", "Open manual for a command"),

    # 2️⃣ Intermediate Commands
    ("df -h", "Check disk usage in human-readable format"),
    ("du -sh folder/", "Check size of a folder"),
    ("free -m", "Check RAM usage in MB"),
    ("top", "Show running processes"),
    ("htop", "Interactive process viewer (if installed)"), # sudo apt install htop -y
    ("ps aux", "List all processes"),

    ("kill <PID>", "Stop process using its PID"),
    # Ek naya process run karte hain (sleep 100 command 100 sec tak wait karega)
    # -- ( sleep 100 & ) -> output -> [1] 12345 new PID no
    # ps aux | grep sleep -> to check status, [1]+  Done                    sleep 100
    # kill 12345 -> kill <PID_No>
    # ps -p 1404 -> check process is working or not after kill aur before kill

    # Imp
    ("whoami", "Show current logged user"),
    ("uptime", "Show system uptime"),
    ("uname -a", "Show system info"), ("uname", "show the running env system name now, its (Linux)"),
    ("chmod 755 file.sh", "Change file permissions"),
    ("chown user:user file.txt", "Change file ownership"),
    ("tar -czvf backup.tar.gz folder/", "Compress folder"),
    ("tar -xzvf backup.tar.gz", "Extract compressed file"),
    ("zip -r folder.zip folder/", "Create zip archive"),
    ("unzip folder.zip", "Extract zip archive"),

    # 3️⃣ Networking
    ("ping google.com", "Check internet connection, send unlimited ping"), ("ping -c 5 google.com", "Send limited ping"),
    ("ip addr show", "Show IP address info"),
    ("curl https://example.com", "Send web request"),
    # get only headers <Doctype> to start of <body> only 
    # curl -L https://google.com -> get full HTML of Developer tool
    # curl -I https://google.com -> to check what goes in header data

    # sudo apt install jq -y
    # curl -o /dev/null -s -w "Total time: %{time_total}s\n" https://example.com
    # curl -s https://api.github.com/repos/python/cpython | jq -> get json data on API calls
    # curl -vI https://google.com -> to check if path is avaliable or not
    # curl -v https://example.com/some-page -> error Debugging (500/404 ka reason samajhna)
    # for i in {1..10}; do curl -o /dev/null -s -w "%{http_code}\n" https://example.com; done -> Multiple Requests Load Test Simulation

    ("wget https://file.com/file.zip", "Download file"),
    # Download with a perfect path
    # Note 
    # -O = Output file ka naam + path
    # -P = sirf directory path, naam automatic URL se uthta hai
    # wget -P ~/DesktopLinux/Test/ https://ftp.gnu.org/gnu/wget/wget-1.21.4.tar.gz -> with path
    # wget -O ~/DesktopLinux/Test/my_pdf_1 https://ftp.gnu.org/gnu/wget/wget-1.21.4.tar.gz -> with file name
    
    ("scp file.txt user@host:/path/", "Copy file to remote server"),
    ("ssh user@192.168.1.10", "Login to remote server"),
    ("netstat -tulnp", "Show active ports"),
    ("ss -ltn", "List listening ports"),
    ("traceroute google.com", "Show route packets take"),
    ("dig google.com", "DNS lookup"),

    # 4️⃣ Advanced Text Processing
    ("grep 'error' log.txt", "Search for text in file"),
    ("grep -r 'error' /var/log/", "Recursive search in folder"),
    ("find / -name file.txt", "Find file by name"),
    ("locate nginx.conf", "Fast file search"),
    ("awk '{print $1}' file.txt", "Print first column of file"),
    ("sed 's/old/new/g' file.txt", "Replace text inside file"),
    ("sort file.txt", "Sort lines"),
    ("uniq file.txt", "Remove duplicate lines"),
    ("wc -l file.txt", "Count lines in file"),

    # 5️⃣ Package Management
    ("apt update && apt upgrade -y", "Update system packages (Debian/Ubuntu)"),
    ("apt install <package>", "Install package"),
    ("yum install <package>", "Install package (RHEL/CentOS)"),
    ("dpkg -i package.deb", "Install deb file"),
    ("rpm -ivh package.rpm", "Install rpm file"),

    # 6️⃣ Advanced File Handling
    ("ln -s file link", "Create symbolic link"),
    ("stat file.txt", "Show detailed file info"),
    ("file file.txt", "Show file type"),
    ("mount /dev/sdb1 /mnt", "Mount storage device"),
    ("umount /mnt", "Unmount storage"),
    ("lsblk", "List block devices (disks)"),
    ("df -Th", "Show filesystem types and usage"),

    # 7️⃣ Automation & Scheduling
    ("crontab -e", "Edit scheduled cron jobs"),
    ("crontab -l", "List scheduled jobs"),
    ("at now + 5 minutes", "Run command after 5 min"),
    ("watch -n 5 'ls -l'", "Repeat command every 5 sec"),
    ("alias ll='ls -la'", "Create command shortcut"),
    ("nano ~/.bashrc", "Edit bash startup file"),

    # 8️⃣ Services & Logs
    ("systemctl status nginx", "Check service status"),
    ("systemctl restart nginx", "Restart a service"),
    ("systemctl enable nginx", "Enable service at startup"),
    ("journalctl -xe", "Check detailed system logs"),
    ("tail -f /var/log/syslog", "Live view system log"),
    ("dmesg | less", "Kernel/system boot logs"),

    # 9️⃣ Development & Tools
    ("gcc file.c -o file", "Compile C program"),
    ("python3 script.py", "Run Python script"),
    ("node app.js", "Run Node.js app"),
    ("docker ps", "List running docker containers"),
    ("docker images", "List docker images"),
    ("git clone repo_url", "Clone a git repository"),
    ("git status", "Check git repo status"),
    ("git log --oneline", "Show commit history"),
    ("vim file.txt", "Open file in Vim editor"),

    # 🔟 User & Permissions
    ("adduser newuser", "Create new user"),
    ("passwd newuser", "Change user password"),
    ("su - newuser", "Switch user"),
    ("groups", "Show groups"),
    ("usermod -aG sudo user", "Add user to sudo group"),
    ("id", "Show current user UID & GID"),
]

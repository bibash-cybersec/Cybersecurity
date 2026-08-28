       /      (root  -- Top of everything)
       ├────── /bin   --essential commands (ls,cat, cp,mv)
       ├────── /sbin   -- system/admin cmd (fdisk)
       ├────── /usr   -- users programs and data
       │        ├────── /usr/bin   -- most user cmd
       │        ├────── /usr/sbin   -- non-essential admin cmd
       │        ├────── /usr/lib   -- libraries
       │        └────── /usr/local   -- locally installed software
       ├──────  /etc  -configuration files (imp)
       │           ├────── passwd   -- user account
       │           ├────── shadow   -- password hashes
       │           ├────── hosts   -- local DNS
       │           ├────── network/  -- config
       │           ├────── ssh/   -- SSH config
       │           ├────── cron.d   -- scheduled tasks
       │           ├────── sudoers   -- sudo permission
       │           └────── fstab   -- filesystem mounts
       ├────── /home    -- user home directory
       │         └────── username/   -- each users personal folder
       ├────── /root       -- root user's home directory
       ├────── /var       -- variable data
       │         ├────── /var/log          -- log files (imp)
       │         │          ├────── auth.log      -- authentication log
       │         │          ├────── syslog       -- system logs
       │         │          ├────── apache2/      -- web server logs
       │         │          └──────  nginx/      -- nginx logs
       │         ├────── /var/www      -- web servers files
       │         └────── /var/mail      -- emails
       ├────── /tmp      -- temporary files ( erased on reboot)
       ├────── /dev      --device files
       │         ├────── /dev/sda      -- first hard drive
       │         ├────── /sda/null      -- Trash (discard output)
       │         └────── /sda/zero      -- Generates zero
       ├────── /proc      --running processes
       │          ├────── /proc/1/      -- process ID 1
       │          └────── /proc/net      -- network info 
       ├────── /sys      -- system hardware info
       ├────── /boot       -- boot files
       ├────── /lib       -- essential library
       ├────── /opt      -- optional third party software
       ├────── /mnt      -- temp mount points
       └──────  /media       -- removable media ( USB, CD)

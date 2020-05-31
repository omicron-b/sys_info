# sys_info

![screenshot](https://github.com/omicron-b/sys_info/blob/master/screenshot.png)

## general info
Python script to show basic data in elegant way
This is a work in progress. For now the idea is simplicity. This works fine  
for a small server, where checking only root partition for space is enough.  

`sysinfo.py` outputs RAM and Disk space usage.  
`install.sh` changes directory to `sys_info`, creates Python virtual enviroment and sets it up to avoid bloat on your machine.  
`s_info`     changes directory to `sys_info`, runs `sysinfo.py` in created enviroment, then exits the enviroment and changes directory back to what it was.  

## prerequisites
- Python 3  
- tested on Fedora 29 Server: `sudo dnf install python3-devel`  
- tested on Ubuntu 18.04 Server, Debian 9.7 Stable: `sudo apt install python3-venv python3-pip`  
- tested on Arch Linux: `sudo pacman -Syu python-pip`  

## installation
```
git clone https://github.com/omicron-b/sys_info.git
chmod +x sys_info/install.sh
sys_info/install.sh
```

## removal
- Just remove sys_info folder.
- Optionally remove prerequisites if you do not need them.

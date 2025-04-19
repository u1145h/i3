# i3 Window Manager (Dotfiles)
### 💻 Requirements
- [Termux](https://f-droid.org/packages/com.termux/)
- [Termux X11](https://github.com/termux/termux-x11)

### 🖼️ Screenshots
![01](/screenshot/01.png)
![02](/screenshot/02.png)
![03](/screenshot/03.png)
![04](/screenshot/04.png)
![04](/screenshot/05.png)

### 📦 Basic Installation Guide
Install *proot-distro*
```
pkg install proot-distro
```

#### Arch
```
pkg update && pkg install proot-distro -y
proot-distro install archlinux
```
```
proot-distro login archlinux
```
```
pacman-key --init
pacman-key --populate
pacman -Syu --noconfirm
pacman -S --noconfirm sudo i3 xterm imv zathura rofi pulseaudio-alsa alsa-utils dbus
```
```
useradd -m -G wheel *username*
passwd *username*
```
```
su - *username*
echo "exec i3" > ~/.xinitrc
exit
```
```
exit
```
###### Termux Script to launch i3 WM in Within Termux X11
```
nano arch-i3.sh
```
```sh
#!/data/data/com.termux/files/usr/bin/bash

# Kill existing Termux X11 sessions if any
kill -9 $(pgrep -f "termux.x11") 2>/dev/null

# Start PulseAudio with TCP access
pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1

# Set up Termux X11 environment
export XDG_RUNTIME_DIR=${TMPDIR}
termux-x11 :0 >/dev/null &

# Give X11 time to launch
sleep 3

# Launch X11 main activity
am start --user 0 -n com.termux.x11/com.termux.x11.MainActivity > /dev/null 2>&1
sleep 1

# Login to Arch and run i3 as user u1145h
proot-distro login archlinux --shared-tmp -- /bin/bash -c 'export PULSE_SERVER=127.0.0.1; export XDG_RUNTIME_DIR=${TMPDIR}; su - u1145h -c "env DISPLAY=:0 i3"'

exit 0
```

###### Termux Script to launch i3 WM in Within VNC Viewer
- [Start Script](termux/start-vnc-user.sh)
- [Stop Script](termux/stop-vnc-user.sh)

##### Autostart Apps in i3
edit */home/username/.config/i3/config* and add:
```
exec --no-startup-id pulseaudio --start
exec --no-startup-id xterm
```

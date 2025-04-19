#!/data/data/com.termux/files/usr/bin/bash

# Start Arch and launch VNC server as user u1145h with resolution 1440x900
proot-distro login archlinux --shared-tmp -- /bin/bash -c "su - u1145h -c '/usr/bin/vncserver :1'"

echo "✅ VNC started as u1145h on :1 (port 5901)"

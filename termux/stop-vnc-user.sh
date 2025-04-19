#!/data/data/com.termux/files/usr/bin/bash

proot-distro login archlinux --shared-tmp -- /bin/bash -c "su - u1145h -c 'vncserver -kill :1'"

echo "🛑 VNC server stopped for u1145h (display :1)"


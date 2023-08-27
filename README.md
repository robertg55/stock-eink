# stock-eink

## Initial setup
- Run sudo init.sh to instal dependencies
- Setup automatic login:
	Run: sudo raspi-config
	Choose option: 1 System Options
	Choose option: S5 Boot / Auto Login
	Choose option: B2 Console Autologin
	Select Finish, and reboot the Raspberry Pi.
- Enable SPI Interface: 
	Run: sudo raspi-config
	Chose option: 5 Interfacing Options
	Chose option: P4 SPI
	Chose option: Yes
	Select Finish, and reboot the Raspberry Pi.
- Set startup script to run on login
    Clone repo: git clone https://github.com/robertg55/stock-eink.git
	add permissions to start script: chmod +x ~/stock-eink/start.sh
	edit rc.local with: sudo vi /etc/rc.local
	add to it: sudo ~/stock-eink/start.sh

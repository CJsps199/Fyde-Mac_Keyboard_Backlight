# Fyde-Mac_Keyboard_Backlight - Works on FydeOS, ChromeOS via Brunch or ChromeOS Flex
Chromius Based OS - Macbook keyboard backlight.
Steps to get keyboard backlight working semi fine on Macbook running FydeOS

# 4 Steps:
### Activate Developer Mode on OS
### Install Chromebrew
### Download Python Script
### Activate autostart with  Chrome Autostart

# Activate Developer Mode to access crosh shell:
## Video guide:
[![Watch the video](https://fydeos.io/help/_astro/light-logo.CAcCaTqf.svg)](https://fydeos.io/wp-content/uploads/2024/03/switch-mode.mp4)


> ```
>1: Open the Settings menu.
>2: Select FydeOS Settings.
>3: Click `Enable Developer Mode’to complete the setup.
> ```

# Install Chromebrew:
Thanks to the developers: https://github.com/chromebrew/chromebrew

## Prerequisites
> [!WARNING]
> Please be aware of the fact that developer mode is insecure if not properly configured.

<a id="set_passwd" /> <!-- for reference in installation section -->
> [!TIP]
> Setting a password as instructed in the VT-2 login screen is recommended. It is also recommended to enable signed boot:
>
> ```bash
> sudo chromeos-setdevpasswd
> ```
> ```bash
> sudo crossystem dev_boot_signed_only=1
> ```

## Installation

> [!IMPORTANT]
> The beta, dev, and Canary channels are ***not*** supported and should ***not*** be used with Chromebrew. Failure to take notice of this warning will cause major issues with your Chromebrew installation.
>
> See issue [#2890](https://github.com/chromebrew/chromebrew/issues/2890) and the [FAQ](https://github.com/chromebrew/chromebrew/wiki/FAQ) for more details.

> [!WARNING]
> On ChromeOS M117+, the Chromebrew installer will not work in `crosh` anymore due to the security changes introduced in ChromeOS M117.

Open a VT-2 terminal session with <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> and login with the `chronos` user and password if set [above](#set_passwd). *(if you are unable to do this, please have a second look at the prerequisites and make sure your Chromebook is in developer mode)*

Then run the installation script below:

```bash
bash <(curl -L git.io/vddgY) && . ~/.bashrc
```


> This is mainly to add Python support.
> Chromebrew installs Python by default during installation.

# Add python script:
## Make the root directory writable.

```bash
sudo -i
```

```bash
mount -o rw,remount /
```
## Clone Repository to home directory

```bash
cd /home/chronos/user
```

```bash
 git clone https://github.com/CJsps199/Fyde-Mac_Keyboard_Backlight.git
```

## Copy python file to correct directory

```bash
cd Fyde-Mac_Keyboard_Backlight
```

```bash
cp keyboard-backlight.py /usr/local/bin
```
## Copy bash script to home directory & make script executable

```bash
cp keyboard-startup.sh /home/chronos/user/
```

```bash
chmod +x /home/chronos/user/keyboard-startup.sh
```

# Add Chrome-Autostart:
Thanks to the developers: https://github.com/supechicken/ChromeOS-AutoStart

## Installation
> [!IMPORTANT]
> This extension conflicts with [Secure Shell extension (development version)](https://chrome.google.com/webstore/detail/algkcnfjnajfhgimadimbjhmpaeohhln). (as this extension [used its ID](#How-does-it-works))
>
> Please remove it before installing this extension (if installed), otherwise this extension might not work as expected

- Download [the latest release of this extension (in `zip`)](https://github.com/supechicken/ChromeOS-AutoStart/releases/latest) and unzip it
- Go to `chrome://extensions` and enable Developer Mode
- Click `Load unpacked extension` and select the `ChromeOS-AutoStart-<version>` unzipped folder
- A new window will appear and add command(s) you want to run at startup
- Optional: Click the `Test run` button to test it out after adding a command

> [!NOTE]
> Please do not delete the unzipped folder after loading the extension, otherwise the extension will get deleted after reboot


## Setup to start *keyboard-backlight.py*


- CLick on Extention details: 
> ![image](https://github.com/user-attachments/assets/a37f850d-ae68-4078-8d01-7a6211e0492b)
>
> 
- Click on Extention Options:
> ![image](https://github.com/user-attachments/assets/273f2896-affb-42ed-808a-5ba3432471b6)
>
> 
- Click on Manage Autostart Entries:
> ![image](https://github.com/user-attachments/assets/3a8bde87-d86a-49e2-a97f-e3cf1d6155fb)
>
> 
- Click on Add New Entry:
> ![image](https://github.com/user-attachments/assets/81d9ac39-ed4a-494c-a763-d547ae0dc098)
>
> 
- Add Command:
> ![image](https://github.com/user-attachments/assets/0d1d93ef-968e-47d3-8c1c-7ad4a4cab526)
>
> 
```bash
shell
sudo bash /home/chronos/user/keyboard-startup.sh
<developer password> (this was set when installing Chromebrew)
```
>
>
- Save Script:
> ![image](https://github.com/user-attachments/assets/89da0744-9f7c-43fb-86ae-480c6542d58b)
>
> 
- Test Run Script:
> ![image](https://github.com/user-attachments/assets/be7fd44d-fee7-493b-986d-12e9460626b1)



# Fyde-Mac_Keyboard_Backlight - Works on FydeOS, ChromeOS via Brunch or ChromeOS Flex
Chromius Based OS - Macbook keyboard backlight.
Steps to get keyboard backlight working semi fine on Macbook running FydeOS

# Activate Developer Mode to access crosh shell:
## Video guide:
[![Watch the video](https://fydeos.io/help/_astro/light-logo.CAcCaTqf.svg)](https://fydeos.io/wp-content/uploads/2024/03/switch-mode.mp4)


> ```
>1: Open the Settings menu.
>2: Select FydeOS Settings.
>3: Click `Enable Developer Mode’to complete the setup.
> ```

# Install Chromebrew:
Thanks to the devolopers: https://github.com/chromebrew/chromebrew

## Prerequisites
> [!WARNING]
> Please be aware of the fact that developer mode is insecure if not properly configured.

<a id="set_passwd" /> <!-- for reference in installation section -->
> [!TIP]
> Setting a password as instructed in the VT-2 login screen is recommended. It is also recommended to enable signed boot:
>
> ```bash
> sudo chromeos-setdevpasswd
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

# Add Chrome-Autostart:


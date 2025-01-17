# Fyde-Mac_Keyboard_Backlight
FydeOS - Macbook keyboard backlight.
Steps to get keyboard backlight working semi fine on Macbook running FydeOS

# Activate Developer Mode to access crosh shell:
https://fydeos.io/wp-content/uploads/2024/03/switch-mode.mp4
> ```
>1: Open the Settings menu.
>2: Select FydeOS Settings.
>3: Click `Enable Developer Mode’to complete the setup.
> ```

# Install Chromebrew:
<a id="set_passwd" /> <!-- for reference in installation section -->
> [!TIP]
> Setting a password as instructed in the VT-2 login screen is recommended. It is also recommended to enable signed boot:
>
> ```bash
> sudo chromeos-setdevpasswd
> sudo crossystem dev_boot_signed_only=1
> ```
Then run the installation script below:

```bash
bash <(curl -L git.io/vddgY) && . ~/.bashrc
```

# Add python script:

# Add Chrome-Autostart:


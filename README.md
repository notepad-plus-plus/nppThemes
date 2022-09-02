# Notepad++ Themes Collection

Notepad++ ships with around 20 [themes](https://npp-user-manual.org/docs/themes/) available to define the formatting rules for normal text and syntax highlighting. However, users can create their own themes, or get themes from somewhere else.

To facilitate sharing of user-created themes, the Notepad++ Developers have create this Themes Collection to house the XML files for the user-created themes.

## Using a Theme from this Collection

For now, you have to manually download and install a Theme from this Collection.

1. Download the XML file from the [`themes/` folder](./themes) of this Collection.
   - From the [`themes/` folder](./themes), click on the name of the theme's XML file.
   - From the file's page, click on either the "Raw" button (which will take you to a page where you can copy/paste the raw contents), or even easier, just click on the copy raw contents button, which will immediately place the raw contents in your clipboard for pasting.
       PASTE
   - Do _not_ just right click to try to download the file from the [directory listing on GitHub](./themes), as either of those right-click actions will download the GitHub web page for that file (which is _not_ the Theme's XML file and will _not_ work).
2. Import the file by placing the file in your `themes\` folder
    - For most installations, the easiest place to put a new theme is in the `%AppData%\Notepad++\themes\` folder.
    - If you have multiple users on the same computer, and want the theme available to all users on that machine, put it into `C:\Program Files\Notepad++\themes\` (or `C:\Program Files (x86)\Notepad++\themes` for a 32-bit Notepad++)
    - For portable installations, instead put the themes in the `themes\` sub-folder under the directory where your portable `notepad++.exe` resides
3. Restart Notepad++
4. Select the theme from the [Preferences > Style Configurator](https://npp-user-manual.org/docs/preferences/#style-configurator) dialog

It is also possible to use the menu entry [Settings > Import > Import Style Themes...](https://npp-user-manual.org/docs/preferences/#other-settings-menu-entries) and select a Theme XML file from your computer instead of steps 2-3 above; Notepad++ will then install it in the right place.

## Submitting your Theme to the Collection

You can submit your Theme file(s) into this repo if you would like to share it with the general public.  

To do so, you may either:
- Create a Pull Request: create your own fork of this repository; add the new theme XML file to the themes folder your fork; and finally, create the Pull Request (PR).
- or Create a new Issue: go to the [issues](../../issues) page for this repository, click on the **New issue** button, give it a meaningful issue name, and attach the theme's .XML file to the issue, then submit the issue.

The Theme Collection team will validate your theme (using manual review and/or automated tools), and will decide whether or not to accept your submission.  

The original author of any Theme in this Collection may [request](../../issues) that we remove it from the Collection (or submit a PR to do the same), and we will oblige.

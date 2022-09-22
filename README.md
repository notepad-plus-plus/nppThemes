# Notepad++ Themes Collection

Notepad++ ships with around 20 [themes](https://npp-user-manual.org/docs/themes/) available to define the formatting rules for normal text and syntax highlighting. However, users can create their own themes, or get themes from somewhere else.

To facilitate sharing of user-created themes, the Notepad++ Developers have create this Themes Collection to house the XML files for the user-created themes.

## Using a Theme from this Collection

For now, you have to manually download and install a Theme from this Collection.

1. Download the XML file from the [`themes/`](./themes) folder of this Collection.
   - From the [`themes/`](./themes) folder, click on the name of the theme's XML file.
   - From the file's page, click on either the "Raw" button (which will take you to a page where you can copy/paste the raw contents), or even easier, just click on the copy raw contents button, which will immediately place the raw contents in your clipboard for pasting.
       ![image](https://user-images.githubusercontent.com/17455758/188165490-c27c8931-03b7-4012-89a5-506ca650c276.png)
   - Do _not_ just right click to try to download the file from the [directory listing on GitHub](./themes), as either of those right-click actions will download the GitHub web page for that file (which is _not_ the Theme's XML file and will _not_ work).
2. Import the file by placing the file in your `themes\` folder
    - For most installations, the easiest place to put a new theme is in the `%AppData%\Notepad++\themes\` folder.
    - If you have multiple users on the same computer, and want the theme available to all users on that machine, put it into `C:\Program Files\Notepad++\themes\` (or `C:\Program Files (x86)\Notepad++\themes` for a 32-bit Notepad++)
    - For portable installations, instead put the themes in the `themes\` sub-folder under the directory where your portable `notepad++.exe` resides
3. Restart Notepad++
4. Select the theme from the [Preferences > Style Configurator](https://npp-user-manual.org/docs/preferences/#style-configurator) dialog

It is also possible to use the menu entry [Settings > Import > Import Style Themes...](https://npp-user-manual.org/docs/preferences/#other-settings-menu-entries) and select a Theme XML file from your computer instead of steps 2-3 above; Notepad++ will then install it in the right place.

## Submitting your Theme to the Collection

### Theme Best Practices

- Include a comment block near the top of the theme, listing things including
   - Name of the Theme
   - Author (you)
   - Date of creation or last modification
   - Any other credits or acknowledgements or notes you'd like the user to see when downloading
- When possible, make use of "background inheritance" (set `colorStyle="1"` in the raw XML or right click on the **Background colour** input in the Style Configurator) so that styles for various language markups inherit the **Default Style**'s background colour -- this will mean that a user of your theme only has to change one entry to get the background to change on hundreds of style entries.  The [99er theme](https://github.com/notepad-plus-plus/nppThemes/blob/main/themes/99er.xml) includes the steps used to do that in a bulk search-and-replace to the raw XML.

See the [default styler](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/stylers.model.xml) and the [themes included with Notepad++ distributions](https://github.com/notepad-plus-plus/notepad-plus-plus/tree/master/PowerEditor/installer/themes) for good examples of Themes.

### Submission Process

You can submit your Theme file(s) into this repo if you would like to share it with the general public.  

To do so, you may either:
- Create a Pull Request: create your own fork of this repository; add the new theme XML file to the themes folder your fork; and finally, create the Pull Request (PR).
- or Create a new Issue: go to the [issues](../../issues) page for this repository, click on the **New issue** button, give it a meaningful issue name, and attach the theme's .XML file to the issue, then submit the issue.

The Theme Collection team will validate your theme (using manual review and/or automated tools), and will decide whether or not to accept your submission.  Following the Best Practices (above) will help ensure your submitted Theme is added into the Collection.

### HOW TO Submit Pull Request

Since many contributors are not GitHub experts, we have added in this section to make it easier for you to submit your file in a Pull Request (PR)

0. Create a GitHub account 
   - Without an account, you cannot submit a PR
2. Create a **fork** of the Themes Collection
   - Click the **Fork** label/icon from the [main UDL Collection page](https://github.com/notepad-plus-plus/nppThemes)
   - ![image](https://user-images.githubusercontent.com/17455758/191838275-f4237476-0e99-45f7-8bc7-251e8936f1d3.png)
   - If you already have a fork, use **Sync Fork > Update Branch** to make sure your fork is up-to-date with the main Collection
3. Make your changes:
   - Upload the Theme's XML file to the `themes\` folder _in your fork_
4. Create a PR from your fork
    - from your fork's master branch, after you've made the changes above,
    - click the down arrow on **Contribute** 
    - select **Open Pull Request**
    - fill out your description for the PR, and submit the PR

## Automatic License

Any Theme uploaded to the Collection is automatically released under the terms of the GPL v3, as put forth in the Collection's [LICENSE](./LICENSE) file.  If you do not want to publish your Theme under that license, do not submit it to this Collection.

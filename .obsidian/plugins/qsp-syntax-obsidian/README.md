# QSP-syntax HighLghting for Obsidian
<!-- https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin -->

This plugin based on fork of [sample plugin](https://github.com/obsidianmd/obsidian-sample-plugin) for [Obsidian](https://obsidian.md) and [lean-syntax-highlight
](https://github.com/tomaz1502/lean-syntax-highlight/tree/main?tab=readme-ov-file) by tomaz1502.

Stand this plugin into your Obsidian storage:

1. Find folder `.obsidian` into you Obsidian storage folder.
2. Go to folder `plugins`
3. Extract folder `qsp-syntax-obsidian` from [arch](https://github.com/AleksVersus/qsp-syntax-obsidian/releases) of this realese.
4. Load or reload Obsidian
5. In Obsidian, open **Settings**.
6. In the side menu, select **Community plugins**.
7. Select **Turn on community plugins**.
8. Under Installed plugins, enable the **QSP-syntax highlight** by selecting the toggle button next to it.
9. Prove syntax work by this fragment:

````
```qsp
local $top_text = $args[0] & ! text from top
local $command = $iif($args[1]<>"", $args[1], "*pl") & ! command for print text
local $screen = $mid($args[1], 1, 1) & ! first symbol from command
local $text = ""
if $screen="*":
	! if fist symbol is *
	! main description wondow
	$text=$maintxt
else
	! addition description window
	$text=$stattxt
end
! use dynamic for run command:
dynamic "
	<<$screen>>clr
	<<$command>> $args[0]
	<<$screen>>p $args[1]
", $top_text, $text
```
````

if syntax don't work, reload page, or type text in codeblock.

- ask me: aleksversus@mail.ru
- "Subscribe my boosty": "https://boosty.to/aleksversus",
- "Donate": "https://www.donationalerts.com/r/aleksversus"

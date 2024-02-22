
<div align=center><img src = "https://www.renpy.org/static/index-logo.png"></div>

# <div align=center>Renpy Translator</div>

<div align=center>A free and open-source translator for ren'py</div>

<div align=center><img src= "https://camo.githubusercontent.com/60c21c6ef57c61b0a329f621af32f87c9b4ffe0283eeebe8a453e60de2675c51/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6c616d612d636c65616e6572"></div>

------

<div align=center><img src = "https://github.com/anonymousException/renpy-translator/blob/main/docs/img/interface_v1.5.3.png"></div>

<div align=center><img src = "https://github.com/anonymousException/renpy-translator/blob/main/docs/img/translated_contents.png"></div>

------

## Another Docs

## AI Version

If you want to use offline ai translation, you can refer to :

https://github.com/anonymousException/renpy-translator/blob/feature/ai-translate/README.md

### Chinese

<div align=center>中文版 README 在 <a href = 'https://github.com/anonymousException/renpy-translator/blob/main/README_zh.md'>这里</a> </div>

## Target

As you see the above translated contents. The original contents will be remained after translation.

If the contents are short of the original contents(behind the "#" as comment) , translation will not take effect on them

The reason why I made this tool is not to replace the real translator's work , but to help.

The translated contents will be not accurate enough due to auto google | youdao | deepl translation. 

So the original contents will do the effect. You can re-translate the translated contents according to the original contents. And what you modified will not be replaced during next translation.

This tool also take care of the special symbols like "{}"  "[]" and "<>"   in untranslated contents , for detail you can see it on the [Features point 2](#jump_features)

## Download

You can download the latest version through https://github.com/anonymousException/renpy-translator/releases/latest

## <span id ="jump_features">Features</span>

- Completely free and open-source
- Support **special symbols** in untranslated contents like "{}"  "[]" and "<>"  , the contents in special symbols will not be translated.  Example:
- ```python
  # untranslated contents:
  # "Your name is [povname], right?"
  
  # Chinese translated:
  "你的名字是 [povname] ，对吗？"
  
  # Japanese translated:
  "あなたの名前は [povname] ですよね?"
  ```

- Support  extract the untranslated words ren'py engine has not discovered
- Support input,brower and drag the file(s) and directory
- Support translate/extract for single rpy file
- Support translate/extract for all rpy files under directory
- Support **replace the fonts** used by translated language
- Support **be compatible with** the translated game that not translated by this translator. The translated contents before will be remained and just translate the untranslated contents
- Support **108** kinds of language (Default Google Translation) , you can view the [google support source](https://github.com/anonymousException/renpy-translator/blob/main/src/google.source.rst?plain=1) and the [google support target](https://github.com/anonymousException/renpy-translator/blob/main/src/google.target.rst?plain=1)
- Support **remain the original words as comments** after translation
- Support **real-time log output** , you can check the progress about the translation
- Support **local-proxy** , if you can not access google , you can use a vpn tool like v2ray and set local proxy
- Support **multi** translation engine : Google Translation from [pygtrans](https://github.com/foyoux/pygtrans/tree/main) , YouDao Translation , DeepL Translation , OpenAI Translation

------

## Usage

Translate Files:

https://github.com/anonymousException/renpy-translator/assets/157234942/495be06c-9751-4966-b22c-84602fb3dc0a

Translate Directory:

https://github.com/anonymousException/renpy-translator/assets/157234942/0034bbaa-d1fc-4981-b228-9bde62423367

Replace fonts:

https://github.com/anonymousException/renpy-translator/assets/157234942/46e524d7-14ef-472e-8426-ac47d923bef0

Extract File(s):

https://github.com/anonymousException/renpy-translator/assets/157234942/7d1efbfd-7152-407f-9896-c63a98538f02

Extract Directory:

https://github.com/anonymousException/renpy-translator/assets/157234942/817c6e9c-2fa2-48a3-914f-85765c0b64c3

## Tutorial

### Prerequisite

A good network environment , if not you may not able to translate words through ***Google Translate | YouDao Translate | Deepl Translate***

If you can not access the translate engine, you can try use vpn tool like v2ray and set local-proxy

before:

![proxy_fail](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/proxy_fail.png)

usage:

![proxy_setting](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/proxy_setting.png)

------

An unpacked ren‘py game (for what you can find .rpa files under the game directory)  like this:

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/unpacked.png)

You can try to translate [the tutorial game](https://github.com/anonymousException/renpy-translator/blob/main/docs/demo_game/DemoGame-1.0-win.zip) following the tutorial

if not you can try to unpack it

I usually use [UnRen-ultrahack.bat](https://github.com/anonymousException/renpy-translator/blob/main/docs/tool/UnRen-ultrahack.bat) from https://f95zone.to/ to unpack the game

It's **strongly not recommended** for translators to make translation through unpack and then deliver a translated version without the original author's permission. Please **respect** the original author

Download the  [UnRen-ultrahack.bat]() and copy it to the game directory (where game.exe locates)

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/move_unren.png)

Double-Click the UnRen-ultrahack.bat and the following console will show

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/unren_console.png)

Input 9 and then Enter and then Enter y

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/unren_console2.png)

Wait for a moment and then the unpack will be over

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/unren_console3.png)

------

### FirstTranslation

If the game is completely blend-new for you to translate , you can continue to the following contents

If the game has already been translated , you want to update the translation (translate the contents still not been translated) , you can jump to the next caption :  [UpdateTranslation](#jump-update-translation)

the first thing for the First-Translation is to extract the untranslated words from game

there are two methods to do that:

- Official Extract (extract function supported by the ren'py engine)
- [Tool Extract](#jump-tool-extract) (extract function supported by this tool)

It's recommended to use [Offical Extract](#jump_official_extract) first and then translate the game. If you found that there still remains plenty of words not been translated after translation (Sometimes ren'py engine's official extract may miss many words). You can use the tool extract function and retranslate the game.

#### <span id = "jump_official_extract">Official Extract(Recommend) </span>

https://github.com/anonymousException/renpy-translator/assets/157234942/b032480f-fc2f-4438-9730-611b3e219556

you can forward to https://www.renpy.org/ and then download the latest version

Unzip the ren'py engine you download

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_folder.png)

Click "preferences" in the lower right corner

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_interface.png)

Reset the "Projects Directory" to the parent directory of the game you want to translate

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_preference.png)

Return back to the last interface and Click "Generate Translations"

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_interface2.png)

Fill the "Language" , this is just a tag (It's related to the "tl name" label in this tool) used for the translation that you can name whatever you want. But it's recommended to name the target language you want to translate. Such as "japanese" or "chinese" etc.

It would be alright to keep other options default ,Especially for "Generate Translations" option , do not tick the "Generate empty strings for translations"

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_gen_translate.png)

After all options have been set . Click the "Generate Translations" and wait to complete

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_gen_tranlate_over.png)

And then you can close the software , the official extract is done

You can see the generated folder , remember the path

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_gen_translate_folder.png)

The folder path in this tutorial is : 

```
F:\Games\RenPy\DemoGame\game\tl\japanese
```

#### <span id = "jump-tool-extract"> Tool Extract(Optional)</span>

Fill (input,drag or brower) the directory that generated by [Official Extract](#jump_official_extract) before and just tap the extract buttion , and then extraction will be done

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_translator_extract.png)

Quite easy, right ? That's why I made this tool.

#### Add Entry

https://github.com/anonymousException/renpy-translator/assets/157234942/a0316ab5-f912-4e25-8423-19b82b7fbfbe

You need to add an entry to change the language in game

Open the game directory and then enter subfolder "game", open the "screens.rpy" file (you can use notepad to open it)

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/screens.rpy_folder.png)

Search the key words："game_menu(_("Preferences")" (usually the words do effect if not you may need to explore what the game use to replace "Preferences")

Normally you will found many "vbox:" like this:

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/screens_notepad.png)

Try to find a vbox that contains "Language" or some other words can replace "Language"

If not found , add the following code to the file(the location next to the vbox contains "skip"):

```python
vbox:
    style_prefix "radio"
    label _("Language")
    textbutton "English" action Language(None) 
    textbutton "LanguageName" action Language("The Tag you fill in official Extract") 
    #such as textbutton "turn to Japanese" action Language("japanese")
```

Pay attention to the indentation to keep it aligned. After edit it should be like this

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/screens_notepad_edit.png)

------

If found , just add a new line to the vbox:

```python
textbutton "LanguageName" action Language("The Tag you fill in official Extract") 
#such as textbutton "turn to Japanese" action Language("japanese")
```

------

After the file saved,open the game and make sure the preference show the content you just edit

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/game_language.png)

------

#### Translation

https://github.com/anonymousException/renpy-translator/assets/157234942/9b1c0b9f-7f90-4a90-9876-6588994d0658

Before translation you need to get the font file (.*ttf or .otf) you want to translate

For japanese, I usually use the [hanazomefont](https://www.asterism-m.com/font/hanazomefont/)

For chinese, I usally use the [SourceHanSansCN](https://github.com/CyanoHao/WFM-Free-Font/tree/master/SourceHanSansCN)

For other language , you can find relative font files using search engine easily

Open the ren'py translator and fill the following blanks

directory : the path  generated during [Official Extract](#jump_official_extract) before

font: the font file you downloaded

target : the target language you want to translate (input the letter in front of the target language to search  is supportable , need not to scroll to search)

source: default Auto Detect is OK

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_translator_translate.png)

Wait until the translation done:

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_translator_translate_over.png)

So far , the translation is done , you can open game and check it : 

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/game_language_translated.png)

### <span id = "jump-update-translation"> UpdateTranslation </span>

Update-Translation is quite easy, directly use the [Official Extract](#jump_official_extract) (optional) and [Tool Extarct](#jump-tool-extract)

After extraction ,  just input the directory generated during [Official Extract](#jump_official_extract) and choose the target , font can leave empty because it has been replaced before

![img](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/renpy_translator_update_translate.png)

## Development

If you are willing to develop based on this project. You will need to have a python3 environment.

And install the following packages ：[requirements.txt](https://github.com/anonymousException/renpy-translator/blob/main/src/requirements.txt)

## FAQ

### All the translation skip

![skip](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/translation_all_skip.png)

Make sure when you in [Official Extract](#jump_official_extract) step , for "Generate Translations" option , do not tick the "Generate empty strings for translations"

The translation will only do effect when the format like this:

```python
# game/script.rpy:553
translate schinese naming_0f7b6e71:
	# r "Do name yourself like that and I'll break your face..."
	r "Do name yourself like that and I'll break your face..."
```

or

```python
    # game/script.rpy:30886
    old "Win or Lose?"
    new "Win or Lose?"
```

------

Notice that the original text (behind # or old) should be **the same with** untranslated text (behind no # or new)

------

### <span id = "jump_error_translate_special_symbols">Some errors made it impossible to translate certain lines</span>

you may meet errors like this:

```python
2024-01-30 14:55:19 Error in line:1320 D:\Download\Nova-Pasta\SunshineLoveCH2-1.01-pc\game\tl\Portugues/10_week10_00.rpy
"It’s [s_name]. And [y_name]."
It’s [0] . And [1] . Error
"É [0] . E 1] ."
```

It's depend on the translation result. In order to skip translate special symbols like '[]' '{}' '<>' , this tool will replace the contents in special symbols in order nums.

For example :

"It’s [s_name]. And [y_name]."

will be replaced to

"It’s [0] . And [1] ."

Normally, this format will not be translated and will remain '[0]' and '[1]' , and the tool will restore the orginal contents with the ordered nums.

However , sometimes this format may be destroyed after translation. As mentioned ： "É [0] . E 1] ."

You can found that one '[' is missing , so this tool can't restore the original contents. And will not translate this line.

You may need to modify these certain lines manually.

Fortunately this situation occurs rarely , you need not to spend too much time to modify these certain lines.

### Anti-virus software report viruses

This program is packed by pyinstaller and with file operation (open read write) ， so may cause false detection

If you are worried about this , you can download the source code and run the program yourself

### Some errors occur after running the translated game

you may meet errors after running the translated game like this :

![error_after_translation](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/error_after_translation.png)

![error_after_translation_source](https://github.com/anonymousException/renpy-translator/blob/main/docs/img/error_after_translation_source.png)

You can found that after translation "[[XXXX]" was translated into "[ [XXXX]" , an extra space was added  (you may meet other error format but the important point is that after translation **the structure of the special symbols destroyed**)

The result is translated by translate engine , sometimes translation engine **is not friendly to** special symbols like '[]' '<>' ... especially when the special symbols used repeatedly

But there still remains good news , normally the case will not happen frequently , you only need to modify the error sentences manually (For the case mentioned above , just remove the extra space)

### Some sentences seem not to be translated after translation

#### tooltip

For special text in **tooltip** is actually translated but seems not work

the original code looks like this :

```python
tooltip "this is a tooltip"
```

Following the tutorial from https://f95zone.to/threads/translation-of-text-in-screen.90781/

Just open the rpy file (any one under tl folder else if you can create a new one) and add the following code :

```python
# if you choose to create a new one，you need to add the next line remove header # and relace tl_name with the directory name under tl folder like japanese
#translate tl_name strings:
	old "[tooltip]"
    new "[tooltip!t]"
```

#### notify

For special text in **notify** is actually translated but seems not work

You need to locate the sentence on the orginal code (not the translation tl folder)

You will found the original code looks like this :

```python
show screen notify(_("Find old Man Gibson"), None)
```

------

replace it with

```python
show screen notify(__("Find old Man Gibson"), None)
```

the operation is just to add '_' after notify(

quite easy right? And then the translation will do the effect

#### other

It probably remains other case that some sentences seem not to be translated after translation

It depends on the original code , extraction may not completely covered if the original code is not quite translation-friendly

To avoid extra useless extraction , the extraction function in this tool will not extract sentences match the following style :

the length of sentences (space and special synbol will be counted as zero length)  lower than 8 

for example :

```
"I know [special symbol]"
```

the actual effect content is

```
Iknow
```

the length is only 5 , so it will not be extracted by the extraction from the tool

------

Besides the contents in [ConditionSwitch()](https://www.renpy.org/doc/html/displayables.html#ConditionSwitch) will also not be translated due to switch code may contained in it

### OpenAI

You can view your rate-limits on : [rate-limits](https://platform.openai.com/account/rate-limits)  and set a reasonable limit

There are great restrictions for a new user of openai , can only post max 3 requests in per minute. almost **unusable** to translate

The default setting is for this situation , If you don't pay much attention to the time cost , you can try it with the default config

For higher-level user , it's recommended to turn up the setting. A suggested config is :

| parameter                  | recommend                                                    |
| -------------------------- | ------------------------------------------------------------ |
| RPM(requests per minute)   | 250                                                          |
| RPS(requests per second)   | 10                                                           |
| TPM(requests token limits) | [rate-limits](https://platform.openai.com/account/rate-limits) |
| model                      | gpt-4-turbo-preview                                          |

OpenAI seems not to be friendly to special symbols like '{}' '[]' , you may meet errors mentioned before : [Some errors made it impossible to translate certain lines](#jump_error_translate_special_symbols)

You can re-translate the error lines with google engine (translated lines will be **auto skipped** , just re-translate the full directory or file(s) translated before)

(Google translation is more friendly to the special symbols but may still remain few errors) 

At last you need to modify the remained **few** error lines manually

Besides if you meet traceback errors in openai , try to disable the option Multi-Translate and re-translate (it's more stable but slower). 

And you may meet errors like this:

```python
2024-02-22 11:18:28	Traceback (most recent call last):
  File "openai_translate.py", line 180, in translate_limit
  File "json\__init__.py", line 346, in loads
  File "json\decoder.py", line 337, in decode
  File "json\decoder.py", line 353, in raw_decode
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 1613 (char 1612)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "openai_translate.py", line 187, in translate_limit
Exception: Unterminated string starting at: line 1 column 1613 (char 1612)
```

It's due to the error format data returned by openai , fortunately this will not happened frequently and will only cause partially untranslated in one file. You can re-translate the untranslated lines with other translation engine such as google translation

Another problem is that openai may merge multi-translation result occasionally , such as:

```
#untranslated
["Hello","Good"]
#translated
["こんにちは,良い"]
```

This can lead to mismatching of translations ， so the partial translation will not do effect , you may need to translate the untranslated lines with other translation engine


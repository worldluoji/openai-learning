# Renpy
Ren'Py is a <strong>visual novel engine</strong> – used by thousands of creators from around the world – 
that helps you use <strong>words, images, and sounds</strong> to tell interactive stories that run on computers and mobile devices. 

These can be both visual novels and life simulation games. 
The easy to learn script language allows anyone to efficiently write large visual novels, 
while its Python scripting is enough for complex simulation games.

<br>


## "Tutorial" and "The Question"
The terms "Tutorial" and "The Question" in the context of Ren'py refer to different aspects of using or interacting with a game created using this engine:
- Tutorial: It refers to a section or mode designed to teach users how to play the game or use its features. 
For a Ren'py game, this could be a guided introduction that teaches players about the game mechanics such as clicking choices, navigating menus, saving/loading progress, and understanding how dialogue and narrative work within the game.
- The Question: It would typically be a part of that game's storyline or gameplay. 
It might be a critical decision point or a puzzle element where the player must make a choice or answer a question that affects the story progression or character development. 

<br>

## images
For example, the following files, placed in the images directory, define the following images.
- "bg meadow.jpg" -> bg meadow
- "sylvie green smile.png" -> sylvie green smile
- "sylvie green surprised.png" -> sylvie green surprised

```
# 定义角色
define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

label start:

    scene bg meadow

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    # 第二次执行show会替换掉前面show的图片
    show sylvie green surprised

    "Silence."
```
The scene statement on line 6 clears all images and displays a background image. 
The show statements on lines 16 and 26 display a sprite on top of the background, and change the displaying sprite, respectively.


### Hide Statement
Ren'Py also supports a hide statement, which hides the given image.
```
label leaving:

    s "I'll get right on it!"

    hide sylvie

    "..."

    m "That wasn't what I meant!"
```

### Image Statemen
Sometimes, a creator might not want to let Ren'Py define images automatically. 
This is what the image statement is for. It should be at the top level of the file (unindented, and before label start), 
and can be used to map an image name to an image file. For example:
```
image logo = "renpy logo.png"
image eileen happy = "eileen_happy_blue_dress.png"
```

<br>

## Transitions
In the script above, pictures pop in and out instantaneously. 
Since changing location or having a character enter or leave a scene is important, 
Ren'Py supports transitions that <strong>allow effects to be applied when what is being shown changes</strong>.

```
label start:

    scene bg meadow
    with fade

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"
```
The with statement takes the name of a transition to use. 
The most common one is <strong>dissolve which dissolves from one screen to the next</strong>. 
Another useful transition is <strong>fade which fades the screen to black, and then fades in the new screen</strong>.

<br>

## Positions
By default, images are shown centered horizontally, and with their bottom edge touching the bottom of the screen. 
This is usually okay for backgrounds and single characters, but when showing more than one character on the screen it probably makes sense to do it at another position. 
It also might make sense to reposition a character for story purposes.
```
    show sylvie green smile at right
```
- left for the left side of the screen
- right for the right side
- center for centered horizontally (the default)
- truecenter for centered horizontally and vertically.

<br>

## Music and Soundlink
Most Ren'Py games play music in the background. Music is played with the play music statement. 
The play music statement takes a filename that is interpreted as an audio file to play. 

Audio filenames are interpreted relative to the game directory. Audio files should be in opus, ogg vorbis, or mp3 format.

For example:
```
    play music "audio/illurock.ogg"
```

When changing music, one can supply a fadeout and a fadein clause, which are used to fade out the old music and fade in the new music.
```
    play music "audio/illurock.ogg" fadeout 1.0 fadein 1.0
```

The queue music statement plays an audio file after the current file finishes playing.
```
    queue music "audio/next_track.opus"
```

Music can be stopped with the stop music statement, which can also optionally take a fadeout clause.
```
    stop music
```

play sound statement. Unlike music, sound effects do not loop.
```
    play sound "audio/effect.ogg"
```

<br>


## Pause Statementlink
The pause statement causes Ren'Py to pause until the mouse is clicked.
```
    pause
```
If a number is given, the pause will end when that number of seconds have elapsed.
```
    pause 3.0
```

<br>

## Ending the Gamelink
You can end the game by running the return statement, without having called anything. 
Before doing this, it's best to put something in the game that indicates that the game is ending, 
and perhaps giving the user an ending number or ending name.
```
    ".:. Good Ending."

    return
```

<br>

## Menus, Labels, and Jumpslink
The menu statement lets <strong>presents a choice</strong> to the player:
```
s "Sure, but what's a \"visual novel?\""

menu:

    "It's a videogame.":
        jump game

    "It's an interactive book.":
        jump book

label game:

    m "It's a kind of videogame you can play on your computer or a console."

    jump marry

label book:

    m "It's like an interactive book that you can read on a computer or a console."

    jump marry

label marry:

    "And so, we become a visual novel creating duo."
```

<br>

## Supporting Flags using the Default, Python and If Statements

```
# True if the player has decided to compare a VN to a book.
default book = False
...
label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    jump marry
```
The book flag starts off initialized to the special value False (as with the rest of Ren'Py, capitalization matters), meaning that it is not set. 
If the book path is chosen, we can set it to True using a Python assignment statement.

<strong>Lines beginning with a dollar-sign are interpreted as Python statements</strong>.

To check the flag, use the if-else statement:
```
if book:

    "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

else:

    "Sylvie helped with the script on our first video game."
```
Python variables need not be simple True/False values. 
Variables can be used to store the player's name, a points score, or for any other purpose. 

Since Ren'Py includes the ability to use the full Python programming language, many things are possible.

<br>

## reference
- https://www.renpy.org/doc/html/quickstart.html
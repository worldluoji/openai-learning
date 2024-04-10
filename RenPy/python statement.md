# python statement
The python statement takes a block of Python, and runs the block when control reaches the statement. 
A basic Python statement can be very simple:
```
python:
    player_health = max(player_health - damage, 0)
    if enemy_vampire:
        enemy_health = min(enemy_health + damage, enemy_max_health)
```

## One-line Python Statement
```
# Set a flag.
$ flag = True

# Initialize a variable.
$ romance_points = 0

# Increment a variable.
$ romance_points += 1

# Call a function that exposes Ren'Py functionality.
$ renpy.movie_cutscene("opening.ogv")
```

## Init Python Statement
The init python statement runs Python at initialization time, before the game loads. Among other things, 
this can be used to define classes and functions, or to initialize styles, config variables, or persistent data.
```
init python:

    def auto_voice_function(ident):
        return "voice/" + ident + ".ogg"

    config.auto_voice = auto_voice_function

    if persistent.endings is None:
        persistent.endings = set()

# A priority number can be placed between init and python. When a priority is not given, 0 is used
init 1 python:

    # The bad ending is always unlocked.
    persistent.endings.add("bad_ending")
```

<br>

## reference
https://www.renpy.org/doc/html/python.html#python-statement
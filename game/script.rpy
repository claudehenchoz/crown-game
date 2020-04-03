define j = Character("Journalist")

screen stats_overlay():
    if public_image > 0:
        text 'IMAGE {color=#0f0}[public_image]{/color}' align (0.95, 0.04)
    elif public_image < 0:
        text 'IMAGE {color=#f00}[public_image]{/color}' align (0.95, 0.04)
    else:
        text 'IMAGE [public_image]' align (0.95, 0.04)
    if finances > 0:
        text 'FINANCES {color=#0f0}[finances]{/color}' align (0.95, 0.08)
    elif finances < 0:
        text 'FINANCES {color=#f00}[finances]{/color}' align (0.95, 0.08)
    else:
        text 'FINANCES [finances]' align (0.95, 0.08)
    if public_health > 0:
        text 'HEALTH {color=#0f0}[public_health]{/color}' align (0.95, 0.12)
    elif public_health < 0:
        text 'HEALTH {color=#f00}[public_health]{/color}' align (0.95, 0.12)
    else:
        text 'HEALTH [public_health]' align (0.95, 0.12)
    if karma > 0:
        text 'KARMA {color=#0f0}[karma]{/color}' align (0.95, 0.16)
    elif karma < 0:
        text 'KARMA {color=#f00}[karma]{/color}' align (0.95, 0.16)
    else:
        text 'KARMA [karma]' align (0.95, 0.16)
init python:
    config.overlay_screens.append('stats_overlay')


# The game starts here.

label start:

    $ public_image = 0
    $ finances = 0
    $ public_health = 0
    $ karma = 0

    scene bg bundeshaus
    play music "audio/bundeshaus-theme1.ogg"

    show journalist happy

    j "The new Coronavirus outbreak in Wuhan..."
    j "It will reach us quickly."
    j "What will you do about it?"

    menu:
        "We will close the borders":
            $ finances -= 1
            $ public_health += 1
            jump bordersclosed
        "We will observe the situation further":
            $ public_image -= 1
            $ public_health -= 1
            jump furtherobservation
        "We will declare lock-down":
            $ public_image += 1
            $ public_health += 1
            $ finances -= 1
            jump lockdown


label bordersclosed:
    scene bg bundeshaus
    play music "audio/bundeshaus-theme2.ogg"
    show journalist happy

    j "Oh really. That is... bold."
    j "Won't this negatively impact finances? FINANCES: %(finances)s"

    play music "audio/bundeshaus-theme3.ogg"

    j "But it is good for our health? HEALTH: %(public_health)s"
    j "Let's see what happens"

    return

label furtherobservation:
    scene bg bundeshaus
    show journalist happy

    j "Okay, but what about our neighbors, who all took immediate action?"

    return

label lockdown:
    scene bg bundeshaus
    show journalist happy

    j "Thank you."

    return

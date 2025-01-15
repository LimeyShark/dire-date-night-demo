#DIRE DATE NIGHT CODE!!
#Author: Beatrice Stotz
#12/29/24

define e = Character('Emory', image = 'mc', color = "#748651") # #jacket 525F38  #gry #b1b1b1
define et = Character('Emory', image = 'mc', what_italic=True, what_prefix="*", color = "#748651") #EMORY THOUGHTS
define a = Character('Avery', image = 'mc', color = "#b7495f")
#define at = Character('Avery', image = 'mc', what_italic=True, what_prefix="*", color = "#b7495f") #avery thoughts. Does avery every think :sob:
define n = Character(None, image = 'mc', what_italic=True) 
define h = Character('Hostess', image = 'h', color= "#d05816")
define w = Character('Waiter', image = 'w', color="#758a87")
default aff = 0 #affection
define config.window_hide_transition = None
#Cannot use what_suffix, makes "extend" look weird


image bg app = "bg app.png"
image app2= "bg app2.png"
image bg timed1= "bg timed1.png"
image bg timed2= "bg timed2.png"
image bg timed3="bg timed3.png"
image bg instruct1="bg instruct1.png"
image bg instruct2="bg instruct2.png"
image bg demoEnd1= "bg demoEnd1.png"
image bg demoEnd2= "bg demoEnd2.png"
image bg demoEnd3= "bg demoEnd3.png"
image bg demoEnd0good= "bg demoEnd0good.png"
image bg demoEnd0bad= "bg demoEnd0bad.png"
image bg demoEnd0quick= "bg demoEnd0quick.png"




init python:
    renpy.music.register_channel("music_2")
    config.window_hide_transition= None


screen cd: 
    timer 0.001 repeat True action If(time > 0, true=SetVariable('time', time-0.01), false=[Hide('cd'), Jump(timer_jump)])
    bar value time*100 range timer_range*100 xalign 0.5 yalign 0.662 xmaximum 1680

label timer(x,y,z):
    $ time = x 
    $ timer_range = y
    $ timer_jump = z
    window hide
    show screen cd 
    return

screen affectionMeter(): #for testing purposes
    $ string1= "Affection: %d" % aff
    text string1:
        xalign 0.05
        yalign 0.05

screen underConstruction():
    text "{color=#f00}{size=150}I HAVENT DRAWN THIS YET!!!":
        xalign 0.5
        yalign 0.5
        
image warning = "warning.png" 
label warn:
    show warning onlayer overlay:
        xalign 0.815
        yalign 0.95
    return





label start:
    scene bg timed1 with Fade(0,0,1)
    python:
        for x in range(3):
            renpy.show('bg timed1')
            renpy.pause(0.5)
            renpy.show('bg timed2')
            renpy.pause(0.5)
            renpy.show('bg timed3')
            renpy.pause(1)
    scene bg instruct1 with Fade(0.5,0.5,0.5, color="#A0699E") 
    pause(1)
    show bg instruct2 with Dissolve(1)
    pause
    play music "track1outside.mp3" loop 
    scene bg app with Fade(0.5,0,0.5, color="#A0699E")
    python:
        for x in range(3):
            renpy.show('app2')
            renpy.pause(0.5)
            renpy.hide('app2')
            renpy.pause(0.5)
    show app2
    scene bg exter
    #show mc econc
    with Fade(0.5,0.0, 1.0)
    
    # neutral
    pause
    
    show mc ehapsc
    et "Well,{w} this is it.{w} This is the place.*"
    #show screen affectionMeter
    e econcedsc "..."
    et eworedsc "Jeez*"
    et "Traffic was super backed up and I'm 15 minutes late*"
    et "I probably reek of sweat after running here from the parking garage*"
    et "And I didn't have time to swing by the apartment and change into something nicer*"
    et eworsc "I hope I'm not too underdressed*"
    et eworedsc "Although considering the price range for this place, I almost definitely am*"
    et "The reservation's under my name too, I hope she was able to get seated*"
    et eworsc "I should probably text her that I'm here.*"
    call warn
    et eneuedsc "Or I could just go meet her.*"
    call timer(5,5,'textTO') from _call_timer_27
    menu:
        "Text her":
            hide screen cd
            et ephonefirmedsc "I'll just shoot her a quick text.*"
            e ephonehapedso "\"Hey Avery! I just got here, I'm excited to meet you!\""
            et ephonesterneusc "No, too enthusiastic*"
            e ephonefirmedso "\"Out front\""
            et ephonesterneursc "Too cold*"
            e ephoneneuedso "\"I just got here, I'm wearing a green jacket :)\""
            et ephonesternsc "Whatever, good enough*"
            et efirmsc "I'll just head inside and find her*"
            jump front
    label textTO:
        et efirmsc "It's fine, I'll just find her inside*"
        jump front
        

label front:
    scene bg front
    show mc eneusc:
        yalign 1.0 
        xalign 0.1
    show h downc 
    with Fade(0.4,0.4,0.4)
    play music_2 [ "<sync music>track1.mp3", "track1.mp3" ] fadein 1.0 loop volume 0.4
    play audio "crowd.mp3" loop volume 0.4 fadein 2.0

    #with Fade(0.5,1.0,0.5)
    pause
    stop music
    et "Wow, fancy. {w}It smells like{w} *sniff*{w} overpriced cologne*" #EMORY LOOKING UP????
    et eneuedsc "It's nice and warm in here, I was freezing my tail off outside.*" #EMORY DOWN SMILE
    e ehaperso "Hi! I have a reservation."
    show mc ehapersc
    h downo "Name?"
    show h downc
    e ehaperso "Emory."
    show mc ehapersc
    h downo "One moment."
    show h downc
    et ehapeursc "Is Avery here yet?*"
    et eneueursc "I don't see a golden retriever anywhere* "
    et efirmeursc "Well, I see one, but that's a guy.*"
    et eneueursc "Maybe she's running late?*"
    et "Maybe there's more seating in the back?*"
    show mc eneuersc
    call warn
    h downo "I have a reservation for Emily"
    show h downc
    show mc eworersc
    call timer(2,2,'correctherTO') from _call_timer_28
    menu: 
        "Correct Her":
            hide screen cd
            e econcerso "Sorry, it should be \"Emory\""
            show h irrc 
            n econcersc "The hostess glances up from her screen disinterestedly, with a look that screams I Would Kill You Right Now If I Didn't Have Rent To Pay{i}"
            show mc eworersc
            h irro  "Ok."
            show h downirrc
            et eworedsc "She's out for blood*"
            show mc esurpersc
            h downirro "Well \"Emory\", we only hold tables for 10 minutes."
            show h downirrc
            jump correctherCONT
    label correctherTO:
        show mc esurpersc
        h downo "We only hold tables for 10 minutes, sir and or ma'am."
        show h downc
    label correctherCONT:
        show mc edisedso
        e "I'm so sorry, I got held back at work and traffic was backed up and I-"
        show mc esurpersc
        h downo "Wait, nevermind. Another guest is already waiting for you." 
        h upo "Follow me to your table."
        show h upc
        et eupsetersc "She's already here?*"

label table:
    hide h 
    hide mc 
    show bg e 
    show mc ehostesstc
    show h tablec behind mc
    show men
    with Fade(0.4,0.4,0.4)
    pause
    h tableo "A waiter will see to you shortly." #EMORY SITTING DOWN LOOKING AT HOSTESS
    show bg a 
    show mc empty
    hide h
    hide men
    n "The hostess trudges back to her station, dragging her feet the whole time"
    et "Where is she? I thought the hostess said she was already here?*" #AVERY EMPTY SEAT
    show bg e
    show men
    et ehaptc "Gosh, I'm so nervous, I can barely sit still*"
    et econctc "I hope she's not upset at me for being late*"
    et eneutc "I wonder what she's gonna be like in person*"
    et "I've texted her a little bit and she seemed super sweet, but meeting someone in person is an entirely different experience*"
    et ehaptc "I wonder if she'll be as kind as she seems. Or as pretty as her pictures"
    et "Maybe she'll be really funny, or charming, or easy going*"
    et "I can't wait to meet her! I can't remember the last time I went on a date*"
    et eneutc "I've never used a dating site before either, so I really am walking into this blind...*"
    et ehaptc "It'll be fine, I'm sure we'll get along great in person*"
    et ewortc "Assuming she even shows up, I don't see her anywhere in here*"

    #AVERY ARRIVES
    hide men 
    show bg a
    n astandneutc "At that moment, a red dog approaches your table" 
    a astandneuto "Sorry, I had to run to the bathroom." 
    et astandneutc "Huh!?{w} Is this the right table?*" 
    a astandneuto "You must be Emory."
    show bg e 
    show men
    e eawkto "That's me! I take it you're Avery?"
    hide men
    show bg a 
    n aneutc "Avery takes a seat across from you"
    a aneuto "Yup."
    et aneutc "So this {u}is{/u} her? She looks nothing like her profile on that website! She's not even a golden retriever!*"
    e "Well, Avery, it's great to meet you!"
    a aneuto "Yeah."
    et aneutc "And that response!? She wasn't nearly this cold over text!*"
    n areachneuedmc "Avery suddenly reaches her arm out, but it is unclear why."
    call warn 
    et "What is she doing? Is she going in for a pawshake? Who shakes paws like that though!?*"
    call timer(2,2,'pawshakeTO') from _call_timer_29
    menu: 
        "Shake her paw":
            hide screen cd
            show bg e 
            hide men
            n eshakeawksweatmc "You reach out to shake her paw. It feels like touching a cadaver."
            et "She has the stiffest grip I have ever felt in my life*"
            e eshakeawksweatmo "I'm so happy to finally meet you in person!"#DRAW pawSHAKE FRAMES???
            show bg a
            a ashakestunmc "...{w} M... "
            extend ashakestunmo "Menu..."
            show bg e 
            e eshakeconfmc "Hm?"
            e eshakeconcmo "Oh, I haven't had a chance to look at the menu yet but I'm sure you'll find something you like!"
            show bg a 
            a ashakestunmo "No-{w} menu-{w} on the table-"
            show bg e 
            et eshakestunmc "Oh Dog, she was reaching for the menu*"
            show men
            e epawsawksweatmo "Oh! I'm sorry, I thought you were going in for a pawshake" 
            hide men
            show bg a 
            a astunedmo "It's fine."
            et astunedmc "It's not too late to leave this date now with your dignity semi-intact*" 
            show bg e 
            show men 
            e eawkto "Why don't we decide on what we're gonna eat?"
            show bg a 
            hide men 
            a aedgeedmo "Yes please, that would be nice."
            show bg e 
            et eworedmc "Get it together Emory, first impressions aren't everything, you can still save this date*"
            e econcmo "You,{w} um,{w} you have nice paws"
            show bg a 
            a auhhmo "Uhh... Thanks?"
            show bg e
            show mc econcedmo
            $ aff -=2
            jump pawshakeCONTINUE
label pawshakeTO:
    n aneuedmc "Avery reaches across the table and grabs one of the menus placed between the two of you"
    show bg e 
    show men
    et econctc "Oh, she was going for the menu! That could have gone much worse*"
    e econcto "I haven't had a chance to look at the menu yet, what looked good to you?"
    show bg a 
    hide men
    a aneuedmo "Oh um, " 
    extend aneumo "it all looked good to me"
    show bg e 
    e ehapmo "I'll just have to give it a look myself then!"
    show mc ehapedmo
label pawshakeCONTINUE:
    e "This place is offering a great deal on their fixed price menu, I'll probably order something from there!"
    et econcsweatermc "It's the only way I could take a girl to a restaurant this nice on my budget*"
    call ordering from _call_ordering #from _call_ordering

    n "The waiter steps away from the table to deliver your order to someone in the back"
    show bg a 
    if(desOrder==1):
        show mc anervedtc
    else:
        show mc aneutc
    n "You and Avery are finally alone at your table"
    call appconvo from _call_appconvo #from _call_appconvo
    if(quick):
        jump demoEnd

    if(appOrder==2): #if you ordered beef tartare
        #DRAW waiter holding beef tartares
        show w tartareo
        w "Here are your two beef tartares. Enjoy."
    else: #if you ordered ceviche or chefs choice
        #DRAW waiter holding ceviche and beef tartare
        show w cevicheo
        w "Here are your ceviche and beef tartare. Enjoy."

    jump demoEnd

label demoEnd:
    if(quick):
        show bg demoEnd0quick 
        hide mc
        with Fade(1,1,1)
        pause(4)
    elif(aff>0):
        show bg demoEnd0good
        hide mc
        hide w
        with Fade(1,1,1)
        pause(4)
    else:
        show bg demoEnd0bad
        hide mc
        hide w
        with Fade(1,1,1)
        pause(4)

    show bg demoEnd1 with Fade(1,1,1,color="#A0699E")
    pause(1)
    show bg demoEnd2 with Dissolve(1)
    pause(4)
    scene bg demoEnd3 with Fade(1,1,1, color="#A0699E")
#Fade(0.5,0.5,0.5, color="#A0699E") 
    pause
    scene black with Fade(1,0,0) 
return


label aloneENDING:
    e "the end"
                #ENDING SLIDE
                #You had Avery's Cheesecake for dessert (You heartless bastard) #IN RESTAURAUNT ALONE
return 
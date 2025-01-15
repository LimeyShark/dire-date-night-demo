label ordering:
    default appOrder=0
    default desOrder=0
    default entOrder=0
    define longer_easein = MoveTransition(2.0, enter=offscreenright, enter_time_warp=_warper.easein)

    show bg a 
    show mc aneuwmc
    show w skepec behind mc
    #with longer_easein
    n "Before you have a chance to read through the menu, the waiter approaches the table, eyeing you up and down with an air of superiority"
    et "Now I kinda feel out of place in my less-than-formal attire*"
    w neuao "I see your companion has finally arrived."
    #show bg e 
    #show w empty
    #show mc estraintc
    show bg a
    show mc aneuwmc
    w neueo "What would the two of you be interested in ordering on this night?"
    show bg e 
    show w empty
    e ehapmo "I think we're both gonna order off the \"prey fee\" menu"
    show bg a 
    #show mc aneuwmc
    show mc aconmc
    w skepeo  "The prix fixe menu?" 
    show bg e 
    show w empty
    e econcsweatflushermo "Yeah, that one."
    show bg a 
    show mc aneuedmc
    w neupo "And which of the appetizers would you like?"
    show bg e 
    show w empty
    call warn
    et esurpmc "Shit, I barely had any time to look at the options!*"
    show mc eneuedmc
    call timer(5,5,'appOrderTO') from _call_timer_24
    menu: 
        "Ceviche":
            hide screen cd
            $ appOrder=1
            e ehapedmo "Can I get the, um, \"shey vi shey\"?"
            show bg a 
            show w skepeurc
            n aneuedmc "The waiter rolls his eyes at your butchered pronunciation of the word" 
            w skeppo "Of course. "
            show mc aneuwmc
            extend neuao "And for you, miss?"
            show w neuac
            a aneuwmo "Could I please have the beef tartare?"
            show mc aneuwmc
            w neupo "Very well. I have here one order of the ceviche and one order of the beef tartare."
            show bg e 
            show w empty
            et ewormc "Is she gonna judge me for my choice of appetizer?*"
            et eworedmc "Maybe I should have gotten the tartare so she would think we have similar taste*"
            jump appOrderCont
        "Beef Tartare":
            hide screen cd
            $ appOrder=2
            e ehapedmo "Can I get the beef tartare?"
            show bg a 
            show mc aneumc
            w skepeo "And you are aware this dish contains raw beef?"
            show bg e 
            show w empty
            et esurpmc "It does??*"
            e estrainmo "Yup, I love it, can't get enough!"
            et estrainmc "I hope I don't get salmonella*"
            show bg a
            show mc aneuwmc
            w skeppo "Very well. " 
            extend neuao "And for you, miss?"
            show w neuac
            a aneuwmo "Could I please have the beef tartare as well?"
            a ahapedwmo "I can't remember the last time I had beef tartare..." 
            show mc ahapwmc
            w neupo "Of course. I have here two orders of the beef tartare."
            show bg e 
            show w empty
            et ewormc "Is she gonna judge me for my choice of appetizer?*"
            et eworedmc "Maybe I should have gotten the ceviche, I hope she doesn't think I picked the tartare just to impress her*"
            jump appOrderCont
    label appOrderTO:
        show bg a 
        show mc aneumc
        w neueo "For your appetizer?"
        show w skepec
        e "..."
        a aconmo "Emory?"
        a "Emory?"
        show bg e
        show w empty
        e econcedmo "Sorry, um, " 
        extend econcmo "either is fine"
        show bg a 
        show mc aconmc
        w skepec "..."
        extend skepeo "I'll just put down 'chef's choice'"
        show bg e 
        show w empty
        e econcmo "Perfect, yeah"
        et ewormc "Is she judging me for taking too long?*"
        et eworedmc "I'm pretty sure a friend once told me women like people who are confident...*"
label appOrderCont:
    et ewormc "Can you ruin a date before you even order?*"
    show bg a 
    show mc aneuedmc
    call warn
    w neupo "And for you entrees?"
    show w neupc
    call timer(5,5,'entOrderTO') from _call_timer_25
    menu:
        "Ribeye Steak":
            hide screen cd
            $ entOrder=1
            show bg e 
            show w empty
            e econcmo "Can I get the ribeye steak?"
            show bg a 
            show w neuac
            a aneuwmo "I'll do the steak too"
            show mc aneuwmc
            w neupo "Two steaks. "
            show mc aneuedmc
            extend neueo "And for dessert?"
            jump entOrderCont
        "Honey Glazed Salmon":
            hide screen cd
            $ entOrder=2
            show bg e 
            show w empty
            e econcmo "Could I try the salmon?"
            show bg a 
            show w neuac
            a aneuwmo "I think I'll do the steak"
            show mc aneuwmc
            w neupo "One salmon one steak."
            show mc aneuedmc
            extend neueo " And for dessert?"
            jump entOrderCont
    label entOrderTO:
        show mc aneumc
        w skepeo "Your choice of entree?"
        show bg e 
        show w empty
        e esurpmo "OH, um,"
        extend econcmo " whatever's good"
        show bg a 
        show w neuac
        a aneuwmo "I think I'll do the steak"
        show mc aneuwmc
        show w skeppo
        if(appOrder==0):
            w "One steak and {i}another{/i} chef's choice"
        else:
            w "One steak and...{w} I'll just put down 'chef's choice'" 
        w neuao "And for dessert?"
label entOrderCont:
    show bg e 
    show w empty
    call warn
    et eworedmc "I really wish I had more time to look at the menu, but I guess it's too late now*"
    #show mc eneuedmc
    call timer(5,5,'desOrderTO') from _call_timer_26
    menu: 
        "Chocolate Lava Cake":
            hide screen cd
            $ desOrder= 1
            e ehapedmo "Ooo, the chocolate lava cake sounds great, I'd love to try it!" 
            show bg a 
            show w neupc
            et astunmc "Hm? Avery looks a bit pale*" 
            et "I hope she's feeling alright*"
            w neuao "And what can I get for you miss?"
            show w neuac
            a astunedmo "Ah- I- um-"
            a "Just the cheesecake."
            show bg e 
            show w empty
            et econfmc "I wonder what's gotten into her?*"
            show bg a 
            show mc astun2edmc
            w neupo "One order of the chocolate lava cake and one order of the cheesecake, then?"
            show w neuec
            e "Yup, perfect!"
            show w neupc
            a "..."
            w neupo "I will return shortly with your appetizers"
            w neuao "I can take your menus."
            w neueo "Enjoy your evening"
            #waiter fade?
            hide w
            show bg e 
            show mc ehaptc
            $ aff -=3 #s-3 or -2? i think -3
            return
        "Cheesecake":
            hide screen cd
            $ desOrder=2
            e ehapedmo "Ooo, the cheesecake sounds great, I'd love to try it!"
            show bg a 
            show w neupc
            a aneuedmo "I guess I'll get the cheesecake too, I don't really have any other choice"
            e aneumc "Hm?"
            a aconmo "I'm a dog? Chocolate would totally mess up my insides."
            show bg e
            show w empty
            et esurpmc "Oh Dog, I didn't even think of that! I sure am glad I picked the cheesecake*"
            et ewormc "Dating a dog might be harder than I thought...*"
            show bg a 
            show mc aneuwmc
            w neupo "Two orders of the cheesecake, then?"
            show w neuec
            e aneumc "Yup, perfect!"
            jump desOrderCont
    label desOrderTO:
        if(appOrder==entOrder==0): #TIMED OUT OF ALL 3
            show bg a 
            show w skepec
            a aconmo "Emory are you feeling alright?" 
            a aconmo "I'm worried about you, you seem to be spacing out a lot"
            show bg e 
            show w empty
            e esurpmo "Wha- oh, um, sorry"
            e econcmo "What did you say?"
            show bg a 
            show w skepec
            a aconmo "Are you sure you don't wanna just go home? We can try again some other night, when you're feeling better"
            show bg e 
            show w empty
            e eslantconcmo "No no, I'm okay, really. I wanna be here with you."
            show mc econcmc
            w "Well then?"
            e econcedmc "..."
            extend econcmo "Sorry, what was the question?"
            show bg a 
            show w skepac
            a aneuwmo "We'll do two orders of the cheesecake"
            show mc aneuwmc
            w neupo "Very well."
            $ aff-=1
        else:
            e eneuedmo "Hmm, I really can't decide." 
            extend ehapmo " Avery, do you have any input?"
            show bg a 
            show w neuec
            a aconmo "The cheesecake. Obviously the cheesecake."
            show bg e
            show w empty
            e econcmo "Oh wow, I didn't realize you were such a big fan of cheesecake!"
            show bg a 
            show w neuec
            a aconmo "I'm not, I would just prefer if you picked the option that {i}wasn't{/i} poisonous to me"
            show bg e
            show w empty
            e esurpmc "OH!" 
            extend econcsweatmo " Right!{w} The whole 'dog' thing"
            show bg a 
            show w neuec
            a aconmo "Yes. The whole 'dog' thing."
            show mc aneuwmc
            w neupo "Two orders of the cheesecake, then?"
            show w neuac
            a aneuwmo "That'll be all"
            $ aff-=1
label desOrderCont:
    show mc aneuwmc
    w neupo "I will return shortly with your appetizers."
    w neuao "I can take your menus."
    w neueo "Enjoy your evening."
    #waiter fade?
    hide w
    show bg e 
    show mc econctc
return 
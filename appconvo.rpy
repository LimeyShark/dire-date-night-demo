label appconvo:
    default st = False
    default cj= False 
    default tay= False 
    default aah= False 
    default pfp=False
    default order=0 

    default quick=False
    show bg e
    show mc ehaptc

    et "Well, here I am!{w} I'm actually on a date! "
    extend eneutc "Now what?*"
    et "What do people talk about on a date? And in what order?*"
    et ewortc "Is it weird if I just start asking her questions after we just met?*"
    call warn
    et edistc "And why does she look nothing like her profile picture on that dating site??*"
    show mc eawktc
label conversation:
    #if():#ADD
    call timer(15,15,'conversationTO') from _call_timer
    menu:
        "Make small talk" if not st:
            $ st=True
            $ order +=1
            hide screen cd
            show mc ehaptc
            if(not(aah or tay)): #GOOD, if you have not askedabouther OR talkedaboutself
                et "You can do this Emory, just break the ice with some small talk!*"
                call warn
                et eawktc "WHAT DO PEOPLE EVEN TALK ABOUT?*"
            else: #Bad
                call warn
                e "Okay, be cool Emory, just butter her up with some small talk"
            call timer(8,8,'smalltalkTO') from _call_timer_1
            menu: 
                "The weather":
                    hide screen cd 
                    if(not(aah or tay)): #good if before asking about her OR talking about self
                        e eawkto "So, um, I heard it was going to rain soon!"
                        show bg a
                        call warn
                        a aneuto "Is it? I'm looking forward to it."
                        show mc aneutc
                        call timer(3,3,'weatherTO') from _call_timer_2
                        menu:
                            "I don't like the rain":
                                hide screen cd
                                show bg e
                                e ehapto "Really? I hate the rain, I can't stand getting wet!"
                                show bg a 
                                a afrusto "Oh, huh."
                                show bg e 
                                et eawktc "Shit I should have held my tongue.*"
                                $ aff-=1
                                jump conversation
                        label weatherTO:
                            hide screen cd
                            a ahapedto "I love listening to the sound of rain falling." #smile
                            a "Especially if I can stay inside all day."
                            show bg e 
                            e eslanthapto "Yeah, I guess it {i}is{/i} pretty peaceful."
                            show mc ehaptc
                            $ aff +=1
                            jump conversation
                    else: #bad
                        e eawkto "So... how about it! The weather, I mean."
                        show bg a 
                        a aneuto "What about it?"
                        show bg e 
                        e eawkto "Sure is, um, dark, out there."
                        show bg a 
                        a aconto "...Yeah. You can really tell by the lack of... um... light..."
                        show bg e 
                        e eawkto "Yeah..."
                        show bg a 
                        a anervtc "..."
                        show bg e 
                        e eawktc "..."
                        e "*{i}AAAAAAAAAAAAAAAAA*"
                        $ aff -=1
                        jump conversation
                "Traffic":
                    hide screen cd
                    if(not(aah or tay)): #good      
                        e eawkto "Wow, that traffic, huh?"
                        show bg a
                        a aneuto "Oh, I took the subway, I wouldn't know"
                        show bg e 
                        e estrainto "Yeah, it was pretty backed up, sorry for showing up late"
                        show bg a 
                        a aneuto "Ah, no worries, I wasn't waiting that long."
                        show bg e 
                        et estraintc  "Great small talk Emory.*"
                        jump conversation
                    else: #bad
                        e eawkto "Wow, that traffic, huh!"
                        show bg a 
                        a aconto "The traffic? Like in general or?"
                        show bg e 
                        e eawkto "No um. Well. I mean. It's pretty backed up right?"
                        e "Or, well, it *{i}was{/i}* pretty backed up. When I got here, I mean. Late."
                        show bg a 
                        a aneuto "I took the subway, so I couldnt say."
                        show bg e 
                        e eawkto "I see."
                        show mc eawktc
                        jump conversation
                "The restaurant":
                    hide screen cd
                    if(not(aah or tay)): #good
                        e ehapto "This place seems pretty cool!{w} I don't really eat at fancy places, so this is a neat experience!"
                        show bg a 
                        call warn
                        a ahapedto "Yeah, I guess so... {w}I'm just excited to try the steak."
                        show bg e 
                        show mc eneutc
                        call timer(2,2,'steaksTO') from _call_timer_3
                        menu:
                            "Dogs like steaks":
                                hide screen cd
                                e ehapto "Haha, you really {i}are{i} a dog!"
                                show bg a 
                                a aconto "What do you mean?"
                                show bg e 
                                e econcto  "You know, you like steaks? Dogs like steaks?"
                                show bg a
                                a askepto  "I guess? I mean not all dogs like steaks, I just happen to enjoy them."
                                show bg e
                                e eawkto "Oh uh, my mistake."
                                et eawktc "DIFFERENT SUBJECT, NOW.*"
                                $ aff-=1
                                jump conversation
                        label steaksTO:
                            et edistc "DONT SAY THAT*"
                            e econcto "Steaks sure are wonderful..."
                            et econctc "That's so typical of a dog, but im glad im learning about her likes*"
                            $ aff+=1
                            jump conversation
                    else: #bad
                        e ehapto "So this place is pretty neato, don't you think? I haven't really been to many fancy restaurants"
                        show bg a 
                        a aconto "Yeah it sure is, um... neato? I'm just looking forward to my food."
                        show bg e 
                        e eawkto "Oh uh, yeah, me too."
                        et eawktc "'Neato'!? Who in the past decade has said the word 'Neato'??*"
                        $ aff -=1
                        jump conversation
                "Dogs":
                    hide screen cd
                    if(not(aah or tay)): #good
                        e ehapto "So... Dogs, huh!"
                        show bg a 
                        call warn
                        a aconto "What about them?"
                        show bg e 
                        show mc econctc
                        call timer(5, 5, 'elaborateTO') from _call_timer_4
                        menu:
                            "Elaborate":
                                hide screen cd
                                e econcto "So um, you're a dog, what's that like!"
                                show bg a 
                                a aconto "Fine, I guess?"
                                call warn
                                et acontc "Don't ask if the toilet thing is real.*"
                                call timer(2, 2, 'toiletTO') from _call_timer_5
                                menu: 
                                    "Ask if the toilet thing is real":
                                        hide screen cd
                                        show bg e
                                        e ehapto "Is the toilet thing real?"
                                        show bg a 
                                        a aconto "What?"
                                        show bg e 
                                        e ehapto "Do you guys actually drink from the toilets or is that a myth?"
                                        show bg a 
                                        n astunflushtc "Avery's face flushes more red than it already is, she seems too stunned to speak"
                                        show bg e
                                        et edistc "WHY DID YOU ASK IF THE TOILET THING IS REAL*"
                                        $ aff-=3
                                        jump conversation
                                label toiletTO:
                                    show bg e
                                    e estrainto "That's cool... That's cool..."
                                    show mc estraintc
                                    $ aff-=1
                                    jump conversation
                        label elaborateTO:
                            e econcto "Nothing, they're just neat, is all..."
                            show mc econctc
                            jump conversation
                    else: #bad
                        e estrainto "So... dogs, am I right?"
                        show bg a 
                        a aconto "What do you mean? What about Dogs?"
                        show bg e 
                        e estrainto "Dogs are cool! Their tails wag! And they do that thing with toilets!"
                        show bg a 
                        a aconto "Your tail wags too. And what thing?"
                        show bg e 
                        call warn
                        e estraintc "*This is already going poorly. Do. Not. Mention. The toilet thing*"
                        call timer(5,5, 'toilet2TO') from _call_timer_6
                        menu:
                            "Mention the toilet thing":
                                hide screen cd 
                                e eawkto "You know, you guys sometimes refresh yourself... with uh... toilet water?"
                                show bg a 
                                a askepto "Toilet water? Like water from a toilet?"
                                a "You do realize we have sinks too?"
                                show bg e 
                                e edisto "Oh.{w} Right.{w} Of course.{w} Sorry."
                                et edistc "If I go to the bathroom and bash my skull in the wall now maybe I can still save this date.*"
                                et estraintc "Or I could try just talking to her.*"
                                et "Why does talking to her have to be so much harder than the alternative.*"
                                $ aff-=3
                                jump conversation
                        label toilet2TO:
                            e estrainto "Oh um, it's nothing, just something I heard once"
                            et estraintc "TALK ABOUT SOMETHING, ANYTHING ELSE*"
                            $ aff-=1
                            jump conversation
            label smalltalkTO:
                show bg a 
                a anervto "So...{w} um...{w} do you like...{w} food?"
                show bg e 
                et ewortc "Oh Dog, it looks like she had the same idea to make small talk*"
                e econcto "Um, yeah, I like food"
                show bg a 
                a anervto "Me too."
                show bg e 
                e econcto "That's cool."
                show bg a 
                a anervtc "..."
                show bg e 
                e estrainto "Do... you... have a favorite food?"
                show bg a
                a anervflushtc  "{size=30}... "
                extend anervflushto "meat...{/size}"
                show bg e 
                e estrainto "Sorry? I didn't catch that"
                show bg a 
                a anervflushto "meat..."
                show bg e 
                e estrainto "Oh, meat! I like meat too!"
                show bg a 
                a anervflushto "Yeah."
                show bg e 
                et estraintc "This is the worst small talk I have ever made in my life, no more small talk*"
                jump conversation 

        "Talk about yourself" if not tay: #good if comes after aah
            $ tay = True
            $ order +=1
            hide screen cd
            if(aah): #GOOD
                show bg a 
                a aneuto "Well what about you?" 
                show bg e 
                e econfto "What about me?" #Camera only on Emory??
                a econftc "Tell me about yourself"
                e econfto "What do you want to know?"
                call warn
                a econftc "Anything"
            else: #BAD
                et ewortc "Emory if you don't break this silence right now you will never be able to talk to a girl ever again in your life*"
                et edistc "Then you'll never find love and you'll grow old and die alone and in 100 years no one will remember your name*"
                et ewortc "That got too dark I don't want that to happen*"
                call warn
                et eslantwortc "Just talk about yourself, it's better than nothing.*"
            call timer(8,8,'tayTO') from _call_timer_7
            menu:
                "Talk about work":
                    hide screen cd 
                    if(aah):#GOOD
                        e ehapto "Well I work part time as a barista on weekends"
                        show bg a 
                        a ainterto "Oh? I've always wanted to work at a coffee shop, it sounds peaceful, and I love the smell"
                        show bg e
                        e econcto "Believe me, it's anything but peaceful. You wouldn't {i}believe{/i} the customers I see"
                        show bg a 
                        a aconto "I wouldn't?"
                        show bg e
                        e eneuto "Well for starters, the so called \"coffee\" is more creamer, food coloring, and high fructose corn syrup than actual coffee."
                        e eneuerto "And then we occasionally get these old people that come in every day and order a black coffee"
                        e eneuedto "And every time I ask for the size they ask for \"NORMAL\" without fail, like they're being rebellious or something"
                        e eneuto "It's a whole song and dance"
                        show bg a 
                        a aconto "What are they singing?"
                        show bg e 
                        e eslantconcto "No, um, it's a figure of speech. I meant they always make a huge scene.{w} They're probably just lonely cause their grandkids don't call them"
                        show bg a 
                        a aneuedto "Oh, I see. That sounds rough."
                        show bg e 
                        e econcto "Eh, work is work"
                        show bg a 
                        a aneuedrto "Work is work..."
                        show bg e 
                        e eslanthapto "You were right about the smell though, some of my coworkers can't stand it but I don't think I'll ever get sick of the smell of coffee"
                        show bg a 
                        a ahapto "Me neither"
                        show bg e 
                        show mc ehaptc
                        $ aff +=2
                        jump conversation
                    else: #BAD
                        e econcto "I work as a barista part time and I only get to eat at nice places like this on special occasions, so this is a bit of a treat"
                        show bg a
                        n aexcitedtc "Avery's ears perk up a bit at the last word"
                        a aexcitedto "Treat? "
                        extend anervfrusedrto "Sorry- I mean- "
                        extend asurphapto "you work as a barista?"
                        show bg e
                        e ehapto "Yeah, on weekends. Not the most fun, but it pays for meals like this one."
                        show bg a 
                        a ahapto "What's it like?"
                        show bg e
                        e ehapto "The morning rush is always tough, but after that it's not too bad"
                        e econcto "I mostly work on register so I have to talk to the customers, which can be pretty exhausting"
                        e eslanthapto "But if I'm on with coworkers I like, it's not too bad"
                        show bg a
                        a ahapedto "That sounds nice, better than my gig..."
                        show bg e
                        e econcto "Well, if you're ever considering a change in career, I'm happy to put in a good word for you at our shop"
                        show bg a
                        a ahapto "Hah, I'm not sure if they'd hire me, but thanks anyways."
                        show bg e 
                        show mc ehaptc
                        $ aff+=1
                        jump conversation
                "Talk about school":
                    hide screen cd
                    if(aah): #good
                        e ehapto "Well, I'm currently in school and I work part time"
                        show bg a 
                        a ainterto "Oh? What are you in school for?"
                        show bg e
                        e eneuedto "Civil Engineering. I'm not super passionate about it, but it pays pretty decent and people will always need engineers, so that's nice"
                        show bg a 
                        a aneuto "I see. I doubt I could really grasp any of that stuff, it's all too confusing."
                        show bg e
                        e eslantconcto "Yeah, it can be pretty rough. I'm passing my classes but to be honest, I don't think I've gotten more than 6 hours since,{w} well,{w} since I started school"
                        show bg a
                        call warn
                        a aneuedto "That sounds tiring..."
                        show bg e 
                        show mc eneutc
                        call timer(5,5,'grossStoryTO') from _call_timer_8
                        menu:
                            "Tell a gross story":
                                hide screen cd
                                e econcto "The professors don't make it any easier, either"
                                e ehapto "I had this one professor, super awkward guy, entirely bald. During lectures he would just...{w} {i}slurp{/i} on rock candy the whole time."
                                e "And cause it's a huge class he has a microphone and it picks up all his slurping"
                                show bg a 
                                a aconcto "Ewww"
                                show bg e 
                                e eslantconcto "I don't think anyone had the heart to tell him how gross and offputting it is, as far as I know he's still slurping to this day"
                                show bg a 
                                a aconcto "Oh my Dog that's gross, don't tell me that when I'm about to eat"
                                show bg e
                                e eslantconcto "Sorry, sorry, no more gross stories" #happy
                                show mc ehaptc
                                $ aff +=3
                                jump conversation
                        label grossStoryTO:
                            e ehapto "It can be. Truth is, I've wanted to go into aerospace engineering since I was a kitten"
                            e econcedto "But I don't think I've got what it takes to cut it in aerospace engineering, so I'll settle for civil"
                            show bg a 
                            a ahapedto "Well, you seem pretty smart to me. But what do I know..."
                            show bg e
                            e econcto "Thanks, that's kind of you to say"
                            show bg a
                            a ahapedto "No problem"
                            show bg e 
                            show mc ehaptc
                            $ aff +=1
                            jump conversation
                    else: #BAD
                        e econcto "Sorry again about being late, classes ran late and I didn't have time to change into something nicer. I'm in school for civil engineering."
                        show bg a 
                        a ainterto "Oh? What does a civil engineer do?"
                        show bg e
                        e econcto "Uh, y'know, like bridges and stuff."
                        show bg a 
                        a aconto "Bridges and stuff?"
                        show bg e 
                        e ehapto "Yeah, bridges, roads, tunnels, all that kinda stuff"
                        a ehaptc "Ah, I see. I didn't realize I was on a date with an honor student"
                        e econcto "Oh, you're not in school?"
                        call warn
                        a econctc "No."
                        call timer(5,5,'notinschoolTO') from _call_timer_9
                        menu:
                            "No, you're {u}not{/u} in school?":
                                hide screen cd 
                                e econcto "No, you're not in school?"
                                show bg a
                                a afrusedto "Yes, correct, I'm not in school."
                                a aconto "Don't get me wrong, I want to be, I just can't really afford it."
                                show bg e
                                e eworto "Oh. I'm sorry to hear that."
                                show bg a
                                a afrusto  "Don't be. I'm working and saving up now to send myself to school in a year or two"
                                show bg e 
                                e econcto "Wow, that's really impressive! I wish you the best with that!"
                                a econctc "Thanks."
                                et "That's a good note to end this discussion on, let's talk about something else before I ruin the mood again*"
                                jump conversation
                            "No, you {u}are{/u} in school?":
                                hide screen cd
                                e econcto "No, you {i}are{/i} in school?"
                                show bg a
                                a afrusto "No, I'm {i}not{/i} in school"
                                $ aff-=1
                                jump notinschoolTO
                        label notinschoolTO:
                            show bg e 
                            e estrainto "Ah, I see"
                            et estraintc "Great, now she thinks I'm showing off*"
                            et "I think I'll just digging myself into a hole if I keep talking, we gotta talk about something else*"
                            $ aff-=1
                            jump conversation
                "Talk about hobbies":
                    hide screen cd
                    et ehaptc "Maybe we'll have some hobbies in common!*"
                    call warn
                    et ewortc "What sorta stuff would she be into though?*"
                    call timer(8,8,'hobbiesTO') from _call_timer_10
                    menu:
                        "Fangs and Folklore":
                            hide screen cd
                            if(aah): #good
                                e ehapto "Well, on weekends I meet up with a couple friends and play Fangs and Folklore"
                                show bg a 
                                a aconto "Fangs and Folklore?"
                                show bg e 
                                e eexcitedto "Wait- don't tell me you've never heard of Fangs and Folklore!"
                                show bg a 
                                call warn
                                a aconto "I don't know what that is."
                                show mc acontc
                                call timer(5,5,'fangsandfolkloreTO') from _call_timer_11
                                menu:
                                    "Elaborate":
                                        hide screen cd
                                        show bg e 
                                        e ehapto "Okay so basically Fangs and Folklore is this fantasy tabletop roleplaying game, where you and your friends make these characters that you play as{nw}"
                                        e ehapedto "and you can make your character pretty much whatever you want which I think is pretty cool, and there are a bunch of different classes and races for{nw}"
                                        e ehaperto "you to pick for your character and you can customize their gear and their stats and their abilities and stuff, and then once you've all made your characters one{nw}"
                                        e ehapto "of you has to be the Domain Master who basically comes up with a story for the adventure you and your friends to go on and they improv a lot of what{nw}"
                                        e ehapedto "happens so you can get really creative and it requires a lot of imagination and pretty much everything is determined by dice rolls which are dependent on a{nw}" 
                                        e ehapto  "player's proficiency in the skill and-{nw}"
                                        et estuntc "OH DOG, how long have I been talking for?*"
                                        show bg e
                                        e econcto "Sorry I'm rambling I-"
                                        show bg a 
                                        a aadmireto "That sounds really cool!" 
                                        a asurphapto "I love the idea of being able to be whoever I want"
                                        show bg e
                                        et esurptc "She was listening?*"
                                        call warn
                                        e ehapto "It is! The best part has got to be the customizability! You can be and do pretty much anything you can imagine, like for instance..."
                                        show mc ehapedtc
                                        call timer(5,5,'characterTO') from _call_timer_12
                                        menu:
                                            "Talk about your half dragon fighter":
                                                hide screen cd
                                                e ehapto "I have this fight that's half goblin and half dragon, so my friends use him as a little flamethrower"
                                                e "His name is Gorbstaggler and all of his points are in esoteric magic, so he just dishes out damage"
                                                show bg a 
                                                a ahapto "That sounds like a lot of fun"
                                                show bg e
                                                e ehapto "It really is! If you'd like, you're welcome to join us some time"
                                                show bg a
                                                a aavoidedrto "I've never really been invited to a group activity..."
                                                show bg e
                                                e ehapto "Oh you'd get along swell with my friends, they're all mega-nerds"
                                                show bg a 
                                                a aconcto "Maybe someday."
                                                show bg e 
                                                e eslanthapto "Well, we'd love to have you"
                                                et eslanthaptc "Who would have thought she was as much of a nerd as I am*"
                                                show mc ehaptc
                                                $ aff+=2
                                                jump conversation
                                            "Talk about your wild form druid":
                                                hide screen cd
                                                e ehapto "I have this druid character who is normally an elf, kinda just a weak little twig"
                                                e "But when she loses half her health she transforms into this monstrous werewolf, and she tear through entire battles alone-"
                                                show bg a
                                                n astuntc  "Avery's eyes widen, growing pale as all the color is drained from her fluffy cheeks" 
                                                a astunerto "I-{w} in- {w}interesting-"
                                                show bg e
                                                e econcto "Hey are you okay? Did I ramble too much?"
                                                et econctc "Maybe she has a fear of werewolves?{w} Or elves?*"
                                                show bg a 
                                                a anervto "N- no, the games sounds- um- fun-"
                                                show bg e
                                                e econcto "Oh! Well, I'd love to have you over sometime to play with me and my friends"
                                                show bg a 
                                                a atenseedrto "That sounds nice..."
                                                show bg e 
                                                et econftc "She seems to have calmed down, I wonder what got into her?*"
                                                et econctc "It's probably best if I don't keep talking about this*"
                                                $ aff+=2
                                                jump conversation
                                        label characterTO:
                                            e econcerto "I um... actually I prefer to be in charge, I'm usually the Domain Monarch"
                                            et econcertc "Talking about my own characters feels so vulnerable, I don't think I can share something that personal with a near-total stranger...*"
                                            show bg a 
                                            a aconto "That doesn't sound like much fun"
                                            show bg e
                                            e estrainto "It can be! If you're good at it. Which I'm not."
                                            a estraintc "Oh. Alright."
                                            et "She seemed interested, but I guess not anymore*"
                                            jump conversation
                                label fangsandfolkloreTO:
                                    show bg e
                                    e eslantconcto "Ah, um, it's just this old game I used to play."
                                    show bg a 
                                    a ainterto "Oh?"
                                    show bg e 
                                    e econcedto "It's for kids, I've outgrown it"
                                    show bg a 
                                    a aneuedto "Oh um, alright then..."
                                    show bg e 
                                    et eawktc "Crap, did she actually want to hear about it?*"
                                    $ aff-=1
                                    jump conversation
                            else: #bad
                                e econcto "Sorry, this is a bit of a weird ask, but... uh... do you like Fangs and Folklore?"
                                show bg a 
                                a aneuto "Um, no. What's Fangs and Folklore?"
                                show bg e 
                                e eexcitedto "\"What's Fangs and Folklore\"?? Have you been living under a rock your entire life? It's only the greatest board game ever created!"
                                show bg a 
                                a aconto "I don't think I would fit under a rock."
                                show bg e 
                                e econfto "What? "
                                extend ehapto "Nevermind, doesn't matter."
                                e ehapto  "So basically Fangs and Folklore is this fantasy tabletop roleplaying game, where you and your friends make these characters{nw}"
                                e ehapto "and you can make your character pretty much whatever you want which I think is pretty cool, and there are a bunch of different classes and races for{nw}"
                                e ehapedto "you to pick for your character and you can customize their gear and their stats and their abilities and stuff, and then once you've all made your characters one{nw}"
                                e ehaperto "of you has to be the Domain Master who basically comes up with a story for the adventure you and your friends to go on and they improv a lot of what{nw}"
                                e ehapedto "happens so you can get really creative and it requires a lot of imagination and pretty much everything is determined by dice rolls which are dependent on a{nw}" 
                                e ehapto "player's proficiency in the skill and-"
                                show bg a 
                                n afrusedtc "Avery is looking down at the floor, awkwardly shifting in her seat"
                                show bg e 
                                e eworto "Oh Dog, I'm sorry, I got carried away talking-"
                                show bg a 
                                a afrusedto "It- it's fine."
                                show bg e
                                et edistc "C'mon Emory, you should know by now not to ramble about your interests with new people, it just comes off as weird*"
                                et ewortc "I don't think she wants to hear about Fangs and Folklore anymore...*"
                                $ aff-=2
                                jump conversation
                        "Critter Quest":
                            hide screen cd 
                            if(aah): #good
                                e ehapedto "Well, I've been obsessed with the Critter Quest franchise for as long as I can remember"
                                show bg a 
                                a asurpto "Oh, Critter Quest! I watched a couple episodes of the show when I was a pup"
                                show bg e 
                                e ehapto "Really? No way, oh my Dog, did you play the card game at all?"
                                show bg a 
                                a ahapedto "No, but whenever my aunt would come visit my cousin would let me play the video game on his console"
                                show bg e 
                                e ehapto "Ooo, I really love the games, they were actually my intro to the franchise and from there I came to appreciate the card game!"
                                e ehaperto "Between the ages of 10-14 Critter Quest was basically my entire personality, I spent all my times playing the games or watching the shows or drawing Critters"
                                e ehapedto "I used to fall asleep hoping that I would wake up as a Critter, like in that one game, and I would always be a little bit disappointed waking up in my usual body..."
                                e eslantconcto "Sorry, that's kind of embarrassing to admit on a first date-"
                                show bg a 
                                a ahapto "No, it's cute. I like seeing you talk about something passionately"
                                if(aff>0): #if date is going well
                                    a ahapedto "I'm envious, really. I've never really had something I cared about as much as you care about Critter Quest."
                                    show bg e 
                                    e eflushedto "Oh.{w} Well, I'm always happy to share the things I love with other people, if you ever want to try getting into it"
                                    show bg a 
                                    a aconcto "I think I would like that"
                                    show bg e 
                                    et ehaptc "Huh, I didn't know she had this side to her. I wonder what else I don't know about her*"
                                    $ aff+=2
                                else: #otherwise
                                    show bg e
                                    e ehapto "Oh, well thank you for listening, I like talking about my passions!"
                                    show bg a 
                                    a ahapto  "Any time."
                                    show bg e 
                                    et eflushedtc "She can be pretty cute, huh*"
                                    show mc ehaptc
                                    $ aff+=1
                                jump conversation
                            else: #bad
                                e econcto "Do you, by any chance, know of Critter Quest?" 
                                show bg a 
                                a aneueurto "Oh gosh, that brings back memories. I haven't played Critter Quest since I was a pup"
                                show bg e 
                                e ehapto  "Really, no way! What's your favorite Critter? Mine's lupinite, I love its wolf form!"
                                show bg a 
                                a aneuedto "I can barely remember most of them"
                                a aneuto "I guess I would have to say um... florabella?"
                                show bg e 
                                call warn
                                et econctc "Florabella? She really is a casual*"
                                call timer(5,5,'analyzeTO') from _call_timer_13
                                menu:
                                    "Analyze her choice":
                                        hide screen cd
                                        e ehapto "Really? Its stats are so lame, and it can't really learn any cool moves, kinda just a bad pick. Why do you like them?"
                                        show bg a 
                                        a afrusedto "I just thought it was pretty, I wanted to look like that"
                                        show bg e 
                                        e estrainto "Oh, um, yeah I guess that's a fine reason to like florabella"
                                        et estraintc "Of course she doesn't care about stats, why would she? Now she probably thinks you're an insensitive prick...*"
                                        et "She seems kind of upset, I should change the subject*"
                                        $ aff-=2
                                        jump conversation
                                label analyzeTO:
                                    e econcto "Oh! Florabella! Yeah I love Florabella"
                                    et econctc "Its stats are lame and it can't really learn any cool moves, it's kinda just a bad pick...*"
                                    e econcto  "What do you like about Florabella?"
                                    show bg a
                                    a ahapedto "I think she's pretty, when I was little I wanted to look like her"
                                    show bg e
                                    e ehapto "Aww, that's sweet"
                                    show bg a 
                                    et anervflushtc "Is she blushing?*"
                                    et "I guess if it makes her happy, she can like whatever Critter she wants*"
                                    show bg e 
                                    show mc ehaptc
                                    $ aff+=1
                                    jump conversation
                        "Singing in private":
                            hide screen cd 
                            if(aah): #good
                                e ehapto "Well, when I'm alone I like to sing to myself, especially in the shower"
                                show bg a 
                                a asurpto "Really? I didn't take you for a singer"
                                show bg e
                                e econcto "Oh I'm not, I have a horrendous voice, I do it because it's fun"
                                show bg a 
                                a aconto "Really? It's fun even though you're not good at it?"
                                show bg e
                                e aconto "It's fun to be bad at stuff sometimes! And it makes me happy!"
                                show bg a 
                                a aneuedto "Huh. I guess so"
                                show bg e 
                                e ehapto "You should try it some time too!"
                                show bg a 
                                a aconcto "I think I'll pass..."
                                show bg e
                                show mc ehaptc
                                $ aff +=1
                                jump conversation
                            else: #bad
                                e ehapto "I sing in the shower."
                                show bg a 
                                a aconto "What?"
                                show bg e 
                                e eawkto "What"
                                show bg a 
                                show mc 
                                a aconto "What did you say"
                                show bg e 
                                e eawkto "I said \"I sing in the shower\""
                                show bg a 
                                a aconto "Why did you tell me that?"
                                show bg e 
                                e eawkto "To make conversation"
                                show bg a 
                                a aneuto "Oh. I don't sing in the shower."
                                show bg e
                                e eawkto "That's cool"
                                show bg a 
                                a aconto "I guess?"
                                show bg e 
                                et eawktc "Okay no more talking about myself*"
                                $ aff-=1
                                jump conversation
                    label hobbiesTO:
                        if(aah): #good
                            e eawkto "Um,{w} well,{w} hmmm,{w} no not that..."
                            e ehapto "Oh!{w} I can't solve a Rubik's cube!"
                            show bg a 
                            a aconto "Okay? I mean, I guess that's interesting, but it doesn't really tell me anything about you."
                            show bg e 
                            e eawkto "Oh, um, sorry. I can't really think of anything else..."
                            show bg a 
                            a afrusto "It's fine. Why don't we just move on?"
                            show bg e 
                            e eawkto "Ah. Of course."
                            $ aff-=2
                            jump conversation
                        else: #bad
                            et ewortc "What kind of stuff does she even like!? Dog, I don't know...*"
                            et edistc "You're taking too long Emory, just pick something harmless to talk about*"
                            e eawkto "Hey Avery! So um- did you- um-"
                            e "Did you know I can't solve a Rubik's cube!"
                            et eawktc "That's your definition of harmless??*"
                            show bg a 
                            a aneuto  "No, no I did not. I do now, I guess."
                            show bg e 
                            et eawktc "I don't think I'm very good at talking about myself, let's not try that again.*"
                            $ aff-=1
                            jump conversation
                "Talk about dating history":
                    hide screen cd 
                    if(aah): #good 
                        e ehapto "Well, this is the second date I've ever been on"
                        show bg a 
                        a aneuedrto "That's one more than me"
                        show bg e
                        e eexcitedto "Really? Then I'm happy to be your first!"
                        show bg a 
                        a aneuto "Thank you."
                        a aneuedtc "..."
                        a aneuto "What was your other date like?"
                        show bg e 
                        e ehapedto "Well, Cookie and I got together after that date, and stayed together for 2 years, so I would say it went well"
                        show bg a 
                        a asurpto "That long? How did it go?"
                        a aneuedrto "I mean obviously it didn't work out, if you're here now, but like, "
                        call warn
                        extend aneuto "what was it like?"
                        show bg e 
                        show mc eneutc
                        call timer(5,5,'datinghistorygoodTO') from _call_timer_14
                        menu:
                            "Talk about the good times":
                                hide screen cd
                                e ehapto "It was good! It was nice having someone to rely on, someone I knew was always in my corner"
                                e econcto "I mean, at least until she wasn't. But up until then, it was fun"
                                show bg a 
                                a aconto "Fun?"
                                show bg e
                                e ehapto "Yeah! We would always spend our weekends together, watching stuff or eating together or going out. We were both cats so we had plenty in common."
                                e ehapedto "We loved going to the aquarium together and looking at all the fish."
                                e "We would spend hours watching them swim around without even realizing the day was slipping by."
                                show bg a 
                                a aneuto "Oh. Well, I hope I can be 'fun' enough for you too"
                                show bg e
                                e econcto "I'm having fun thus far, I wouldn't be worried if I were you"
                                if(aff<0): #if date isn't going well
                                    et econctc "Not entirely true, but I'm hoping she'll open up a bit more once we start to click*"
                                show bg a 
                                a aflushedto "That's reassuring to hear, thank you."
                                show bg e 
                                e eslanthapto "Any time!"
                                $ aff+=1
                                jump conversation
                            "Talk about the bad times":
                                hide screen cd
                                show mc 
                                e econcto "It wasn't great. I mean, don't get me wrong, I have some good memories of her, but they're all stained by the memory of our breakup"
                                show bg a 
                                a aconto "Was it that bad?"
                                show bg e 
                                e econcedto "We were getting dinner together on the weekend like normal, nothing out of the ordinary, and then out of nowhere she says she thinks we should see other cats"
                                e eworedto "One week later she's back with some old flame and I'm glued to the couch downing ice cream by the pint and bawling my eyes out"
                                if(aff>0): #if date is going well
                                    e eplayto "Jokes on her though, I stole that ice cream from her apartment when I was moving out, so in a way it was revenge gluttony"
                                    show bg a
                                    a asurpto "Really!?"
                                    show bg e 
                                    e ehapto "Really, I was mad and I was petty and it was my way of getting back at her for breaking up with me with zero notice"
                                    show bg a 
                                    a ahapto "Well, if we end up together, I'll be sure to keep my freezer locked up before dumping you"
                                    show bg e
                                    et esurptc "Was that a joke? Did she just tell a joke?*"
                                    et econctc "I didn't know she was capable of that*"
                                    e ehapto "Let's not get ahead of ourselves, we gotta see how this date goes"
                                    show bg a 
                                    a ahapedto "Of course, of course"
                                    show bg e
                                    show mc ehaptc 
                                    $ aff+=1
                                    jump conversation
                                else: #if date isn't going well
                                    show bg a
                                    a aconedrto "Oh. Um. I'm sorry that happened."
                                    show bg e
                                    e eslantconcto "Don't sweat it, it was a while back, I'm over her now."
                                    a eslantconctc "Ah, I see."
                                    et estraintc "Maybe I shouldn't have started talking about my shitty ex on my first date with this girl...*"
                                    $ aff=-1
                                    jump conversation
                        label datinghistorygoodTO:
                            e ehapto "It was. And now it's over. I'm here now, with you, that's what matters"
                            show bg a 
                            a ahapto "I'm glad to hear it." 
                            show bg e 
                            show mc ehaptc
                            $ aff +=1
                            jump conversation
                    else: #BAD
                        e econcto "I apologize if I'm a bit rusty at this, I haven't been on a date in years."
                        show bg a 
                        a ainterto "Oh?"
                        show bg e 
                        e estrainto "N-Not cause I'm lonely, I was just in a pretty long relationship before this one"
                        show bg a 
                        a aneuto "Ah, I see. Were you two serious?"
                        show bg e 
                        call warn
                        e econcerto "Yeah. Cookie was..."
                        show mc econcertc
                        call timer(5,5,'datinghistorybadTO') from _call_timer_15
                        menu:
                            "Talk about the good times":
                                hide screen cd
                                e econcedto "She was everything. She meant the world to me, and at the time, I couldn't imagine life without her."
                                e "She was smart, funny, kind, really everything you could ask for in a partner."
                                e econcto "We used to take these long romantic walks on the beach, just the two of us watching the sunset together. "
                                e "Then we'd get dinner together and talk the night away. She really was great-"
                                show bg a
                                n afrusedtc "Avery is looking down at the floor, awkwardly shifting in her seat"
                                show bg e
                                et ewortc  "Oh Dog, I got carried away reminiscing about Cookie*"
                                e eworto "Shit, I'm sorry, I-"
                                show bg a 
                                a afrusedrto "It's fine. Let's just get this date over with."
                                show bg e
                                et edistc "Oh Dog, I really messed up*"
                                $ aff-=3
                                jump conversation
                            "Talk about the bad times":
                                hide screen cd
                                e econcto "She was the worst. She was mean and judgemental and controlling. No joke, a week after she kicked me to the curb, she was back with her ex"
                                e eworedto "Almost two years down the drain just to leave me for some prick named 'Spike'. Like really, 'Spike'? How generic do you have to be to even name your child spike, who picks up their child and looks at them in their pretty " #newly born eyes and thinks,, durrr im going to name you Spike! Generic ass name, and then..."
                                e eworto "Y'know, she broke up with me entirely out of nowhere" 
                                e edisedto "We were getting dinner together like we would every Saturday and then out of nowhere it's 'I think we should see other cats' and 'We lost our spark'"
                                e edisto "I still can't believe her-"
                                show bg a 
                                n afrusedtc "Avery is looking down at the floor, awkwardly shifting in her seat"
                                show bg e 
                                et ewortc "Oh Dog, I got too upset thinking about Cookie*"
                                e eworto "Shit, I'm sorry, I-"
                                show bg a 
                                a afrusedrto "It's fine.{w} Let's just get this date over with."
                                show bg e
                                et edistc "Oh Dog, I really messed up*"
                                $ aff-=4
                                jump conversation
                        label datinghistorybadTO:
                            e econcto "She was nice, but it didn't work out."
                            e econcto "I don't want to talk about her. I'm not on a date with her, I'm on a date with you"
                            show bg a 
                            a aneuto "Alright then."
                            show bg e 
                            et econctc "It's probably for the best that I don't unearth those memories right now.*"
                            jump conversation
            label tayTO:
                if(aah): #good
                    e ehapto "Well,{w} um,{w} I'm Emory!"
                    show bg a 
                    a aneuto "I know that already."
                    show bg e 
                    e eneuto  "Oh, yeah. Right."
                    e ehapto "Did you know pineapples eat you while you eat them?"
                    show bg a 
                    a aconto "What?"
                    show bg e
                    e ehapto "Bromelain! It's an enzyme that eats flesh, and it's found in pineapples"
                    e "Pineapples eat you while you eat them!"
                    show bg a 
                    a aconto "That still doesn't tell me anything about you"
                    show bg e
                    e eworto "Oh, um. That's kind of all I got."
                    et edistc "Dog damnit, what's wrong with me*"
                    $ aff-=1
                    jump conversation
                else: #bad
                    e eawkto "Hello! Um, I'm Emory"
                    show bg a 
                    a aneuto "I already know your name, Emory"
                    show bg e 
                    e eneuto "Oh, yeah. Right."
                    show bg e 
                    e ehapto "Did you know pineapples eat you while you eat them?"
                    show bg a 
                    a aconto "What?"
                    show bg e
                    e ehapto "Bromelain! It's an enzyme that eats flesh, and it's found in pineapples"
                    e ehapto "Pineapples eat you while you eat them!"
                    show bg a 
                    a aconto "Um, cool fact, I guess?"
                    show bg e 
                    e estrainto "Oh, um, no problem."
                    et estraintc "Dog damnit, what's wrong with me*"
                    $ aff-=1
                    jump conversation
        "Ask about her" if not aah: #good if not first thing you do
            $ aah=True
            $ order +=1
            hide screen cd
            e ehapto "Why don't you tell me a bit about yourself?"
            show bg a 
            a aavoidedrto "Oh, um, I don't know..."
            call warn
            a aconto "Like what?"
            show bg e
            show mc eneutc
            call timer(8,8,'aahTO') from _call_timer_16
            menu: 
                "Ask about snowboarding":
                    hide screen cd
                    et ehaptc "Her profile said she liked snowboarding, that'll be good to talk about*"
                    e ehapto "So... you like snowboarding, that must be exciting!"
                    show bg a 
                    a aconto "What? Snowboarding?"
                    call warn
                    a "I have never gone snowboarding in my life"
                    show bg e 
                    show mc ewortc
                    call timer(5,5,'datingprofileTO') from _call_timer_17
                    menu:
                        "Bring up dating profile":
                            hide screen cd
                            $ pfp=True
                            e econfto "You've never been? Your dating profile claims you're a 'voracious snowboarder'"
                            show bg a 
                            a aconto "That's not what that word means"
                            show bg e
                            et ewortc  "I thought it was a cool word...*"
                            e eworto  "Aren't you the one who wrote it?"
                            show bg a 
                            a aconto "No I-"
                            n astuntc "Avery goes pale"
                            a astunflushto "Oh Dog, that was my friend, "
                            extend astunflushedto "she's the one that pressured me to go on this stupid date in the first place." 
                            show mc astunflushcryedto
                            if(order>1):
                                call warn
                            a "I let her make my profile for me, I should have {i}known{/i} she would do something like this, Dog I'm so stupid." 
                            if(order>1): 
                                show mc astunflushcryedtc
                                call timer(5,5,'comfortTO') from _call_timer_18
                                menu:
                                    "Comfort her":
                                        hide screen cd
                                        show bg e
                                        e econcto "Well, you're here now!"
                                        e "Who cares how you got here!"
                                        e ehapto "Let's get to know each other and we'll go from there"
                                        show bg a
                                        a aconflushcryedtc "{i}*sniff* {/i}"
                                        extend aconflushcryedto "Thank you..."
                                        show bg e 
                                        e eslanthapto "Of course. Let's try to enjoy our night."
                                        show bg a 
                                        a aconcflushcryedto "Yeah." 
                                        show bg e
                                        et econcflushtc "She has a cute smile*"
                                        show bg a
                                        a aconcflushcryto "Jeez, I'm so sorry, I didn't mean to get you involved in this,{w} and now I'm being rude complaining about being on this date."
                                        show bg e 
                                        e eslantconcflushto "No no, it's okay, I figured something was off when you weren't a golden retriever"
                                        show bg a 
                                        a aconflushcryto "What do you mean-"
                                        a aconflushcryedto "Oh. Right. Fake dating profile."
                                        show bg e 
                                        e econcto "You know what, I think you're prettier in person"
                                        show bg a
                                        a aconcflushcrytc "*{i}sniff*{/i}" 
                                        extend aconcflushcryto " Thank you"
                                        show bg e 
                                        show mc econctc
                                        $ aff+=3
                                        jump conversation
                            else:
                                jump comfortTO
                            label comfortTO:
                                a astunflushcryedtc "{i}*sniff*{/i}"
                                extend anervflushcryedto " Jeez, I'm so sorry, I didn't mean to get you involved in this, and now I'm being rude complaining about being on this date."
                                show bg e 
                                e econcto "No no, it's okay, I figured something was off when you weren't a golden retriever"
                                show bg a 
                                a aconflushcryto "What do you mean-"
                                a aconflushcryedto "Oh. Right. Fake dating profile."
                                show bg e 
                                e econcto "You know what, I think you're prettier in person"
                                show bg a 
                                a aconcflushto "*{i}sniff{i}* Thank you"
                                show bg e 
                                show mc econctc
                                $ aff+=1
                                jump conversation                                
                    label datingprofileTO:
                        et "I guess her entire dating profile was fake, I probably should have known after taking one look at her*"
                        e estrainto "Sorry, you just struck me as um, a fellow 'boarder'"
                        show bg a 
                        a aconto "Uh, okay."
                        show bg e 
                        et estraintc "It's probably for the best to avoid bringing up her profile, it might just upset her*"
                        $ aff-=1
                        jump conversation
                "Ask about hobbies":
                    hide screen cd
                    if(order >1):
                        e ehapto "What do you like to do for fun?"
                        show bg a 
                        a aneuedto "Well... I like gardening"
                        call warn
                        a ahapedto "There's something so fulfilling about nurturing new life"
                        show mc ahapedtc
                        call timer(3,3,'gardeningTO') from _call_timer_19
                        menu:
                            "I suck at gardening!":
                                hide screen cd
                                show bg e 
                                e estraintc "That must be hard! I can barely keep a houseplant alive, let alone a real one"
                                e "I once managed to kill a fake plant!"
                                show bg a
                                a aconto "I mean, it's not *that* hard..."
                                show bg e 
                                et estraintc "oops*"
                                $ aff-=1
                                jump conversation
                        label gardeningTO:
                            et ahapedtc "She seems lost in thought*"
                            a ahapto "Sorry, I'm being sappy" 
                            show bg e 
                            e eslanthapto "No, it's cute"
                            show bg a 
                            a aflushedto "Cute...?"
                            show bg e 
                            et econctc "Oh gosh, she's blushing, I hope I wasn't too direct*"
                            $ aff+=2
                            jump conversation
                    else: 
                        e ehapto "Well... what do you do for fun"
                        show bg a 
                        call warn
                        a aneuedrto "You know, just, the usual"
                        show bg e 
                        show mc eneutc
                        call timer(2,2,'funpryTO') from _call_timer_20
                        menu: 
                            "Pry":
                                hide screen cd
                                e eplayto "And what does \"the usual\" entail?"
                                show bg a
                                a aneuedto "Just like, watching movies I guess"
                                show bg e
                                e ehapto "Ah! Movies are cool"
                                show bg a 
                                a aneuedto "Sure" 
                                show bg e 
                                et econctc "Did I say something wrong?*"
                                $ aff-=1
                                jump conversation
                        label funpryTO:
                            e econcto "Ah, alrighty" 
                            show bg a 
                            a aneuto  "Sorry, it's just kinda personal"
                            show bg e 
                            e eslantconcto "No no, I understand"
                            e eslanthapto "Gotta keep up the mysterious thing you've got going" #eyes ^^ 
                            show bg a 
                            a aconto "Mysterious?"
                            show bg e 
                            et econctc "Shoot*"
                            e econcto "It's nothing, don't worry about it."
                            show mc econctc
                            $ aff-=1
                            jump conversation
                "Ask about work":
                    hide screen cd
                    if(order >1): #good
                        e ehapto "Well, what do you do for work?"
                        show bg a
                        show mc aconto
                        if(aff>0):
                            a "Please don't make me bore you to death, this date hasn't been half bad" #IF AFF +
                        else: 
                            a "Please don't make me bore you to death, then I'll be stuck with the bill" #IF AFF -
                        show bg e 
                        e ehapto "No really, I'm interested!"
                        show bg a 
                        a aneuto "Fine. I work in telemarketing."
                        show bg e 
                        e estarto "You sell phones? That's {i}so cool!{/i} Do you work for Furizon? Or Lycanmobile? Tailstra?"
                        show bg a 
                        a aconto "That's... {w}do you really not know what a telemarketer does?"
                        show bg e
                        e eworedtc "..." 
                        extend eworedto "No..."
                        show bg a
                        a aneueurto "Basically, I spend 8 hours a day 5 days a week calling elderly dogs and trying to convince them that their fence needs to be a whiter shade of white"
                        a aneuto "Or whatever else they have me shilling"
                        show bg e 
                        e econcto "Oh...{w} I bet you meet some interesting people at least!"
                        show bg a 
                        a aconto "Not really. Most of those old bones just yell at me for yapping too much, or they think I'm their grandpup trying to check up on them. It's just sad"
                        show bg e 
                        e eworto "Oh, I'm sorry"
                        show bg a
                        a aneuedrto "It's not your fault. At least it pays the bills"
                        show bg e
                        e eworedto "That's fair..."
                        show mc eworedtc
                        jump conversation
                    else: #bad
                        e ehapto "Well, what do you do for work?"
                        show bg a 
                        call warn
                        a aneuedto "Just some boring desk job."
                        show mc aneuedtc
                        call timer(2,2, 'jobpryTO') from _call_timer_21
                        menu: 
                            "Pry":
                                hide screen cd
                                show bg e 
                                e eplayto "Oh come on, it can't be {i}that{i} boring"
                                show bg a
                                a afrusto "Look, I just spent 8 hours in what is effectively a fluorescent prison cell trying to sell the elderly sham miracle drugs for their arthritis."
                                a "The last thing I want to do right now is think about work some more."
                                a afrustc "..."
                                a afrusedto "Sorry, I had a long day."
                                show bg e
                                e econcto "No no, I get it. I'll drop it."
                                et econctc  "Jeez, touchy subject*"
                                $ aff -=2
                                jump conversation
                        label jobpryTO:
                            show bg e 
                            e econcto "I get that. Whatever pays the bills, right?"
                            show bg a 
                            a aconto "Sorry, yeah. Do you mind if we talk about something else right now?"
                            show bg e 
                            e econcto "Of course"
                            show mc econctc
                            $ aff-=1
                            jump conversation
                "Ask about family":
                    hide screen cd
                    if(order >1): #good
                        e ehapto "Well, do you have any family nearby?"
                        show bg a
                        call warn
                        a afrusedrto "Ehh, I don't really like to talk about my family..." 
                        show mc afrusedrtc
                        call timer(2,2,'familypryTO') from _call_timer_22
                        menu:
                            "Pry":
                                hide screen cd
                                show bg e
                                e econfto "Why? Did something happen between you?"
                                show bg a 
                                a afrusedto "It's just. Complicated. And personal"
                                show bg e 
                                e econcto "Oh, I see, sorry for prying."
                                show bg a 
                                a afrusto "It's fine."
                                show bg e
                                show mc eawktc
                                $ aff-=2
                                jump conversation
                        label familypryTO:
                            a aconto "Sorry... we just aren't really on speaking terms."
                            show bg e 
                            e econcto  "I get that, family can be hell sometimes"
                            show bg a 
                            a afrusedto "Yeah."
                            a aconto "Do you mind if we change the subject?"
                            show bg e 
                            e eslantconcto "Of course"
                            show mc econctc
                            jump conversation
                    else: #bad
                        e ehapto "So... what's your family like?"
                        show bg a
                        a anervto "My family?{w} Um.{w} Normal." 
                        show bg e 
                        e econcto "Got any siblings?"
                        show bg a
                        a anerverto "No"
                        show bg e 
                        e estrainto "Ah. I see!"
                        et estraintc "WHY WOULD YOU ASK ABOUT HER FAMILY YOU DON'T KNOW HER WELL ENOUGH TO ASK THAT*"
                        $ aff-=2
                        jump conversation
            label aahTO:
                et ewortc "I don't know what to ask her...*"
                et "I can't be too intrusive but I also don't wanna be superficial*"
                et "I want to learn more about her but I don't want to make her uncomfortable*"
                et "I want to show her I'm interested but I don't want to seem desperate...*"
                et edistc "WHY DOES THIS HAVE TO BE SO HARD*"
                et eslantwortc "WHATEVER I'M TAKING TOO LONG! JUST ASK ANYTHING DOESN'T MATTER WHAT*"
                e eslantblurtto "What's your favorite color? Is it true dogs are color blind? I personally struggle a bit with greens but I don't know if that's a cat thing or just a me thing. Is everything black and white for dogs or like can you see some colors{nw}"
                e "What's it like being a dog? Is it true that you can't eat chocolate? Do they have chocolate substitutes for dogs? Or do you just have to always make sure there's no chocolate in whatever you're eating? But then what do you do if there" 
                show bg a 
                a anervto "I- um-"
                a anervconto "Could you repeat the question?"
                show bg e
                e edisflusherto "Just, um. "
                extend eawkflushto "What's your favorite color? "
                show bg a 
                a aconedrto "Um"
                a aconto "Blue? I guess?"
                show bg e 
                e eawkto "Nice"
                et eawktc "Nice job, Emory.*"
                $ aff-=1
                jump conversation

        "Crack joke" if not cj:
            $ cj=True
            $ order +=1
            hide screen cd
            if(order>1): #good if not the first thing you do
                et ehaptc "How about I try making her laugh?*"
                call warn
                et econctc "What kind of jokes do dogs like?*"
            else: #bad
                et estraintc "Gosh, the atmosphere's so tense you could cut it with a knife*"
                call warn
                et "Maybe a joke would help?*"
            call timer(8,8,'jokeTO') from _call_timer_23
            menu:
                "Cheesy joke":
                    hide screen cd 
                    if(order>1): #good
                        e ehapto "Hey Avery, how come I'm always staring at your keyboard? {w}Because I caught wind of your mouse!"
                        show bg a 
                        a aconto "You've never seen my keyboard."
                        show bg e 
                        e econcto "No, it's a joke!"
                        show bg a 
                        a aconto "I don't get it. Is the wind part relevant?"
                        show bg e 
                        e estrainto "It's a cat joke!"
                        show bg a
                        a aconto  "Wha- "
                        extend asurpto "Oh! Like mice. Cats like mice. "
                        extend ahapto "I get it." #FAINT SMILE
                        show bg e 
                        et econctc "So she {u}can{/u} smile...*"
                        $ aff+=1
                        jump conversation
                    else: #bad
                        e ehapto "Hey Avery, how come I'm always staring at your keyboard? {w} Because I caught wind of your mouse!"
                        show bg a 
                        a aconto "What?"
                        show bg e 
                        e econcto "It's a joke!"
                        show bg a
                        a acontc "..." 
                        extend aconto  "I don't get it. {w}Is the wind part relevant?"
                        show bg e
                        e estrainto "It's a cat joke!"
                        show bg a 
                        a acontc  "..."
                        extend aconto  "What?"
                        show bg e
                        e eawksweatto "Oh um, it's like, um,{w} nevermind."
                        show mc eawktc
                        jump conversation
                "Joke about being late":
                    hide screen cd 
                    if(order>1): #good
                        e econcto "So sorry for showing up late, "
                        extend ehapto "I must have left my watch in my other jeans!"
                        show bg a 
                        a askepto "Huh?"
                        a asurpto "Oh,{w} uh, "
                        extend astrainto "haha..."
                        show bg e
                        et ewortc "That's a pity laugh if I've ever seen one..*"
                        jump conversation
                    else: #bad
                        e econcto "So sorry for showing up late,{w} I must have left my clock in my other jeans!"
                        show bg a 
                        a aconto "Why were you wearing two pairs of jeans?"
                        show bg e 
                        e estrainto "No sorry not clock I meant-"
                        show bg a 
                        a aconto "And why do you carry a clock around with you?"
                        show bg e
                        e eawkto "No it was supposed to be a joke!"
                        show bg a 
                        a anervflushto "Oh um, haha"
                        a anervflushtc "..." 
                        show bg e 
                        et eawktc "Tough crowd...*" #(embarrassed) 
                        $ aff-=1
                        jump conversation
                "Sarcastic joke":
                    hide screen cd 
                    if(order>1):#good
                        e econcto "Can you believe they don't even offer valet parking for limos? What kind of establishment are these people running?"
                        show bg a 
                        a aconto "Are you joking?"
                        show bg e
                        et estraintc "She's so direct?!*"
                        e estrainto "Yeah I'm just joking"
                        show bg a 
                        a aneuto "Oh, that makes sense."
                        show bg e 
                        et eawktc "WHAT DOES THAT MEAN*"
                        $ aff-=1
                        jump conversation
                    else: #bad
                        e econcto "Can you believe they don't even offer valet parking for limos? What kind of establishment are these people running!"
                        show bg a 
                        a askepto "You drive a limo?" #unimpressed
                        show bg e 
                        e estrainto "No, I don't {i}actually{/i} drive a limo, I was joking"
                        show bg a 
                        a aconto "Oh, um. Alright."
                        show bg e 
                        et eawktc "Oops*"
                        $ aff-=2
                        jump conversation
            label jokeTO:
                et eawktc "I'm taking too long to think of a joke, I'm gonna miss my chance, just say something!*"
                e eawksweatto "So... "
                extend eawksweatedto  "um... "
                extend eawksweatto "why did,{w} um, " 
                extend eawksweatedto "the chicken, "
                extend eawksweatto "sorry, sorry,{w} so, "
                extend eawksweatedto "okay, "
                extend eawksweatto "why did the chicken cross the road?"
                show bg a 
                a afrustc "..."
                show bg e 
                e eawksweattc  "..."
                extend eawksweatto  "You're supposed to say \"why\""
                show bg a 
                a afrusto "Dude,{w} I'm not five you know"
                show bg e 
                e eawkto "Right, yeah."
                e eawktc "*{i}So much for making her laugh{i}*"
                $ aff-=1
                jump conversation

        "Ask about profile picture" if not pfp:
            hide screen cd
            if(order==4): #if you completed all 4 other options
                if(aff>0): #date is going well
                    e econcsweatedto "Hey, I was wondering-{w} and you don't have to answer this if you don't want to-{w} but I'm not sure if you are aware-{w} and again, don't feel pressure to answer-"
                    e "But what I'm trying to say is-"
                    show bg a 
                    a askepto "Spit it out"
                    show bg e 
                    e econcto "Sorry, just- Are you aware you look nothing like your profile picture on the dating site? Like, the picture is a golden retriever.{w} Which I'm pretty sure you aren't."
                    show bg a 
                    a aconto "What do you mean? I don't-"
                    a astuntc "..."
                    a astunto  "Oh Dog"
                    a astunflushedto "Dog, this is so embarrassing... my friend, the one pushing me to get into the dating scene, made my profile for me"
                    a "And I was dumb enough not to check my own profile."
                    a anervflushto "I'm so sorry, that must have been so confusing for you"
                    show bg e 
                    e eslantconcto "Not at all! I mean, I was a bit surprised, but I can tell you're real, not just some dog fisher. "
                    show bg a 
                    a anervflushedto "She said she would make me look like 'prime wife material', but I didn't realize that meant faking my entire profile"
                    a anervfrusedrto "Next time I see her she's getting chewed out"
                    show bg e 
                    e econcto "Don't sweat it, really"
                    e eslanthapto "I'm here now, on a date with you. The {i}real{/i} you. That's what matters."
                    show bg a 
                    a aconcflushto "Thanks. That means a lot to me."
                    n aconcflushtc "Just as the touching scene unfolds, it is interrupted by the waiter, arriving with the appetizers"
                    show mc awaiterconctc
                    return
                else: #date is going poorly
                    e econcto "Hey um, I thought maybe you should know, you look {i}really{/i} different from your profile picture on the dating site."
                    show bg a 
                    a afrusedrtc "..."
                    a afruscryedrto "Look, I know this night hasn't been going great, but you don't have to be cruel."
                    show bg e 
                    e eworto "Cruel?"
                    show bg a 
                    a afruscryto "I'm really trying my best, this dating shit is hard, okay. So would you please give me a break."
                    show bg e 
                    e eawkto "Sorry, I think you misunderstand, I meant that-"
                    show bg a 
                    a afruscryedto  "I know what you meant. Just drop it, okay?"
                    n afruscryedtc "Before you can figure out what to say to clear up this misunderstanding, the waiter arrives with the appetizers"
                    show mc awaiterfrustc
                    return

            elif(order >=2): #if you completed 2 or 3 options
                e econcsweatedto "You know... {w}you- um-"
                show bg a 
                a aintertc "Hm?"
                show bg e 
                e econcsweatto "It's just that you-{w} you look {i}nothing{/i} like your profile picture on that dating site"
                e "What's up with that?"
                a econcsweattc "..."
                e econcsweatto "Well?"
                show bg a 
                a afrusto "Well,{w} I think that is a very rude thing to tell someone on a first date, and I'm trying my best to be kind."
                show bg e
                e eawksweatto "Oh"
                et eawksweattc "Oh Dog, I didn't mean for it to come out like that*"
                et "I probably could have picked a better time to bring it up*"
                show bg a 
                n afrusedtc "Neither you nor Avery can think of anything to say to the other." 
                show bg e 
                n edisedtc "Eyes downcast, the two of you sit in deafening silence until, after what feels like an eternity, the waiter arrives with the appetizers"
                show mc awaiterfrustc
                return
            else: #exhausted 0 or 1 options
                e ehapto "Hey so I noticed that you look, like, absolutely nothing like your profile picture from the dating website"
                e "Like legit you look like an entirely new person"
                e econcto "I don't really know how to ask this, but like, are you dogfishing me?"
                show bg a 
                a astuntc "..." 
                show bg e 
                e econcto  "Avery?"
                show bg a 
                a astuntc "..."
                show bg e 
                e econcto "Are you feeling alright?"
                show bg a 
                a astunerto "I left my, um, sorry, I need to, um-"
                a astunto "I just remembered I'm feeling sick, I need to go"
                show bg e 
                e econcto "To the bathroom?"
                show bg a 
                a astuntc "..."
                extend astunto "Yes."
                show bg e 
                e econcto "Um, alright, don't be long!"
                show bg a 
                n empty "Avery hurriedly rushes to the bathroom, slamming the door behind her"
                n "5 minutes pass with no sign of her, then 10, then 15"
                et "Maybe I was a bit too direct...*"
                n "30 minutes pass"
                n "It becomes clear that she's not coming back"
                n "You finish your meal alone, footing the bill, then spend the rest of the night watching bad television alone"
                $ quick=True
                return
label conversationTO: #timed out conversation
    if(order==4): #if you completed all 4 options
        if(pfp): #if pfp is true, and you did talk about her pfp, do this
            hide screen cd
            if(aff < 0): #if date is going bad
                et econctc "The date hasn't been going spectacular, but at this point I have a much better read on her at least*"
                et ehaptc "I think I'm starting to figure her out, so hopefully this dating stuff only gets easier*"
            else: 
                et econctc "It's been a bit awkward at times, but overall I don't think I'm TOTALLY bombing this date*"
                et ehaptc "Now that I'm starting to actually get to know her, hopefully this dating stuff will only get easier*"
            show bg a 
            n aneueurto "No longer strangers, conversation flows more comfortably between you and Avery"
            show bg e 
            n eslanthapto "After a short bit, their idle chit chat is interrupted by the waiter, approaching with the appetizers"
            show bg a
            show mc awaiterhaptc
        else:
            et econctc "It's probably not a good idea to bring up a girl's profile picture on a first date*"
            et ehaptc "Who knows. If things work out, maybe I'll get to see her again, and I'll tell her then.*" 
            et "It'll be a funny story we reminisce about to our grandchildren*"
            show bg a 
            n ahaptc "The conversation with Avery comes to a natural conclusion, settling into a comfortable silence"
            show bg e 
            n ehaptc "The momentary lull is soon interupted by the waiter, approaching with the appetizers"
            show bg a
            show mc awaiterhaptc
    elif(order>=2): #if you completed 2 or more options
        et econctc "Did I make enough conversation?*"
        et "I don't want it to feel forced, but I can't think of anything else to say*"
        et eworedtc  "Is it better to have an drawn out superficial conversation or no conversation at all?*"
        show bg a
        n aneuedtc "The two settle into an awkward silence, sitting quietly for an uncomfortable amount of time until the waiter finally returns with the appetizers"
        show mc awaiterneutc
    else: #if you completed 0 or 1 options
        et ewortc "Why isn't she saying anything?*"
        et "Is she waiting for me to say something?*"
        et edistc "I don't know what to say!*"
        et "And now it's been too long since anyone said anything and it'll be awkward and pathetic if I try saying something to break the silence*"
        n edisedtc "You continue to sit in silence and catastrophize as minutes tick away."
        show bg a 
        n anervedtc "After an agonizing amount of time, the waiter finally returns with the appetizers"
        show mc awaiternervtc
return


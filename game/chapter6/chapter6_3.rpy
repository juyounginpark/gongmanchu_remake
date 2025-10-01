screen write_poet(title, init_name):
    frame:
        xpadding 50
        ypadding 200
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5

label chapter6_3:

    #[장소: 캠퍼스 문학 체험관]

    show jsk_standard at mid_low with dissolve
    jsk "안녕. 여기야."
    main "어, 안녕! 여기... 되게 조용하네."

    hide jsk_standard
    show jsk_sad_1 at mid_low 
    jsk "응. 사람들이 시끌시끌한 데는 싫어서."
    main "근데 이렇게 꾸며놓으니까 멋있다."
    main "여긴 시집 코너인가?"

    hide jsk_sad_1
    show jsk_joke_1 at mid_low 
    jsk "응."
    jsk "이 시, 들어봤어?"
    jsk "나태주 시인의 <풀꽃> 이야."
    main "한번 들어본거 같은데? 뭐야?"

    hide jsk_joke_1
    show jsk_standard at mid_low 
    jsk "... 여기."

    hide jsk_standard
    show jsk_shorked_2 at mid_low 
    jsk "\"자세히 보아야 예쁘다\n"
    extend "오래 보아야 사랑스럽다\n"
    extend "너도 그렇다\""

    main "..."
    main "(잠시 넋이 나갈 정도로...)"
    main "(조용하고... 이쁜 목소리다.)"

    hide jsk_shorked_2
    show jsk_joke_3 at mid_low 
    jsk "음... 이 시는 풀꽃으로 '마음의 거리'를 말하고 있는 것 같아."

    hide jsk_joke_3
    show jsk_standard at mid_low 
    jsk "빨리, 가볍게 스치면 알 수 없는 사람."
    jsk "천천히 보고, 오래 곁있어야 비로소 드러나는... "

    hide jsk_standard
    show jsk_shy_1 at mid_low 
    extend "그런 사람 있지."
    jsk "조용하고, 무채색인듯 보이지만,"

    hide jsk_shy_1
    show jsk_shy_2 at mid_low 
    jsk "속은 밝고 따뜻한 사람이 있다고."
    jsk "... 시가 그런걸 알려주는 것 같아서 좋아해."

    main "정말...이네."

    hide jsk_shy_2
    show jsk_joke_3 at mid_low 
    jsk "얘기 들어줘서 고마워."

    hide jsk_joke_3
    show jsk_standard at mid_low 
    jsk "여기 봐봐!"
    jsk "이건 단어를 뽑고, 그걸로 짧은 글을 쓰는 체험인가봐."
    jsk "재밌어 보여서 해보려 했거든."

    hide jsk_standard
    show jsk_shy_1 at mid_low 
    jsk "같이 할래?"

    main "나 시 같은건 진짜 약한데..."
    main "뭐, 아무렴 어때."
    main "기억, 따뜻함, 봄... 이라."

    jsk "..."
    $ poet = renpy.call_screen("write_poet", title="|기억| |따뜻함| |봄|", init_name=" ")
    main "나... 다 썼다."

    hide jsk_shy_1
    show jsk_standard at mid_low 
    jsk "나도."
    jsk "한번 읽어봐줄래?"

    $ mid =  len(poet) // 2
    $ poet_head = poet[:mid]
    $ poet_tail = poet[mid:]

    main "... \"[poet_head]"

    hide jsk_standard
    show jsk_shorked_2 at mid_low 
    jsk "[poet_tail]\"..."
    
    hide jsk_shorked_2
    show jsk_standard at mid_low 
    jsk "... 좋다. "
    extend "시에서 너가 느껴지는 것 같아."

    main "너것도, 한번 읽어봐줄 수 있어?"

    hide jsk_standard
    show jsk_shorked_2 at mid_low 
    jsk "..."
    jsk "\"너를 바라보던 그날의 봄,\n햇살보다 더 밝게 웃던 기억.\""

    main "많이 써본 것 같다. 느낌 있네..."

    hide jsk_shorked_2
    show jsk_shy_1 at mid_low 
    jsk "시를... 좋아해서."
    jsk "글로 전하는 게 더 좋을 때가 많거든."

    main "나만의 책갈피 코너?"
    main "저거 해볼까?"

    hide jsk_shy_1
    show jsk_standard at mid_low 
    jsk "좋아."
    jsk "이런 거 해보는 건 처음이네."

    main "(서툰 가위질이, 왠지 약간 귀여운 것 같기도...)"

    hide jsk_standard
    show jsk_joke_2 at mid_low 
    jsk "끝났어."

    main "어? 진짜 예쁘다. 글씨도 정갈하고..."

    hide jsk_joke_2
    show jsk_shorked_2 at mid_low 
    jsk "..."

    hide jsk_shorked_2
    show jsk_shy_2 at mid_low 
    jsk "이거... "
    extend "너 줄게."

    main "... 응?"
    main "내가 받아도 되는 거야?"
    jsk "응."

    hide jsk_shy_2
    show jsk_shy_3 at mid_low 
    jsk "혹시... 너 것도 줄 수 있어?"
    jsk "오늘을 오래 두고 보고 싶어서."

    main "나도."
    main "오늘 되게... 좋았어."

    hide jsk_shy_3
    show jsk_shy_2 at mid_low 
    jsk "나야말로. 고마워."
    jsk "다음에도... 같이 함께 할 수 있을까?"

    main "물론이지."

    hide jsk_shy_2 with dissolve
    ""
    show mnk_angry_2 at mid_low with dissolve
    "..."
    extend ""

    hide mnk_angry_2

    jump chapter7_1
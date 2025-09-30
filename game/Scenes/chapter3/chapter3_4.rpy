label chapter3_4:
    #scene 술집 앞
    show lhs_standard at mid_low
    lhs "어, 벌써 1시네. 우리 기숙사 통금 걸리겠다."
    A "진짜? 빨리 가야겠다~ 오늘 즐거웠어!"
    lhs "응, 나도. 잘 들어가~!"
    A "안녕~"

    hide lhs_standard
    main "...재밌었어. 안녕~"

    show jsk_shy_1 at mid_low
    jsk "저기... 잠깐만...!"
    
    #show jsk_shy at center
    main "응...?"
    jsk "핸드폰 번호... 알려줄래?"

    menu:
        "1. 알려준다.":
            jump jsk_happy2
        "2. 번호 대신 카톡을 알려준다.":
            jump jsk_sad2

    label jsk_happy2:
        main "....번호? 아.. 응, 알겠어"

        hide jsk_shy_1
        show jsk_shy_2 at mid_low
        jsk "....고마워. 잘 들어가."
        main "응... 너도."
        
        hide jsk_shy_2
        jump chapter3_5

    label jsk_sad2:
        main "어...? 갑자기?"

        hide jsk_shy_1
        show jsk_shy_2 at mid_low
        jsk "응..."
        main "핸드폰 번호는 조금 그런데... 혹시 카톡 알려주는 건 안될까?"

        hide jsk_shy_2
        show jsk_sad_2 at mid_low
        jsk "아... 응..."

        hide jsk_sad_2
        jump chapter3_5
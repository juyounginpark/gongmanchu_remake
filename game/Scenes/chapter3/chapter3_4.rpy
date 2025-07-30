label chapter3_4:
    #scene 술집 앞
    #show lhs_smile at center
    lhs "어, 벌써 1시네. 우리 기숙사 통금 걸리겠다."
    #show A_silhouette at center
    A "진짜? 빨리 가야겠다~ 오늘 즐거웠어!"
    #show lhs_smile at center
    lhs "응, 나도. 잘 들어가~!"
    #show A_silhouette at center
    A "안녕~"

    main "...재밌었어. 안녕~"

    #show black
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
        system "정성경 +10"
        main "....번호? 아.. 응, 알겠어"
        #show jsk_smile at center
        jsk "....고마워. 잘 들어가."
        main "응... 너도."
        jump chapter3_5

    label jsk_sad2:
        system "정성경 -10"
        main "어...? 갑자기?"
        #show jsk_shy at center
        jsk "응..."
        main "핸드폰 번호는 조금 그런데... 혹시 카톡 알려주는 건 안될까?"
        #show jsk_sad at center
        jsk "아... 응..."
        jump chapter3_5
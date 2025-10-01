label chapter4_1:
    #[장소: 캠퍼스 한켠 자판기 앞]

    main "4시간 풀강 들었더니 죽을 것같다..."
    main "뭐라도 마실까."
    main "역시 음료수는 샤인머스캣이지..."

    "(음료에 손을 뻗으려는 찰나, 옆에서 익숙한 목소리가 들렸다)"
    "???" "혹시... 경민이?"

    "(고개를 돌린다. 긴 흑발에 잔잔한 눈웃음, 어딘가 낯익은 얼굴)"
    show pyr_standard at mid_low with dissolve
    "" ""
    main "어...? 잠깐만. 너... 혹시..."

    menu:
        "여름이... 맞지?":
            $ likeYeoreum += 20
            
            pyr "맞아. "
            extend "박여름."

            hide pyr_standard 
            show pyr_joke_1 at mid_low
            pyr "기억하는구나!"

        "미안한데... 혹시 이름이?":
            $ likeYeoreum += 10
            
            hide pyr_standard
            show pyr_sad_4 at mid_low
            pyr "..."
            pyr "박여름. 기억안나?"
        "누구세요?":
            $ likeYeoreum += 0
            
            hide pyr_standard
            show pyr_angry_4 at mid_low
            pyr "... 기억안나?"
            pyr "박여름."

    main "(확실히 기억났다. 나의 초등학교부터의 소꿉친구, 박여름.)"
    main "와, 아니... 진짜 반갑다."

    hide pyr_joke_1
    hide pyr_sad_4
    hide pyr_angry_4
    show pyr_standard at mid_low
    pyr "옛날에 우리 친했잖아. "
    extend "... 그때나 지금이도 똑같네, 너."
    main "아하하... 응. 진짜 오랜만이다."
    main "..."

    hide pyr_standard
    show pyr_sad_2 at mid_low
    pyr "..."
    main "아! 그나저나... 너는 무슨 과야?"

    hide pyr_sad_2
    show pyr_standard at mid_low
    pyr "응, 난 미술대. 너는?"
    main "나는 저기 컴퓨터공학과..."
    pyr "아아..."

    main "..."
    hide pyr_standard
    show pyr_sad_2 at mid_low
    pyr "..."

    hide pyr_sad_2
    show pyr_joke_1 at mid_low
    pyr "그렇구나. 뭐 마시려던거 맞지? 마저 뽑아!"
    main "아, 응."

    hide pyr_joke_1
    show pyr_shorked_2 at mid_low
    pyr ""
    pyr "..."
    pyr "역시나 취향도 그대로네. 너나 나나."
    main "응? 뭐라고?"

    hide pyr_shorked_2
    show pyr_shy_2 at mid_low
    pyr "아, 아니야. 아무것도. "

    hide pyr_shy_2
    show pyr_shy_1 at mid_low
    pyr "음, 혹시, 다음수업있어?"
    main "아니... 없어."

    hide pyr_shy_1
    show pyr_shy_2 at mid_low
    pyr "그럼 좀 같이 걸을래?"
    main "! ...그래!"

    hide pyr_shy_2
    jump chapter4_2
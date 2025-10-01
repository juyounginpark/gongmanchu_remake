label chapter4_4:
    #[장소: 캠퍼스 산책길2]

    show pyr_standard at mid_low
    main "여름이 오려나, 벌써 덥네."
    pyr "… 그러네. 있잖아."
    main "응?"

    hide pyr_standard
    show pyr_shy_2 at mid_low
    pyr "너는 참 변한게 없는것 같아. 상냥하고, 말도 잘 들어주고."

    hide pyr_shy_2
    show pyr_shy_1 at mid_low
    pyr "그래서 그런데…"

    hide pyr_shy_1
    show pyr_shorked_1 at left_low
    show pjy_standard at right_low with vpunch
    pjy "어라? 경민이 안녕? 여기서 보네."
    main "주연 선배…!"
    pjy "이쪽은…"

    menu:
        "옛날에 정말 친했던 친구요.":
            $ likeYeoreum += 20
            main "아, 옛날에 정말 친했던 친구인데, 오랜만에 만나게 되어서요."
        "옛날 친구요.":
            $ likeYeoreum += 10
            main "아, 옛날 친구인데… 우연히 만나서요."
        "아, 그냥 친구요.":
            $ likeYeoreum += 0
            main "아… 그냥 친구요."

    pyr "안녕하세요…"
    
    hide pjy_standard
    show pjy_joke_1 at right_low
    pjy "아, 안녕하세요~"

    hide pyr_shorked_1 
    show pyr_joke_1 at left_low 
    pyr "난 이만 가볼게. 아. 잠시만… 폰 좀 줘봐."
    main "(엇, 전화번호를...)"

    hide pyr_joke_1
    show pyr_standard at left_low 
    pyr "그럼."
    main "어… 응. 잘가."
    hide pyr_standard with dissolve

    hide pjy_joke_1
    show pjy_sad_1 at mid_low
    pjy "…"

    hide pjy_sad_1
    show pjy_standard at mid_low 
    pjy "나도 이만 할일이 있어서, 안녕~"
    main "아, 네!"

    hide pjy_standard with dissolve

    "(둘이 멀어지는 모습을 번갈아 보는 그때-)"
    "(조용히 반대쪽에 있던 한 사람)"
    show jsk_angry_3 at mid_low with dissolve
    main "성경이…?"
    "(말없이 경민을 바라보다 손을 흔들고 사라진다)"
    hide jsk_angry_3 with dissolve

    main "하아… 마음속이 복잡하네."

    jump chapter5_1
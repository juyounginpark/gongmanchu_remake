label chapter4_4:
    scene campus_walk_background 
    with dissolve
    show pyr standard at center:
        xoffset -150 
    with dissolve
    main "여름이 오려나, 벌써 덥네."
    pyr "… 그러네. 있잖아."
    main "응?"
    pyr "너는 참 변한 게 없는 것 같아. 상냥하고, 말도 잘 들어주고."
    
    show pyr shy_1 at center:
        xoffset -150 
    with dissolve
    pyr "그래서 그런데…"

    main "응? 무슨 일 있어?"
    pyr "아, 아니야. 그냥 혼잣말."

    show pjy standard at right_low:
        xoffset 150 
    with dissolve
    pjy "어라? [player_name] 안녕? 여기서 보네."
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

    show pyr sad_1 at left_low:
        xoffset -150 
    with dissolve
    pyr "안녕하세요…"
    pjy "아, 안녕하세요~"
    
    pyr "난 이만 가볼게. 아. 잠시만… 손 좀 줘봐."

    main "이건… 반지잖아?"
    show pyr shy_1 at left_low:
        xoffset -150 
    with dissolve
    pyr "그럼."
    
    hide pyr 
    with dissolve
    main "어… 응. 잘가."

    show pjy sad_1 at right_low:
        xoffset 150 
    with dissolve
    pjy "…"
    show pjy standard at right_low:
        xoffset 150 
    with dissolve
    pjy "나도 이만 할 일이 있어서, 안녕~"
    main "아, 네!"
    
    hide pjy 
    with dissolve
    
    main "(두 사람이 떠난 자리를 멍하니 바라보았다.)"
    main "(그런데 저쪽에서...)"
    
    show jsk sad_1 at center:
        xoffset 150 
    with dissolve
    main "성경이…?"
    
    "(성경이는 말없이 나를 바라보더니, 작게 손을 흔들고는 사라졌다.)"
    
    hide jsk 
    with dissolve

    main "하아… 마음속이 복잡하네."

    jump chapter5_1
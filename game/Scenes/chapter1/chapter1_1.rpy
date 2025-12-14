label chapter1_1:
    scene campus_walk_background
    with fade
    main "음... 여기가 한국대학교 대강당인가."
    main "생각보다 엄청 넓네... 어디로 가야 하는 거지?"
    
    play sound pjy_giggle
    show pjy standard at center
    with dissolve
    
    pjy "안녕하세요! 신입생 맞으시죠? 어느 학부세요?"
    main "아, 네! 컴퓨터학부 신입생입니다."
    
    show pjy joke_1 at center
    with dissolve
    pjy "와! 저도 컴퓨터학부예요. 그럼 제가 선배네요?"
    pjy "만나서 반가워요. 저는 23학번 박주연이라고 해요."
    main "아... 안녕하세요! 저는 [player_name](이)라고 합니다."

    show pjy standard at center
    with dissolve
    pjy "이쪽으로 쭉 따라오시면 자리 안내해 드릴게요."
    
    show pjy shy_1 at center
    with dissolve
    pjy "전 오늘 신입생 도우미라서, 나중에 또 봐요!"
    
    hide pjy
    with dissolve
    
    main "(...되게 친절하고 상냥한 선배네.)"

    "주연 선배의 밝은 미소를 뒤로하고, 나는 안내받은 강당 안쪽으로 발걸음을 옮겼다."
    "잠시 후, 왁자지껄한 분위기 속에서 신입생 환영회가 시작되었다."
    
    jump chapter1_2

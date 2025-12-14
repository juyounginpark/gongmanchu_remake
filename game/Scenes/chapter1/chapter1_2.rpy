label chapter1_2:
    scene pub_background
    with fade
    
    show lhs shy_1 at center
    with dissolve
    lhs "저기... 안녕하세요. 혹시 컴퓨터학부세요?"
    main "네? 아, 네... 컴퓨터학부 신입생입니다."

    show lhs shorked_1 at center
    with dissolve
    play sound lhs_giggle
    lhs "오~ 반가워요! 전 이현서라고 해요."
    main "전 [player_name](이)라고 합니다."
    
    show lhs shy_2 at center
    with dissolve
    lhs "저도 25학번 신입생인데... 우리 말 편하게 할까?"
    main "그, 그래. 현서야."
    
    show lhs standard at center
    with dissolve
    lhs "근데 너 아까 그 오티 도우미 선배 봤어?"
    main "응. 박주연 선배 말하는 거지?"
    
    show lhs shy_2 at center
    with dissolve
    lhs "응, 그 선배. 진짜 분위기 있지 않아?"
    lhs "딱 봤는데 연예인 같아서 깜짝 놀랐어."
    
    main "(나만 그렇게 생각한 게 아니었구나...)"
    main "나도 처음 보고 놀랐어. 목소리도 좋으시고, 말씀도 되게 잘하시더라."
    
    show lhs standard at center
    with dissolve
    lhs "그러게. 성함이 박주연 선배님이시랬지? 이름도 예쁘셔."
    main "그러네. 네 말이 딱 맞는 것 같아."

    hide lhs
    with dissolve

    "신입생 환영회가 끝나고, 우리는 같은 조 선배, 동기들과 함께 뒤풀이 장소로 이동했다."
    "어색함과 설렘이 공존하는 술자리, 유리잔 부딪히는 소리가 공간을 채웠다."

    jump chapter1_3

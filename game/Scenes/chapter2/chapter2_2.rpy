label chapter2_2:
    #[배경: 해달 동아리방]

    main "(여기가 동아리실…?)"
    main "안녕하세요!"

    show parkjuyoun_standard at main_position
    pjy "어서와~ 둘다 동아리실은 처음이지?"

    #show hyunseo_standard at main_position
    lhs "네!"

    pjy "반가워~ 편하게 앉아요."
    lhs "보통 동방에선 주로 뭐하세요? 주로 코딩?"

    pjy "음… 코딩도 하고. 밥도 시켜먹고, 가끔 수다만 떨다 가기도 해."
    main "(자주 오시나보다…)"

    pjy "그나저나, 학교 생활은 할만해? 수업은 좀 어때?"
    main "할만한 것 같아요. 약간 졸긴했는데…"
    pjy "처음엔 다 그렇지. 학식은 먹어봤어?"
    main "네. 공식당갔는데 줄 장난 아니던데요…"
    pjy "맞아~ 거긴 항상 그래. 다음엔 러브로드쪽 건너서 있는 정보화 식당 가봐요."

    lhs "‘러브로드’ 요?"
    main "‘러브로드’ 가 뭐에요?"

    pjy "몰랐구나? 우리 학교 전설인데, 썸타는 둘이 러브로드를 처음부터 끝까지 걸으면 사랑이 이루어진대."

    main "선배도 걸어본 적 있어요?"
    pjy "음… 아직? 아직은 없지. 같이 걸을 사람이 없어서~"

    #show parkjuyoun_prank at main_position
    pjy "왜, 같이 걷고싶은 사람이라도 있어?"

    menu:
        "네":
            $likeJuyoun += 10
            main "네… 있어요."
        "아니요":
            main "아니요…"

    pjy "흐흐, 괜찮아. 아직 1학년이잖아. 러브로드 천천히 걷는거야~"
    pjy "아 맞다, 이번 MT 신청했어? 신나게 놀아보자~"
    jump chapter2_3
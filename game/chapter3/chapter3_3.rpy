label chapter3_3:
    #scene 술집 내부

    show lhs_standard at left_low
    lhs "아직 안 왔네. 조금 늦는다더니."
    main "괜찮아. 뭐... 아직 시간도 있고."
    A "안녕하세요~ 많이 기다리셨어요?"
    lhs "아뇨, 저희도 방금 왔어요. 저는 이현서, 여긴 제 친구 서경민."
    A "저는 A예요. 여기는 제 친구 정성경."

    show jsk_standard at right_low with dissolve
    jsk "...안녕하세요."
    lhs "두 분은 어떤 과세요?"
    A "우린 경영학과요. 25학번이고요."
    lhs "오, 우리도 25학번! 저희는 컴퓨터학부예요."
    A "컴공! 완전 어려운 거 한다~ 멋지다."
    
    hide jsk_standard
    show jsk_shorked_2 at right_low
    jsk "...대단해요."
    main "경영은 어때요? 분위기나 수업 같은 거..."

    hide jsk_shorked_2
    show jsk_standard at right_low
    jsk "괜찮은 거 같아요."
    lhs "저희는 진짜 과제가 미친 듯이 나와요. 근데 그래도 뭐... 재미는 있어요. 경영은 약간 팀플 많다고 들었는데 맞나요?"
    A "맞아요! 거의 팀플 천국이에요. 전 좀 사람 만나는 거 좋아해서 나쁘진 않아요~"
    main "전 대문자 I 라서 그런데… 대단하네요."
    A "아니에요, 여기 성경이도 엄청 낯가리는데 어떻게든 하더라고요."

    hide jsk_standard
    show jsk_shy_3 at right_low
    jsk "....네. 할만 하더라고요..."
    main "'...지금 웃는 거 맞나...?'"
    jsk "...컴공 수업은 재밌어요?"
    main "어.. 그냥, 해볼 만은 해요. 아직은 적응 중이라서."
    lhs "저희 다 25학번이면 다들 딱딱하게 존댓말 하지 말고, 말 편하게 놓을까요?"
    A "응! 너무 좋다. 서로 딱딱하게 하지 말고 편하게 반말하자."

    menu:
        "1. 말을 놓는다.":
            main "그럼 이제 말 편하게 할게."
            jump jsk_happy

        "2. 말을 놓지 않는다.":
            main "아... 아뇨. 전 아직 그렇게 편하지 않아서 전 존댓말 쓸게요."
            jump jsk_sad

    label jsk_happy:
        hide jsk_shy_3
        show jsk_shy_2 at right_low
        jsk "...응, 좋아."
        jump next

    label jsk_sad:
        hide jsk_shy_3
        show jsk_sad_1 at right_low
        jsk "....네."
        A "아... 네."
        lhs "에이, 그러지말고 다같이 말놓자~"
        main "(분위기가... 윽.)"
        main "아, 농담이에요. 말 놓으셔도 돼요!"
        jump next

    label next:
        main "'현서랑 A는 대화 엄청 잘 나누네.'"
        main "저... 성경아. 넌 어쩌다가 경영학과에 가게 됐어?"

        hide jsk_shy_3
        hide jsk_sad_1
        show jsk_standard at right_low
        jsk "아... 제일 무난하다고 생각이 들어서... 넌 어쩌다가 컴퓨터학부로 가게 된거야?"
        main "난 예전부터 컴퓨터 쪽에 관심이 많았어서... 이쪽으로 오게 됐어."
        jsk "아... 그렇구나."
        lhs "그럼 다들 서로에 대해서 간단한건 알게 된 거 같은데 일단 술 한잔 할까?"
        A "좋다. 다들 잔 들고~ 짠~!"

        hide lhs_standard
        hide jsk_standard
        jump chapter3_4
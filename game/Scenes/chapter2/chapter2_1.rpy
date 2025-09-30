label chapter2_1:
    #[배경: 대학 가두모집 거리]

    "(웅성웅성)"

    main "우와... 이게 말로만 듣던 가두모집이구나."
    main "진짜 동아리들이 많네..."
    main "어떤 동아리가 나를 기다리려나."

    show lhs_standard at mid_low with vpunch #prank
    lhs "경민아!"
    main "헉, 현서야?! 여긴 어쩐 일이야?"
    #show hyunseo_standard at main_position
    lhs "나도 오늘 가두 모집 보러왔지 ~"
    lhs "따로 동아리 생각해둔거 있어?"
    main "아직 모르겠어..."

    hide lhs_standard with fade
    "(현서와 복작복작한 동아리 라인을 걷는다)"
    main "(다들 자기 동아리 홍보하느라 열오르는 분위기...)"
    main "(어...? 저기 저 사람...)"

    
    show pjy_standard at right_low with dissolve
    pjy "‘부트캠프’로 코딩 알려주는 해달! 코딩 왕초보도 환영~"
    main "(어? 주연 선배다... 저기서 홍보 중이네)"
    main "(동아리 이름이... 해달?)"

    show lhs_standard at left_low
    lhs "저기 주연 선배 아냐?"
    main "응... 근데 괜히 인사하기 민망하네. 기억 못하면 어색할지도..."
    lhs "뭐 어때~ 기억 못하면 웃고 넘어가면 되지. 자, 가자!"

    menu:
        "용기내서 인사한다":
            $likeJuyoun += 20
            main "ㅅ...선배! 안녕하세요."

            show pjy_shorked_4 at right_low
            pjy "어! 경민씨! 그땐 잘 들어갔어요?"
            main "(이름, 기억하고 있으시네...)"
            main "네...! 그땐 감사했어요! 여기서도 열일 하시네요..."

            hide pjy_shorked_4
            show pjy_standard at right_low
            pjy "ㅎㅎ 신입생들에게 동아리 소개중이에요. 혹시 동아리 찾고있어요?"
            main "어떤 동아리에요?"

        "인사하지 않는다":
            main "(그냥 조용히 지나가자.)"

    pjy "해달은 초보자 부담없이 들어올 수 있어요!"
    pjy "C언어, 웹, 파이썬 부트캠프도 있고 해커톤이랑 mt도 자주해요!"
    main "(오오... mt라.)"

    hide lhs_standard
    show lhs_shorked_1 at left_low
    lhs "괜찮아 보이는데? 우리 같이 들어갈래?"
    main "응! 저... 해달에 가입하고 싶어요!"
    pjy "진짜요? 환영해요~"

    hide lhs_shorked_1
    hide pjy_standard

    jump chapter2_2
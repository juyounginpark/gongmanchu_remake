label chapter7_3:
    scene dorm_room_night with fade
    "지잉- 지잉-"

    main "음…"
    main "헉, 나 언제 잠들었지…?"
    main "누구지…?"

    # 모니카와의 문자 대화
    python:
        mnk_conv = PhoneConversation(
            [["나", None], ["모니카", "mnk standard"]],
            [
                1,
                ("어젠 미안했어요.", "오전 9:00"),
                ("괜찮으시면 집 앞 카페로 나와주실 수 있나요?", "오전 9:01"),
            ]
        )
    call screen phone(mnk_conv)

    main "(히익…!)"
    main "(무서워 죽겠네…)"
    main "(물론 가기 싫지만, 가만히 놔두면 주위 사람들까지 위험해질지도 몰라…)"

    # 답장
    python:
        mnk_conv2 = PhoneConversation(
            [["나", None], ["모니카", "mnk standard"]],
            [
                0,
                ("그럴게요.", "오전 9:03"),
            ]
        )
    call screen phone(mnk_conv2)

    jump chapter7_4

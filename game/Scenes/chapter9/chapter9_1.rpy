label chapter9_1:
    scene dorm_room_night with fade
    main "오늘도 힘든 날이었다."
    main "자자…"
    pause 1.0
    main "(정말… 신경 쓰여서 잠이 오질 않잖아.)"
    main "(대체 내가 뭘 잘못한 건데…)"

    "김민수 교수님의 말이 떠올랐다."
    kms "\"중요한 것은, 솔직함과 배려야.\""
    kms "\"그리고, 자신감.\""

    main "…"
    main "(이젠 정말, 선택해야 할 때야.)"

    "(전화벨이 울린다.)"
    main "이 시간에… 모니카잖아?"
    main "(분명… 지금은 얘를 생각할 때가 아니야.)"
    main "(아냐, 그래도... 어쩌지.)"

    menu:
        "→ 전화를 받는다":
            # 모니카 전화 수신
            call screen phone_incoming_call("Monika", "mnk standard", "M")

            main "여보세요?"

            show screen phone_call_active("Monika", "mnk standard", "M")

            mnk "\"으응… 자?\""
            main "아, 아니. 왜?"
            mnk "\"그냥 오늘 지나가다 봤는데 힘들어 보이길래~\""
            mnk "\"걱정되어서 전화해봤어.\""
            main "(… 처음엔 이상한 애인 줄 알았는데, 속은 참 따뜻한 아이인 것 같다.)"
            mnk "\"언제든 힘들면… 내게 기댔으면 좋겠어.\""
            main "고마워."
            main "잠도 안 오는데, 좀 얘기하다 잘래?"
            mnk "\"그래…?\""
            play sound mnk_giggle
            mnk "\"쿠로냥 이야기나 할래? 흐흐…\""
            main "어떤 얘기든 좋아."
            main "(이 애랑 있으면 편안하다 못해, 점점 빨려 들어가는 느낌이야.)"

            hide screen phone_call_active

            $ route = "monika"
            jump chapter10_1

        "→ 전화를 받지 않는다":
            main "(그래. 지금은 이 애를 생각할 때가 아니야.)"
            main "(어서… 선택해야 해.)"

            menu:
                "→ 주연 선배에게 메시지를 보낸다.":
                    python:
                        pjy_conv = PhoneConversation(
                            [["나", None], ["박주연", "pjy standard"]],
                            [
                                0, "선배, 내일 시간 돼요?",
                                1, "응~ 왜?",
                                0, "좀 드릴 말씀이 있어서요.",
                                1, "알았어, 내일 보자!",
                            ]
                        )
                    call screen phone(pjy_conv)
                    $ route = "juyoun"
                    jump chapter9_2

                "→ 성경에게 메시지를 보낸다.":
                    python:
                        jsk_conv = PhoneConversation(
                            [["나", None], ["정성경", "jsk standard"]],
                            [
                                0, "성경아, 내일 같이 도서관 가지 않을래?",
                                1, "... 좋아.",
                                0, "ㅋㅋ 내일 보자!",
                                1, "응, 기대할게.",
                            ]
                        )
                    call screen phone(jsk_conv)
                    $ route = "sungkyung"
                    jump chapter9_3

                "→ 여름에게 메시지를 보낸다.":
                    python:
                        pyr_conv = PhoneConversation(
                            [["나", None], ["박여름", "pyr standard"]],
                            [
                                0, "여름아, 내일 같이 카페 가서 공부할래?",
                                1, "오 갑자기?",
                                0, "응, 같이 있고 싶어서.",
                                1, "흐흐... 알았어!",
                            ]
                        )
                    call screen phone(pyr_conv)
                    $ route = "yeoreum"
                    jump chapter9_4

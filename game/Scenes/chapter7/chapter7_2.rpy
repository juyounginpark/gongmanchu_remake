# CH7-2
label chapter7_2:
    scene dorm_room_night with fade
    main "허억… 허억…."
    main "대체 뭐지? 난 완전 처음 보는 사람인데…!"
    main "몰카? 장난? 애초에 저런 미소녀가 저럴 리가 없잖아…"

    # 전화 수신 화면 (발신자 표시 제한 - 이미지 없음)
    call screen phone_incoming_call("발신자 표시 제한", None, "?")

    # 전화를 받음
    main "발신자 표시 제한…?"

    # 통화 중 화면 표시
    show screen phone_call_active("발신자 표시 제한", None, "?")

    main "여보… 여보세요?"

    mnk "\"네~ 여보에요~\""

    main "예?"

    mnk "\"집 잘 들어갔죠?\""
    main "당신… 아까 그 사람이지?"

    mnk "\"비밀~\""
    mnk "\"오늘은 장난 좀 쳐봤어요.\""
    mnk "\"잘 자요!\""

    main "저기요? 저기요??"

    # 통화 종료
    hide screen phone_call_active
    call screen phone_call_ended("발신자 표시 제한", "00:23")

    main "대체 뭐냐고…"
    main "신고해도 소용없을 것 같고…"
    main "일단 최대한 조심해야겠다."
    main "하… 피곤해 죽겠네… 진짜…"

    jump chapter7_3

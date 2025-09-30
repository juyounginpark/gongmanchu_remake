label chapter8_2:

    # [배경: 강의실 복도]

    main "(하아… 머리가 터질 것 같다.)"
    main "(시험 준비도 힘든데, 요즘 사람들의 시선이 거슬린다.)"

    # 등장인물 대사 (익명)
    "쟤가 걔야?"
    "아, 사다리남? 네 다리 걸친다는?"
    "맞는 것 같은데?"

    main "(… 역시 그 애의 짓일까, 모니카.)"

    if likeJuyoun >= 50: #걍 데이트 한사람이랑ㅇㅇ
        jump chapter8_3

    elif likeSungkyung >= 50:
        jump chapter8_4

    elif likeYeoreum >= 50:
        jump chapter8_5

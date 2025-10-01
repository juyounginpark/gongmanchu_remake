label chapter9_1:

# [배경: 경민의 집 - 밤]

    main "..."
    main "요새 자꾸 안좋은 일이 일어나는 것만 같네."
    main "아, 피곤해..."
    main "자자."
    main "..."
    main "정말... 신경쓰여서 잠이 오질 않잖아."
    main "대체 내가 뭔 잘못을 한건데..."

    #회상
    kms "중요한 것은, 솔직함과 배려야."
    kms "그리고, 자신감."

    main "..."
    main "전혀 그러지 못했잖아."
    main "내가 바보였어..."

    "(전화음)"

    main "뭐야, 모니카잖아?"
    main "... 그런 소문을 내놓고 떳떳하게 전화라니."
    main "일단 받아볼까."

    if likeMonika >= 20: #모니카 루트 탔을 시
        mnk "으응... 자?"
        main "아, 아니. 왜?"
        mnk "그냥 오늘 지나가다 봤는데 힘들어보이길래~"
        mnk "걱정되어서 전화해봤어."
        main "(... 이상한 애인줄 알았는데.)"
        main "(사실 속은 따뜻한 아이일지도.)"
        mnk "언제든 힘들면... 내게 기댔으면 좋겠어."
        main "... 고마워."
        main "잠도 안오는데, 좀 얘기하다 잘래?"
        mnk "그래...?"
        mnk "쿠로냥 이야기나 할래? 흐흐..."
        main "어떤 얘기든 좋아."
        main "(이 애랑 있으면 편안하다 못해)"
        main "(점점 빨려들어가는 느낌이야)"
        mnk "..."
        jump chapter10_1

    else :
        main "... 여보세요?"
        mnk "안녕?"
        mnk "요새 좀 어때?"
        mnk "" #스토리 보충
        main ""

        if likeJuyoun >= 50: 
            main "선배, 혹시 내일 바빠요?"
            jump chapter9_2

        elif likeSungkyung >= 50:
            main "성경아, 혹시 내일 시간 괜찮아?"
            jump chapter9_3

        elif likeYeoreum >= 50:
            main "여름아, 혹시 내일 볼 수 있을까?"
            jump chapter9_4
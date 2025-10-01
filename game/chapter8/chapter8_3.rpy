label chapter8_3:

    # [배경: 강의실 복도]
    
    show pjy_sad_1 at mid_low
    pjy "" 
    main "(선배다!)"
    main "어, 선배. 안녕하세요."
    pjy "... 응."
    main "(반응이...)"
    main "(소문, 신경쓰고 있으신걸까.)"
    pjy "요새 바쁜가봐? 연락이 통 없네."
    main "아, 시험 기간이라 그런지..."
    pjy "그래?"
    pjy "... 하루종일 시험 공부만 하는건 아닐 거 아냐."
    main "아..."

    hide pjy_sad_1
    show pjy_angry_1 at mid_low
    pjy "또, 그렇다기엔 여자애들 많이 만나고 다니는 것 같던데."
    pjy "뭐, 어디까지나 소문일 뿐일테지만."
    main "소문은 정말 사실이 아니에요..."
    
    hide pjy_angry_1
    show pjy_sad_1 at mid_low
    pjy "..."
    pjy "너가 뭘하던 그건 너 자유니까 내가 간섭할건 없지."
    pjy "시험 준비 열심히 해."
    pjy "그럼."

    main "아..."
 
    hide pjy_sad_1 with dissolve
    main "..."
    main "정말 왜 이런거지..."

    jump chapter9_1
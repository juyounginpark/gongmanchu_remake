label chapter10_3:
    # [배경: 캠퍼스 산책길]

    show jsk_standard at mid_low with dissolve
    jsk "(톡톡)"
    main "응?"
    main "아, 성경이네. 여기서 기다렸구나."

    hide jsk_standard
    show jsk_joke_2 at mid_low with dissolve
    jsk "안녕."
    jsk "이제 시험 다 끝난거야?"
    main "응."
    
    hide jsk_joke_2
    show jsk_joke_3 at mid_low with dissolve
    jsk "나도. 확실히 마음이 한결 가벼워."
    main "맞아. 이제야 숨 좀 돌릴 수 있겠다..."
    main "..."
    main "음, 벚꽃이 다 졌네."

    hide jsk_joke_3
    show jsk_sad_1 at mid_low
    jsk "맞아. 봄은 늘 시험이랑 겹쳐서, 꽃 구경은 잠깐이고... "

    hide jsk_sad_1
    show jsk_sad_2 at mid_low
    extend "\n마음놓고 즐길 시간이 없어."
    main "정말로."
    main "그래도 그런만큼, 그 짧은 순간이 소중하게 느껴지는 것 같아."
    main "우리가 처음 만난 날이나,"
    main "축제 날이나..."

    hide jsk_sad_2
    show jsk_shy_1 at mid_low
    jsk "... 응."
    jsk "많은 추억을 남겼네."
    jsk "처음 봤을땐 우리가 이런 사이가 될 줄은 몰랐는데."
    jsk "그 때 용기내서 번호 달라하길 잘했어."

    hide jsk_shy_1
    show jsk_shy_2 at mid_low
    jsk "헤헷..."

    main "(윽... 귀여워.)"

    hide jsk_shy_2
    show jsk_shy_3 at mid_low
    jsk "넌 정말 소중한 친구야."
    jsk "내 취향도 잘맞춰주고."
    jsk "내가 오해했을때도 먼저 연락해주고."

    main "딱히 맞춰주기보단..."
    main "너랑 함께 하는게 좋았어서긴 한데."
    main "다행이네. 그렇게 봐준다니."

    hide jsk_shy_3
    show jsk_shorked_2 at mid_low
    jsk "... "
    jsk "그런 말, 잘 들어본 적 없는데..."

    hide jsk_shorked_2
    show jsk_standard at mid_low
    jsk "저기, 그럼 이번주 주말에 만나지 않을래?"
    jsk "예전에는 내가 좋아하는 거 했으니까, 이번에는 너 취향대로."

    main "음, 좋아!"
    main "어디갈진 잘 모르겠는데... 서점같은 데라도 갈래?"
    main "이번엔 다른 책도 추천해줘."

    hide jsk_standard
    show jsk_shy_1 at mid_low
    jsk "..."
    jsk "좋아."
    main "좋지?"

    hide jsk_shy_1
    show jsk_shy_2 at mid_low
    jsk "아니, 너 말이야."
    main "으, 응?"

    hide jsk_shy_2
    show jsk_shorked_2 at mid_low
    jsk "나조차도 몰랐던 감정을 끌어내는... 너가."

    hide jsk_shorked_2
    show jsk_shy_3 at mid_low
    jsk "..."
    jsk "저기, 나 할말이 있는데."
    main "... 응."

    hide jsk_shy_3
    show jsk_shy_2 at mid_low
    jsk "나랑 사귀어줄래?"
    jsk ""
    main "..."
    main "(항상 생각해왔던 오늘이다.)"
    main "(늘 상상해왔지만, 깜짝 놀란 심장은 주체할 수 없었다.)"
    main "(정적을 깨닫게 될 쯤에는, 내 손은 성경이의 손 위에 있었다.)"
    main "좋아."

    hide jsk_shy_2
    show jsk_joke_1 at mid_low
    jsk "... 고마워."
    main "주말에 만나기로 한거 말이야,"
    main "주말에 말고, 지금 바로 갈까?"

    hide jsk_joke_1
    show jsk_standard at mid_low
    jsk "아니, 주말에도 가고. 오늘도 가자. 헤헤..."
    main "그래!"

    return
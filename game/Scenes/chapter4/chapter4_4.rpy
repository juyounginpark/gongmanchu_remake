label chapter4_4:
    #[장소: 캠퍼스 산책길2]

    main "여름이 오려나, 벌써 덥네."
    pyr "… 그러네. 있잖아."
    main "응?"
    pyr "너는 참 변한게 없는것 같아. 상냥하고, 말도 잘 들어주고."
    #show parkyeoreum_shame at main_position
    pyr "그래서 그런데…"

    #show parkjuyoun_standard at main_position
    pjy "어라? 경민이 안녕? 여기서 보네."
    main "주연 선배…!"
    pjy "이쪽은…"

    menu:
        "옛날에 정말 친했던 친구요.":
            $ likeYeoreum += 20
            main "아, 옛날에 정말 친했던 친구인데, 오랜만에 만나게 되어서요."
        "옛날 친구요.":
            $ likeYeoreum += 10
            main "아, 옛날 친구인데… 우연히 만나서요."
        "아, 그냥 친구요.":
            $ likeYeoreum += 0
            main "아… 그냥 친구요."

    #show parkyeoreum_serious at main_position
    pyr "안녕하세요…"
    parkjuyoun "아, 안녕하세요~"
    #show parkyeoreum_standard at main_position
    pyr "난 이만 가볼게. 아. 잠시만… 손 좀 줘봐."

    main "이건… 반지잖아."
    #show parkyeoreum_shame at main_position
    pyr "그럼."
    main "어… 응. 잘가."

    #show parkjuyoun_serious at main_position
    pjy "…"
    show pjy_standard at main_position
    pjy "나도 이만 할일이 있어서, 안녕~"
    main "아, 네!"

    "(둘이 멀어지는 모습을 번갈아 보는 그때-)"
    "(조용히 반대쪽에 있던 한 사람)"
    main "성경이…?"
    #show jeongseonggyoung_serious at main_position
    "(말없이 경민을 바라보다 손을 흔들고 사라진다)"

    main "하아… 마음속이 복잡하네."

    jump chapter5_1
label chapter4_3:
    #[장소: 캠퍼스 근처 벤치]

    show pyr_standard at mid_low
    pyr "난 가끔 그때 생각이 나. \n"
    extend "고등학교 때 이사만 안갔으면, 쭉 함께였을텐데."
    main "(윽, 꽤나 부끄러운 말을...)"

    hide pyr_standard
    show pyr_shy_4 at mid_low
    pyr "아니...! 그, 그정도는 아니고!"

    hide pyr_shy_4
    show pyr_shy_2 at mid_low
    pyr "그냥... 그땐 조금 그랬었어. 여러 사정이 있었어서."
    main "(엄마가 알려줬었지, 아버지 사업 때문이랬나...) \n"
    extend "어쩔 수 없었구나."

    hide pyr_shy_2
    show pyr_joke_1 at mid_low
    pyr "응, 지금은 완전 괜찮지만."

    hide pyr_joke_1
    show pyr_sad_2 at mid_low
    pyr "고등학교 가서는 많이 힘들었어. 친한 친구도 없고..."
    pyr "그래서 한때는 너무 힘들어서, 미술도 그만 두려 했어."
    main "...응."

    hide pyr_sad_2
    show pyr_sad_1 at mid_low
    pyr "그래서... 음... 너가 많이 그립긴 했어."
    pyr "어릴때 누가 뭐래도 항상 칭찬도, 응원도, 믿음도 줬었던 너가."

    hide pyr_sad_1
    show pyr_sad_2 at mid_low
    pyr "갑작스레 떠난건 난데, 꼴사납지? 하하..."
    main "아, 아니야!"
    main "(연락도 없길래 그냥 잊고 잘 지내는 줄만 알았는데...)"
    pyr "그런데 있지, 우울감에 한동안 방에만 있었는데.\n"
    extend "방정리를 하다 우연히 옛날 공책을 보게됐어."
    main "(아.)"
    pyr "너랑 나랑 그렸던 그림이랑..."
    main "(기억나.)"

    hide pyr_sad_2
    show pyr_sad_1 at mid_low
    pyr "너가 써놓은 편지를 보고... 정말 큰 위로가 됐었어."
    main "(... 몰래 적어뒀었는데 말이지.)"
    
    hide pyr_sad_1
    show pyr_sad_2 at mid_low
    pyr "아. 너무 무거운 얘기만 했네. 미안..."
    main "아냐! 나도 오랜만에 옛날 생각나서 좋았어."

    hide pyr_sad_2
    show pyr_joke_1 at mid_low
    pyr "고마워. 들어줘서. 정말로... 이렇게 만나게 되어서 정말 다행이야."
    main "나도 그래. 하하..."
    pyr "이제 일어날까?"

    hide pyr_joke_1
    jump chapter4_4

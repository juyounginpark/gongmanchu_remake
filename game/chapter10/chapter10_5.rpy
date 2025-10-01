# chXX Monika 얀데레 루트
label chapter10_5:
    "스윽-"

    main "으윽."

    #[배경: monika의 집 안]
    main "(으윽...)"
    main "(여긴 어디지...?)"
    main "(어두워서 아무것도 안보여...)"
    main "(뭐에 묶였는지 움직일 수도 없네...)"
    main "(갑자기 정신을 잃었는데...)"

    show mnk_standard_2 at mid_low with dissolve
    mnk "깼어?"
    main "헉...!"
    main "뭐야? 누구야?"

    hide mnk_standard_2
    show mnk_standard at mid_low
    mnk "나야, Monika."
    main "여기가 어디야...?"

    hide mnk_standard
    show mnk_joke_1 at mid_low
    mnk "여기, 내 집."
    mnk "헤헤... 이제 경민이 한가하지 않아?"
    mnk "앞으로 나랑 계속 함께 할 수 있지?"

    main "(온통 방안에 내 사진에다가...)"
    main "(다른 사람들 사진 위에 엑스표...)"
    main "(이거... 위험해...!)"

    hide mnk_joke_1
    show mnk_angry_5 at mid_low
    mnk "왜 대답을 안하는거야?"
    mnk "... 설마 "

    hide mnk_angry_5
    show mnk_angry_4 at mid_low
    extend "그 망할 여자애들 생각 중인건 아니지?"

    hide mnk_angry_4
    show mnk_joke_1 at mid_low
    mnk "상관없어! "
    extend "내가 다 잘 얘기해뒀으니까."

    hide mnk_joke_1
    show mnk_standard at mid_low
    mnk "경민이는 너같은 애들은 관심 없다고, "
    extend "여러 여자들 꼬시고 다니는 어장남이라고."

    hide mnk_standard
    show mnk_joke_1 at mid_low
    mnk "히히히... 나 잘했지. 응?"
    main "이... 일단 이것좀 풀어줄래."

    hide mnk_joke_1
    show mnk_sad_2 at mid_low
    mnk "많이 불편했지? 미안해..."

    hide mnk_sad_2
    show mnk_sad_1 at mid_low
    mnk "그치만~ "
    extend "경민이가 예전처럼 또 도망쳐버리면 어쩌지?"

    hide mnk_sad_2
    show mnk_sad_1 at mid_low
    mnk "도망치지 못하게 하려면, "

    hide mnk_sad_1
    show mnk_angry_5 at mid_low
    extend "뭘 잘라야할까?"
    main "...!"

    hide mnk_standard
    show mnk_joke_1 at mid_low
    mnk "꺄아~ 귀여워..."

    hide mnk_joke_1
    show mnk_sad_1 at mid_low
    mnk "농담이야~ 내가 어떻게 경민이 몸에 그래..."

    hide mnk_sad_1
    show mnk_standard at mid_low
    mnk "이대로 몇달간만 지내보고, 말 잘들으면 풀어줄게."
    mnk "내가 열심히 돈벌어오구..."

    hide mnk_standard
    show mnk_joke_1 at mid_low
    mnk "음식도 사주고, 하고 싶은 비디오 게임있으면 사줄게."

    hide mnk_joke_1
    show mnk_angry_5 at mid_low
    mnk "온라인 게임은 안돼."
    mnk "..."

    hide mnk_angry_5
    show mnk_angry_4 at mid_low
    mnk "왜 대답이 없어? "
    extend "역시 걔네 생각중인거지?"

    main "아, 아니야. 전혀 아니야. 일단 진정하고..."

    hide mnk_angry_4
    show mnk_joke_1 at mid_low
    mnk "그렇지? 그럼 다행이야..."

    hide mnk_joke_1
    show mnk_standard_2 at mid_low
    mnk "그런데 계속 거슬리는게 있어."
    if likeJuyoun >= 50 :
        mnk "그 망할 선배랑 잡은 오른손 있잖아."
    if likeSungkyung >= 50 :
        mnk "그 망할 과팅녀랑 닿았던 검지손가락 있잖아."
    if likeYeoreum >= 50 :
        mnk "그 망할 소꿉친구랑 마주쳤던 눈 말이야."

    hide mnk_standard_2
    show mnk_angry_2 at mid_low
    mnk "거기서 구역질 나오는 악취가 나는것 같아."
    mnk "그것만 없으면 좋을 것 같은데."

    main "아, 아니야. 이건-"

    hide mnk_angry_2
    show mnk_angry_1 at mid_low
    mnk "아니야."
    mnk "아직 난 경민이를 못믿겠어... 또 저번처럼 떠나가면 어떡하지?"
    mnk "아예 싹을 잘라두어야해... 경민이는 영원히 나만의 것이여야만해."

    hide mnk_angry_1
    show mnk_joke_1 at mid_low
    mnk "아까처럼 자고일어나면 괜찮아 질거야."
    mnk "아프진 않을테니까 걱정마. 사랑해, 경민아."

    main "아니야, 안돼... 윽."

    mnk "그럼."

    return
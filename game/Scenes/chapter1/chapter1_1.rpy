label chapter1_1:
    jump chapter8_5

    #scene 강당

    "...와, 여기가 한국대학교의 대강당이구나."
    "엄청 넓은데 안내해주시는 분은 어딨지...?"
    
    show pjy_standard at mid_low
    pjy "안녕하세요~ 신입생 맞으시죠? 어느 과예요?"
    main "아, 네. 컴퓨터학부 신입생이예요."
    
    hide pjy_standard
    show pjy_joke_1 at mid_low
    pjy "아! 저도 거기 학부예요. 이럼 제가 선배가 되겠네요."
    pjy "만나서 반가워요. 저는 23학번 박주연이라고 해요."
    main "아... 저는 서경민이예요."

    hide pjy_joke_1
    show pjy_standard at mid_low
    pjy "이쪽 줄로 쭉 따라가면 자리 있어요."
    pjy "저는 오늘 도우미니까 나중에 또 봬요~"
    
    hide pjy_standard with fade
    "'말투도 차분하고... 진짜 선배 같다..'"
    
    jump chapter1_2

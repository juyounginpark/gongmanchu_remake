label chapter6_1:
    #[배경: 경민의 기숙사]

    "(지잉- 지잉-)"
    "(지잉-)"

    main "우으음…"
    main "이 신성한 주말아침에…"
    main "뭐지…?"

    "박주연: 뭐해? 오전 8:30"
    "정성경: 안녕 오전 2:12"
    "박여름: 자? 어제 오후 11시"

    main "!!"
    main "이게 뭐야?"
    main "정말, 왜 시간대도 다 제각각이냐고…"
    main "(누구한테 먼저 답장을 해야하지…?)"

    menu:
        "주연":
            $likeJuyoun += 20
            main "(뭐해…?)"
            main "(뭐했다고 해야하지?)"
            main "(방금 일어났다고 하면 게으르다 생각할거고)"
            main "아침먹고 산책중입니다ㅎㅎ 오전 8:33"

            pjy "오 부지런하다! 오전 8:35"
            pjy "(대충 멋지다?는 이모티콘) 오전 8:35"
            pjy "아 맞다 오전 8:36"
            pjy "내일 축제하는거 알아? 오전 8:36"
            main "네! 오전 8:36"
            pjy "나 축제가고싶은데ㅠㅠ 오전 8:36"
            pjy "같이 갈 사람이 없어서 오전 8:36"
            pjy "혹시 같이 돌아다닐래? 오전 8:36"
            pjy "(ㅠㅠ이모티콘) 오전 8:37"

            main "(우와…! 이건 데이트 신청?)"
            main "(설마… 나… 가능성이 있을지도?)"
            main "네 좋아요! 오전 8:38"

            pjy "오 고마워~ 오전 8:38"
            pjy "그럼 축제 때 보자! 연락해! 오전 8:38"
            main "네! 오전 8:38"
            main "우와… 내가 주연 선배랑?"
            main "벌써 심장이 두근두근대…"
            main "뭘 해야하지? 빨리 옷 사야겠다…!"
            main "… 현서한테 물어봐야지."

        "성경":
            $likeSungkyung += 20
            main "(뭐야 이 시간에…)"
            main "(그래도 답장은 해야겠지?)"
            main "(안녕 이모티콘) 오전 8:33"
            main "새벽에 잠이 잘 안왔나봐? ㅎㅎ"

            jsk "응 오전 8:33"
            jsk "책 읽다가 잠들었어."
            main "오"
            main "책 좋아하나봐? 오전 8:34"
            jsk "응 오전 8:34"
            jsk "있잖아"
            main "응? 오전 8:34"
            jsk "이번 축제 때, 문학 체험관이 열린다고 하더라고. 책을 좋아하는 사람들이 직접 꾸민 부스도 있어. 또 조용한 분위기라서, 사람 많아도 편하게 둘러볼 수 있을 것 같아. 혹시 시간 되면, 같이 가줄 수 있을까? 편하게 말해줘. 그냥 같이 보면 좋을 것 같아서. 오전 8:36"

            main "(엄청난 양이네…)"
            main "(뭐… 괜찮으려나)"
            main "그래 그러자! 오전 8:36"
            main "(…)"
            main "(왜 답장이 안오지?)"

            jsk "응 고마워."
            jsk "그때 연락할게."
            main "응 축제 때 봐!"
            main "볼수록 특이한 친구같네."
            main "문학에는 완전 젬병인데…"
            main "미리 책 좀 읽어둬야겠다."

        "여름":
            $likeYeoreum += 20
            main "(11시…? 어제 피곤해서 바로 잤더니…)"
            main "미안! 바로 잠들어버렸어ㅎㅎ 오전 8:33"

            pyr "아냐! 괜찮아 ㅎㅎ 오전 8:33"
            pyr "그게"
            pyr "내일 축제한다는데 같이 가지않을래?"

            main "(응…?)"
            main "(정말… 얘 뭐지…)"
            main "좋아!"

            pyr "(좋다는 이모티콘)"
            pyr "알겠어!"
            pyr "내일 연락할게!"
            main "응 내일봐!"

    jump chapter6_2
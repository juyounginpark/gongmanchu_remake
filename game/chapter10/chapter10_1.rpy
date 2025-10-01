label chapter10_1:

# 배경: 캠퍼스 앞, 해질녘

main "(드디어 중간고사가 끝났다.)"

main "(참 많은 일들이 있었지.)"

main "(주연 선배.)"
main "(정말 든든하고, 재밌는 사람이었어.)"

main "(성경이.)"
main "(너랑 있을때면, 나 자신을 좀 더 들여다보게 돼.)"

main "(여름이.)"
main "(오랜 친구지만, 그 이상의 감정을 느끼고 있다는 걸 알게됐어.)"

main "(그리고... monika 까지.)"
main "(마음은 널 피해도 결국 널 의식하게 됐었어.)"

main "(참 많은 인연이 지나갔지만,)"
main "(내가 가장 붙잡고 싶은 사람은,)"

# 호감도 분기 # 호감도 분기라기보단 루트로 갑니데잉
if likeJuyoun >= 50:
    jump chapter10_2  # 주연 루트

elif likeSungkyung >= 50:
    jump chapter10_3  # 성경 루트

elif likeYeoreum >= 50:
    jump chapter10_4  # 여름 루트

elif likeMonika >= 20:
    jump chapter10_5  # 모니카 루트

elif likeJuyoun < 50 and likeSungkyung < 50 and likeYeoreum < 50 and likeMonika < 20 and likeProfessor >= 30:
    jump chapter10_6  # 교수 루트

else:
    jump chapter10_7  # 배드엔딩
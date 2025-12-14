###############################################################################
# 스마트폰 메시지 시스템 (iMessage 스타일)
# 0GUI-Adds (https://github.com/Kiaazad/0GUI-Adds) 참고
###############################################################################

init python:
    class PhoneMessage:
        """개별 메시지를 저장하는 클래스"""
        def __init__(self, text, time=None):
            self.text = text
            self.time = time

    class PhoneConversation:
        """스마트폰 대화를 관리하는 클래스"""
        def __init__(self, participants, messages):
            """
            participants: 참여자 목록 - [(이름, 이미지경로), ...]
                         0번 인덱스는 플레이어 (오른쪽 표시)
            messages: 대화 내용 목록
                     - 숫자: 화자 전환 (0=플레이어, 1,2,3...=상대방)
                     - 문자열: 메시지 내용
                     - 튜플 (메시지, 시간): 시간 포함 메시지
                     - 리스트: 선택지
            """
            self.participants = participants
            self.messages = list(messages)
            self.sent = []  # [(화자인덱스, [PhoneMessage들]), ...]
            self.typing = ""
            self.typing_time = None
            self.current_speaker = None
            self.speaking = None
            self.current_msg = None
            self.current_time = None
            self.wait_time = 0
            self.choices = None
            self.speed = 0.04
            self.finished = False
            self.waiting_for_input = False  # 스페이스바 대기 상태

        def set_choice(self, choice):
            self.current_msg = choice
            self.choices = None

        def tick(self):
            if self.finished or self.waiting_for_input:
                return

            if self.wait_time > 0:
                self.wait_time -= self.speed
                return

            if self.current_msg is None:
                if not self.messages:
                    self.finished = True
                    return

                raw_msg = self.messages.pop(0)
                self.wait_time = 0.2

                if isinstance(raw_msg, int):
                    self.current_speaker = raw_msg
                    self.speaking = raw_msg
                    # 플레이어 차례면 입력 대기
                    if raw_msg == 0 and self.messages:
                        next_msg = self.messages[0]
                        if not isinstance(next_msg, int) and not isinstance(next_msg, list):
                            self.waiting_for_input = True
                    return

                if isinstance(raw_msg, list):
                    self.choices = raw_msg
                    return

                if isinstance(raw_msg, tuple):
                    self.current_msg = raw_msg[0]
                    self.current_time = raw_msg[1] if len(raw_msg) > 1 else None
                else:
                    self.current_msg = raw_msg
                    self.current_time = None

                self.typing_time = self.current_time

            if self.choices:
                return

            if self.typing != self.current_msg:
                self.typing = self.current_msg[:len(self.typing) + 1]
            else:
                msg_obj = PhoneMessage(self.current_msg, self.current_time)
                if self.current_speaker is not None:
                    self.sent.append([self.current_speaker, [msg_obj]])
                    self.current_speaker = None
                else:
                    if self.sent:
                        self.sent[-1][1].append(msg_obj)

                self.current_msg = None
                self.current_time = None
                self.typing = ""
                self.typing_time = None
                self.wait_time = 0.15

                renpy.restart_interaction()

        def advance(self):
            """스페이스바로 진행"""
            if self.waiting_for_input:
                self.waiting_for_input = False
                renpy.restart_interaction()

        def get_partner_name(self):
            if len(self.participants) > 1:
                p = self.participants[1]
                if isinstance(p, (list, tuple)):
                    return p[0]
                elif hasattr(p, 'name'):
                    return p.name
                return str(p)
            return "메시지"

        def get_participant_image(self, index):
            if index < len(self.participants):
                p = self.participants[index]
                if isinstance(p, (list, tuple)) and len(p) > 1:
                    return p[1]
            return None

        def get_participant_name(self, index):
            if index < len(self.participants):
                p = self.participants[index]
                if isinstance(p, (list, tuple)):
                    return p[0]
                elif hasattr(p, 'name'):
                    return p.name
                return str(p)
            return "?"

default current_phone_conv = None

###############################################################################
# iMessage 스타일 스크린
###############################################################################

screen phone(conv):
    modal True
    zorder 100

    # 배경
    add "#1c1c1e"

    # 타이머
    if (conv.messages or conv.current_msg) and not conv.choices and not conv.waiting_for_input:
        timer conv.speed repeat True action Function(conv.tick)

    # 스페이스바로 진행
    if conv.waiting_for_input:
        key "K_SPACE" action Function(conv.advance)
        key "K_RETURN" action Function(conv.advance)

    # iPhone 프레임
    frame:
        xysize (430, 800)
        padding (0, 0)
        background "#000000"
        align (0.5, 0.5)

        # 노치 영역 (상단)
        frame:
            xfill True
            ysize 50
            yalign 0.0
            background "#000000"

            # 시간
            text "9:41":
                size 15
                color "#fff"
                align (0.5, 0.4)
                bold True

        # 헤더
        frame:
            xfill True
            ysize 60
            ypos 50
            background "#1c1c1e"
            padding (15, 0)

            hbox:
                yalign 0.5
                spacing 10

                # 뒤로가기
                textbutton "〈":
                    text_size 24
                    text_color "#007AFF"
                    text_hover_color "#4da6ff"
                    yalign 0.5
                    action Return()

                # 프로필 이미지 (상단 1/3 얼굴 부분만)
                $ partner_img = conv.get_participant_image(1)
                if partner_img:
                    frame:
                        xysize (40, 40)
                        yalign 0.5
                        add partner_img:
                            crop (0, 0, 1.0, 0.33)
                            size (40, 40)
                else:
                    frame:
                        background "#3a3a3c"
                        xysize (40, 40)
                        yalign 0.5

                        text conv.get_partner_name()[0]:
                            size 18
                            color "#fff"
                            align (0.5, 0.5)

                # 이름
                vbox:
                    yalign 0.5
                    text conv.get_partner_name():
                        size 17
                        color "#fff"
                        bold True

        # 메시지 영역
        frame:
            background "#1c1c1e"
            xfill True
            ypos 110
            ysize 630
            padding (10, 10)

            viewport id "phone_vp":
                draggable True
                mousewheel True
                scrollbars None
                yinitial 1.0
                xfill True
                yfill True

                vbox:
                    xfill True
                    spacing 6
                    yalign 1.0

                    for msg_group in conv.sent:
                        $ speaker_idx = msg_group[0]
                        $ msg_list = msg_group[1]

                        for idx, msg in enumerate(msg_list):
                            if speaker_idx == 0:
                                # 내 메시지 (오른쪽, 파란색)
                                hbox:
                                    xalign 1.0
                                    spacing 6

                                    if msg.time:
                                        text msg.time:
                                            size 11
                                            color "#8e8e93"
                                            yalign 1.0

                                    frame:
                                        background Solid("#007AFF")
                                        padding (12, 8, 12, 8)
                                        xmaximum 280

                                        text msg.text:
                                            color "#fff"
                                            size 16

                            else:
                                # 상대 메시지 (왼쪽, 회색)
                                hbox:
                                    xalign 0.0
                                    spacing 6

                                    # 프로필 (첫 메시지만, 상단 1/3 얼굴)
                                    if idx == 0:
                                        $ img = conv.get_participant_image(speaker_idx)
                                        if img:
                                            frame:
                                                xysize (32, 32)
                                                yalign 1.0
                                                add img:
                                                    crop (0, 0, 1.0, 0.33)
                                                    size (32, 32)
                                        else:
                                            frame:
                                                background "#3a3a3c"
                                                xysize (32, 32)
                                                yalign 1.0

                                                text conv.get_participant_name(speaker_idx)[0]:
                                                    size 14
                                                    color "#fff"
                                                    align (0.5, 0.5)
                                    else:
                                        null width 38

                                    frame:
                                        background Solid("#3a3a3c")
                                        padding (12, 8, 12, 8)
                                        xmaximum 250

                                        text msg.text:
                                            color "#fff"
                                            size 16

                                    if msg.time:
                                        text msg.time:
                                            size 11
                                            color "#8e8e93"
                                            yalign 1.0

                    # 타이핑 중 (상대방)
                    if conv.speaking and conv.speaking != 0 and conv.typing:
                        hbox:
                            xalign 0.0
                            spacing 6

                            $ img = conv.get_participant_image(conv.speaking)
                            if img:
                                frame:
                                    xysize (32, 32)
                                    yalign 1.0
                                    add img:
                                        crop (0, 0, 1.0, 0.33)
                                        size (32, 32)
                            else:
                                frame:
                                    background "#3a3a3c"
                                    xysize (32, 32)
                                    yalign 1.0

                                    text "...":
                                        size 14
                                        color "#fff"
                                        align (0.5, 0.5)

                            frame:
                                background Solid("#3a3a3c")
                                padding (12, 8, 12, 8)
                                xmaximum 250

                                text conv.typing:
                                    color "#fff"
                                    size 16

                    # 입력 대기 중 표시
                    if conv.waiting_for_input:
                        hbox:
                            xalign 0.5
                            frame:
                                background Solid("#2c2c2e")
                                padding (20, 8)
                                text "스페이스바를 눌러 답장하기":
                                    size 13
                                    color "#8e8e93"

        # 하단 입력창 (장식)
        frame:
            xfill True
            ysize 60
            yalign 1.0
            background "#1c1c1e"
            padding (10, 10)

            frame:
                background Solid("#3a3a3c")
                xfill True
                ysize 36
                padding (15, 0)

                text "iMessage":
                    color "#8e8e93"
                    size 15
                    yalign 0.5

    # 선택지
    if conv.choices:
        vbox:
            align (0.5, 0.5)
            spacing 12

            for choice in conv.choices:
                button:
                    xsize 380
                    background Solid("#3a3a3c")
                    hover_background Solid("#007AFF")
                    padding (16, 14)

                    text choice:
                        color "#fff"
                        size 16
                        xalign 0.5

                    action Function(conv.set_choice, choice)


###############################################################################
# 알림 화면 (잠금화면 스타일) - 클릭으로 선택
###############################################################################

screen phone_notifications_select():
    modal True
    zorder 100

    add "#000000"

    frame:
        xysize (430, 800)
        padding (0, 0)
        background "#000000"
        align (0.5, 0.5)

        # 상단 시간
        vbox:
            align (0.5, 0.15)
            spacing 5

            text "9:41":
                size 70
                color "#fff"
                xalign 0.5
                bold True

            text "토요일, 5월 10일":
                size 18
                color "#fff"
                xalign 0.5

        # 알림 목록
        vbox:
            align (0.5, 0.55)
            spacing 12
            xsize 400

            # 주연 선배
            button:
                xfill True
                background Frame(Solid("#2c2c2ecc"), 14, 14, 14, 14)
                hover_background Frame(Solid("#3a3a3acc"), 14, 14, 14, 14)
                padding (12, 10)
                action Return("pjy")

                hbox:
                    spacing 10
                    yalign 0.5

                    frame:
                        xysize (42, 42)
                        add "pjy standard":
                            crop (0, 0, 1.0, 0.33)
                            size (42, 42)

                    vbox:
                        spacing 2
                        xfill True

                        hbox:
                            xfill True
                            text "박주연":
                                size 15
                                color "#fff"
                                bold True
                            text "오전 8:30":
                                size 13
                                color "#8e8e93"
                                xalign 1.0

                        text "뭐해?":
                            size 14
                            color "#ebebf5"

            # 성경
            button:
                xfill True
                background Frame(Solid("#2c2c2ecc"), 14, 14, 14, 14)
                hover_background Frame(Solid("#3a3a3acc"), 14, 14, 14, 14)
                padding (12, 10)
                action Return("jsk")

                hbox:
                    spacing 10
                    yalign 0.5

                    frame:
                        xysize (42, 42)
                        add "jsk standard":
                            crop (0, 0, 1.0, 0.33)
                            size (42, 42)

                    vbox:
                        spacing 2
                        xfill True

                        hbox:
                            xfill True
                            text "정성경":
                                size 15
                                color "#fff"
                                bold True
                            text "오전 2:12":
                                size 13
                                color "#8e8e93"
                                xalign 1.0

                        text "안녕":
                            size 14
                            color "#ebebf5"

            # 여름
            button:
                xfill True
                background Frame(Solid("#2c2c2ecc"), 14, 14, 14, 14)
                hover_background Frame(Solid("#3a3a3acc"), 14, 14, 14, 14)
                padding (12, 10)
                action Return("pyr")

                hbox:
                    spacing 10
                    yalign 0.5

                    frame:
                        xysize (42, 42)
                        add "pyr standard":
                            crop (0, 0, 1.0, 0.33)
                            size (42, 42)

                    vbox:
                        spacing 2
                        xfill True

                        hbox:
                            xfill True
                            text "박여름":
                                size 15
                                color "#fff"
                                bold True
                            text "어제 오후 11:00":
                                size 13
                                color "#8e8e93"
                                xalign 1.0

                        text "자?":
                            size 14
                            color "#ebebf5"


###############################################################################
# 전화 화면 (iPhone 스타일)
###############################################################################

transform phone_vibrate:
    xoffset 0
    linear 0.03 xoffset 3
    linear 0.03 xoffset -3
    linear 0.03 xoffset 3
    linear 0.03 xoffset -3
    linear 0.03 xoffset 0
    pause 0.5
    repeat

transform call_icon_pulse:
    alpha 1.0
    easein 0.8 alpha 0.5
    easeout 0.8 alpha 1.0
    repeat

transform calling_dots:
    alpha 0.4
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.4
    repeat

# 전화 수신 화면
screen phone_incoming_call(caller_name, caller_image=None, caller_id="?"):
    modal True
    zorder 100

    add "#000000"

    frame at phone_vibrate:
        xysize (430, 800)
        padding (0, 0)
        background "#000000"
        align (0.5, 0.5)

        vbox:
            align (0.5, 0.3)
            spacing 15

            # 프로필
            if caller_image:
                add caller_image at call_icon_pulse:
                    size (100, 100)
                    xalign 0.5
            else:
                frame at call_icon_pulse:
                    background "#3a3a3c"
                    xysize (100, 100)
                    xalign 0.5

                    text caller_id:
                        size 40
                        color "#fff"
                        align (0.5, 0.5)

            text caller_name:
                size 28
                color "#fff"
                xalign 0.5

            text "iPhone 음성 통화":
                size 16
                color "#8e8e93"
                xalign 0.5

        # 버튼
        hbox:
            align (0.5, 0.82)
            spacing 60

            # 거절
            vbox:
                spacing 8
                button:
                    xysize (65, 65)
                    background Solid("#ff3b30")
                    hover_background Solid("#ff6961")
                    action Return("decline")

                    text "✕":
                        size 30
                        color "#fff"
                        align (0.5, 0.5)

                text "거절":
                    size 13
                    color "#fff"
                    xalign 0.5

            # 수락
            vbox:
                spacing 8
                button:
                    xysize (65, 65)
                    background Solid("#34c759")
                    hover_background Solid("#5fd97e")
                    action Return("accept")

                    text "✓":
                        size 30
                        color "#fff"
                        align (0.5, 0.5)

                text "수락":
                    size 13
                    color "#fff"
                    xalign 0.5


# 통화 중 화면
screen phone_call_active(caller_name, caller_image=None, caller_id="?", call_time="00:00"):
    zorder 50

    add "#000000aa"

    frame:
        xysize (430, 800)
        padding (0, 0)
        background "#1c1c1e"
        align (0.5, 0.5)

        vbox:
            align (0.5, 0.25)
            spacing 12

            if caller_image:
                add caller_image:
                    size (90, 90)
                    xalign 0.5
            else:
                frame:
                    background "#3a3a3c"
                    xysize (90, 90)
                    xalign 0.5

                    text caller_id:
                        size 36
                        color "#fff"
                        align (0.5, 0.5)

            text caller_name:
                size 24
                color "#fff"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 3
                text call_time:
                    size 15
                    color "#34c759"
                text "...":
                    size 15
                    color "#34c759"
                    at calling_dots


# 통화 종료 화면
screen phone_call_ended(caller_name, duration="00:00"):
    modal True
    zorder 100

    add "#000000"

    frame:
        xysize (430, 800)
        padding (0, 0)
        background "#1c1c1e"
        align (0.5, 0.5)

        vbox:
            align (0.5, 0.4)
            spacing 15

            text "통화 종료":
                size 22
                color "#ff3b30"
                xalign 0.5

            text caller_name:
                size 20
                color "#fff"
                xalign 0.5

            text duration:
                size 16
                color "#8e8e93"
                xalign 0.5

        button:
            align (0.5, 0.65)
            xsize 150
            background Solid("#3a3a3c")
            hover_background Solid("#007AFF")
            padding (15, 12)
            action Return()

            text "확인":
                size 16
                color "#fff"
                xalign 0.5


###############################################################################
# 헬퍼 함수/레이블
###############################################################################

init python:
    def create_phone_conv(partner_name, partner_image, messages):
        """대화 생성 헬퍼"""
        participants = [
            ["나", None],
            [partner_name, partner_image]
        ]
        return PhoneConversation(participants, messages)

label phone_call(caller_name, caller_image=None, caller_id="?"):
    call screen phone_incoming_call(caller_name, caller_image, caller_id)
    if _return == "accept":
        $ _phone_call_accepted = True
    else:
        $ _phone_call_accepted = False
    return _phone_call_accepted

label show_call_screen(caller_name, caller_image=None, caller_id="?"):
    show screen phone_call_active(caller_name, caller_image, caller_id)
    return

label hide_call_screen:
    hide screen phone_call_active
    return

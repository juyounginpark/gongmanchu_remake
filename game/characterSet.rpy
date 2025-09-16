# === 상수 정의 ===
define X_LEFT   = 0.0
define X_CENTER = 0.5
define X_RIGHT  = 1.0

define Y_TOP    = 0.0
define Y_MID    = 0.0
define Y_BOTTOM = 0.0

# === 포지션 정의 ===
define left_top    = Position(xalign=X_LEFT,   yalign=Y_TOP)
define mid_top     = Position(xalign=X_CENTER, yalign=Y_TOP)
define right_top   = Position(xalign=X_RIGHT,  yalign=Y_TOP)

define left_mid    = Position(xalign=X_LEFT,   yalign=Y_MID)
define center      = Position(xalign=X_CENTER, yalign=Y_MID)
define right_mid   = Position(xalign=X_RIGHT,  yalign=Y_MID)

define left_low    = Position(xalign=X_LEFT,   yalign=Y_BOTTOM)
define mid_low     = Position(xalign=X_CENTER, yalign=Y_BOTTOM)
define right_low   = Position(xalign=X_RIGHT,  yalign=Y_BOTTOM)

# === 연출용 ===
define far_left    = Position(xalign=-0.2,     yalign=Y_BOTTOM)
define far_right   = Position(xalign=1.2,      yalign=Y_BOTTOM)
define center_high = Position(xalign=X_CENTER, yalign=0.3)
define tilt_left   = Position(xalign=0.3,      yalign=Y_MID)
define tilt_right  = Position(xalign=0.7,      yalign=Y_MID)

transform bounce:
    yoffset -15
    linear 0.15 yoffset 0
    yoffset 0
    linear 0.15 yoffset -10
    linear 0.15 yoffset 0


# standard 
#with fade → 화면이 점점 어두워졌다가 밝아짐
#with dissolve → 부드럽게 전환
#with pixellate → 픽셀화되면서 전환
#with vpunch → 화면이 위아래로 흔들림
#with hpunch → 화면이 좌우로 흔들림

#system
define system = Character('System', color="#000000")

#배율
define zoomNUm = 0.5
# 박주연
define pjy = Character('박주연', color="#a01361")
#standard
image pjy_standard = Transform("characterImages/pjy/pjy_standard.png", zoom=zoomNUm)
#shy
image pjy_shy_1 = Transform("characterImages/pjy/pjy_shy_1.png", zoom=zoomNUm)
image pjy_shy_2 = Transform("characterImages/pjy/pjy_shy_2.png", zoom=zoomNUm)
image pjy_shy_3 = Transform("characterImages/pjy/pjy_shy_3.png", zoom=zoomNUm)
image pjy_shy_4 = Transform("characterImages/pjy/pjy_shy_4.png", zoom=zoomNUm)
#shorked
image pjy_shorked_1 = Transform("characterImages/pjy/pjy_shorked_1.png", zoom=zoomNUm)
image pjy_shorked_2 = Transform("characterImages/pjy/pjy_shorked_2.png", zoom=zoomNUm)
image pjy_shorked_3 = Transform("characterImages/pjy/pjy_shorked_3.png", zoom=zoomNUm)
image pjy_shorked_4 = Transform("characterImages/pjy/pjy_shorked_4.png", zoom=zoomNUm)
#sad
image pjy_sad_1 = Transform("characterImages/pjy/pjy_sad_1.png", zoom=zoomNUm)
image pjy_sad_2 = Transform("characterImages/pjy/pjy_sad_2.png", zoom=zoomNUm)
#joke
image pjy_joke_1 = Transform("characterImages/pjy/pjy_joke_1.png", zoom=zoomNUm)
#angry
image pjy_angry_1 = Transform("characterImages/pjy/pjy_angry_1.png", zoom=zoomNUm)
image pjy_angry_2 = Transform("characterImages/pjy/pjy_angry_2.png", zoom=zoomNUm)


# 이현서
define lhs = Character('이현서', color="#6c86c9")
#standard
image lhs_standard = Transform("characterImages/lhs/lhs_standard.png", zoom=zoomNUm)
#shy
image lhs_shy_1 = Transform("characterImages/lhs/lhs_shy_1.png", zoom=zoomNUm)
image lhs_shy_2 = Transform("characterImages/lhs/lhs_shy_2.png", zoom=zoomNUm)
#shorked
image lhs_shorked_1 = Transform("characterImages/lhs/lhs_shorked_1.png", zoom=zoomNUm)
#sad
image lhs_sad_1 = Transform("characterImages/lhs/lhs_sad_1.png", zoom=zoomNUm)
image lhs_sad_2 = Transform("characterImages/lhs/lhs_sad_2.png", zoom=zoomNUm)
#angry
image lhs_angry_1 = Transform("characterImages/lhs/lhs_angry_1.png", zoom=zoomNUm)


# 정성경
define A = Character('???', color="#ffffff")
define jsk = Character('정성경', color="#fff42d")
#standard
image jsk_standard = Transform("characterImages/jsk/jsk_standard.png", zoom=zoomNUm)
#shy
image jsk_shy_1 = Transform("characterImages/jsk/jsk_shy_1.png", zoom=zoomNUm)
image jsk_shy_2 = Transform("characterImages/jsk/jsk_shy_2.png", zoom=zoomNUm)
image jsk_shy_3 = Transform("characterImages/jsk/jsk_shy_3.png", zoom=zoomNUm)
#shorked
image jsk_shorked_1 = Transform("characterImages/jsk/jsk_shorked_1.png", zoom=zoomNUm)
image jsk_shorked_2 = Transform("characterImages/jsk/jsk_shorked_2.png", zoom=zoomNUm)
#sad
image jsk_sad_1 = Transform("characterImages/jsk/jsk_sad_1.png", zoom=zoomNUm)
image jsk_sad_2 = Transform("characterImages/jsk/jsk_sad_2.png", zoom=zoomNUm)
#joke
image jsk_joke_1 = Transform("characterImages/jsk/jsk_joke_1.png", zoom=zoomNUm)
image jsk_joke_2 = Transform("characterImages/jsk/jsk_joke_2.png", zoom=zoomNUm)
image jsk_joke_3 = Transform("characterImages/jsk/jsk_joke_3.png", zoom=zoomNUm)
#angry
image jsk_angry_1 = Transform("characterImages/jsk/jsk_angry_1.png", zoom=zoomNUm)
image jsk_angry_2 = Transform("characterImages/jsk/jsk_angry_2.png", zoom=zoomNUm)
image jsk_angry_3 = Transform("characterImages/jsk/jsk_angry_3.png", zoom=zoomNUm)


# 김민수
define kms = Character('김민수', color="#199767")
#images

# Monika
define mnk = Character('Monika', color="#ec9aef")
#standard
image mnk_standard = Transform("characterImages/mnk/mnk_standard.png", zoom=zoomNUm)
image mnk_standard_2 = Transform("characterImages/mnk/mnk_standard_2.png", zoom=zoomNUm)
#shorked
image mnk_shorked_1 = Transform("characterImages/mnk/mnk_shorked_1.png", zoom=zoomNUm)
image mnk_shorked_2 = Transform("characterImages/mnk/mnk_shorked_2.png", zoom=zoomNUm)
image mnk_shorked_3 = Transform("characterImages/mnk/mnk_shorked_3.png", zoom=zoomNUm)
image mnk_shorked_4 = Transform("characterImages/mnk/mnk_shorked_4.png", zoom=zoomNUm)
#sad
image mnk_sad_1 = Transform("characterImages/mnk/mnk_sad_1.png", zoom=zoomNUm)
image mnk_sad_2 = Transform("characterImages/mnk/mnk_sad_2.png", zoom=zoomNUm)
image mnk_sad_3 = Transform("characterImages/mnk/mnk_sad_3.png", zoom=zoomNUm)
image mnk_sad_4 = Transform("characterImages/mnk/mnk_sad_4.png", zoom=zoomNUm)
#joke
image mnk_joke_1 = Transform("characterImages/mnk/mnk_joke_1.png", zoom=zoomNUm)
#angry
image mnk_angry_1 = Transform("characterImages/mnk/mnk_angry_1.png", zoom=zoomNUm)
image mnk_angry_2 = Transform("characterImages/mnk/mnk_angry_2.png", zoom=zoomNUm)
image mnk_angry_3 = Transform("characterImages/mnk/mnk_angry_3.png", zoom=zoomNUm)
image mnk_angry_4 = Transform("characterImages/mnk/mnk_angry_4.png", zoom=zoomNUm)
image mnk_angry_5 = Transform("characterImages/mnk/mnk_angry_5.png", zoom=zoomNUm)


#박여름
define pyr = Character('박여름', color="#000563")
#standard
image pyr_standard = Transform("characterImages/pyr_standard.png", zoom=zoomNUm)
#shy
image pyr_shy_1 = Transform("characterImages/pyr/pyr_shy_1.png", zoom=zoomNUm)
image pyr_shy_2 = Transform("characterImages/pyr/pyr_shy_2.png", zoom=zoomNUm)
image pyr_shy_3 = Transform("characterImages/pyr/pyr_shy_3.png", zoom=zoomNUm)
image pyr_shy_4 = Transform("characterImages/pyr/pyr_shy_4.png", zoom=zoomNUm)
#shorked
image pyr_shorkd_1 = Transform("characterImages/pyr/pyr_shorked_1.png", zoom=zoomNUm)
image pyr_shorkd_2 = Transform("characterImages/pyr/pyr_shorked_2.png", zoom=zoomNUm)
#sad
image pyr_sad_1 = Transform("characterImages/pyr/pyr_sad_1.png", zoom=zoomNUm)
image pyr_sad_2 = Transform("characterImages/pyr/pyr_sad_2.png", zoom=zoomNUm)
image pyr_sad_3 = Transform("characterImages/pyr/pyr_sad_3.png", zoom=zoomNUm)
image pyr_sad_4 = Transform("characterImages/pyr/pyr_sad_4.png", zoom=zoomNUm)
#joke
image pyr_joke_1 = Transform("characterImages/pyr/pyr_joke_1.png", zoom=zoomNUm)
#angry
image pyr_angry_1 = Transform("characterImages/pyr/pyr_angry_1.png", zoom=zoomNUm)
image pyr_angry_2 = Transform("characterImages/pyr/pyr_angry_2.png", zoom=zoomNUm)
image pyr_angry_3 = Transform("characterImages/pyr/pyr_angry_3.png", zoom=zoomNUm)
image pyr_angry_4 = Transform("characterImages/pyr/pyr_angry_4.png", zoom=zoomNUm)
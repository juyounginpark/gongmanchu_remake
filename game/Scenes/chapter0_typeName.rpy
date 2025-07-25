screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5
            
label typeName:
    $ name = renpy.call_screen("set_name", title="내 이름이 뭐였지?", init_name="이름 입력")
    $ main = Character(name, color="#0c0808")
    jump chapter1
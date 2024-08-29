from tkinter import *
import os
from style import *


def center_window():
    """
    Sets window properties and centers based on screen width/height.
    """
    window = Tk()
    window.title("Taş Kağıt Makas v1")
    window.resizable(width=False, height=False)

    window.update_idletasks()
    window_width = 1200
    window_height = 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    return window


def switch_frame(current_frame, next_frame):
    """
    Switches between pages.
    Inputs: It takes current frame (whichever page is on) and next frame (page after current page).
    """
    current_frame.pack_forget()
    next_frame.pack(fill=BOTH, expand=True)


def setup_welcome(frame, next_frame):
    """
    Setups features for greetings frame.
    Inputs: It takes current frame (welcome page) and next_frame (a page following welcome page).
    """
    def on_return(event=None):
        """
        Checks whether return pressed.
        Outputs: If return pressed, switch page.
        """
        switch_frame(frame, next_frame)

    ascii_welcome = writing_rock_scissors_paper['rock_paper_scissors_ascii']
    welcome_ascii = Label(frame, text=ascii_welcome, font=("Courier", 10), justify="center")
    welcome_ascii.pack(pady=10)

    welcome_text = Label(frame, text=f"Taş - Kağıt - Makas v1 Oyununa Hoşgeldin! (●'◡'●){new_line}"
                                     f"Klasik oyun modu ile maziyi hatırlarken\n yeni tasarlanmış oyun modlarıyla farklı "
                                     f"bir dünyaya adım atacaksın!{new_line_short}"
                                     f"Önce oyun modları tanıtılacak ve daha sonra oyuna başlayacaksın.{new_line_short}")
    welcome_text.config(font=("Courier", 14, "bold"), fg="black", justify="center")
    welcome_text.pack(pady=10)

    welcome_text_note = Label(frame, text=f"<ENTER tuşuyla ilerle>{new_line}Not: Herhangi bir nedenden ötürü oyunu kapatmak istesersen ESC tuşuna basmalısın.")
    welcome_text_note.config(font=("Courier", 14, "italic"), fg="black", justify="center")
    welcome_text_note.pack(pady=10)

    frame.bind('<Return>', on_return)
    frame.focus_set()


def setup_instructions_1(frame, next_frame):
    """
    Setups features for first instructions page.
    Inputs: It takes current frame (instructions page) and next_frame (a page following welcome page).
    """
    label = Label(frame, text="", font=("Courier", 14, "normal"), justify="center")
    label.pack(pady=10)

    klasik = ASCII['klasik']

    texts = [f"Oyunda karşınıza rastgele gelebilecek 3 oyun modu vardır...{new_line_short}",
                  f"{klasik}{new_line_short}",
                  f"{multiple_stars} Klasik Oyun Modu {multiple_stars}{new_line_short}",
                  f"Herkes tarafından yüzyıllardır bilinen oyun modu.{new_line_short}",
                  f"Taş, Kağıt ya da Makas yazarak rakibini alt et.{new_line_short}",
                  f"Olasılıklar şunlardır:{new_line_short}",
                  f"▪ Kağıt 🞂 Taş 🞬 {new_line_short}",
                  f"▪ Makas 🞂 Kağıt 🞬 {new_line_short}",
                  f"▪ Taş 🞂 Makas 🞬 {new_line_short}"
            ]

    instant_writer(label, texts, frame)

    next_button = Button(frame, text="Sonraki")
    next_button.config(font=("Courier", 12, "italic"), width=10, height=2,
                       command=lambda: switch_frame(frame, next_frame))
    next_button.place(x=550, y=600)


def setup_instructions_2(frame, prev_frame, next_frame):
    """
    Setups features for second instructions page.
    Inputs: It takes current frame (second instructions page), next frame (page following current page) and previous frame (page before current page).
    """
    label = Label(frame, text="", font=("Courier", 14, "normal"), justify="center")
    label.pack(pady=10)

    karma = ASCII['karma']

    texts = [f"{space}{karma}{space}{new_line_short}",
              f"{multiple_stars} Karma Eller Modu {multiple_stars}{new_line_short}",
              f"Yeni bir soluk getirmek için tasarlandı.{new_line_short}",
              f"Taş, Kağıt ya da Makas yazarak rakibini (kendini??) alt et.{new_line_short}",
              f"Bu modda sen bot için bot da senin için elini seçer!{new_line_short}",
              f"Olasılıklar şunlardır:{new_line_short}",
              f"▪ Sen: Taş 🞂 Bot: Kağıt {multi_dots} 🞬 Kazanan Sen 🞬{new_line_short}",
              f"▪ Sen: Kağıt 🞂 Bot: Makas {multi_dots} 🞬 Kazanan Sen 🞬{new_line_short}",
              f"▪ Sen: Makas 🞂 Bot: Kağıt {multi_dots} 🞬 Kazanan Bot 🞬{new_line_short}"
             ]

    instant_writer(label, texts, frame)

    next_button = Button(frame, text="Sonraki", font=("Courier", 12, "italic"), width=10, height=2,
                         command=lambda: switch_frame(frame, next_frame))
    next_button.place(x=650, y=600)

    prev_button = Button(frame, text="Önceki", font=("Courier", 12, "italic"), width=10, height=2,
                         command=lambda: switch_frame(frame, prev_frame))
    prev_button.place(x=450, y=600)


def setup_instructions_3(frame, prev_frame):
    """
    Setups features for third instructions page.
    Inputs: It takes current frame (third instructions page) and previous frame (page before current page).
    """
    label = Label(frame, text="", font=("Courier", 14, "normal"), justify="center")
    label.pack(pady=10)

    kahin = ASCII['kahin']

    texts = [f"{space}{kahin}{space}{new_line_short}",
              f"{multiple_stars} Kâhin Modu {multiple_stars}{new_line_short}",
              f"Ben... Ben Kâhin! ༼ つ ◕_◕ ༽つ{new_line_short}",
              f"Ne taş, ne kağıt, ne de makas konusunda söz hakkına sahipsin!{new_line_short}",
              f"Bu modda kimin kazanıp kimin kaybedeceğine ben karar veririm (╯°□°）╯{new_line_short}",
              f"Ellerin hepsini Kâhin seçer:{new_line_short}",
              f"▪ Kâhin (Sen): Taş 🞂 Kâhin (Bot): Kağıt {multi_dots} 🞬 Kazanan Bot 🞬{new_line_short}",
              f"▪ Kâhin (Sen): Kağıt 🞂 Kâhin (Bot): Makas {multi_dots} 🞬 Kazanan Bot 🞬{new_line_short}",
              f"▪ Kâhin (Sen): Makas 🞂 Kâhin (Bot): Kağıt {multi_dots} 🞬 Kazanan Sen 🞬{new_line_short}"
             ]

    instant_writer(label, texts, frame)

    # this is the last instruction page, therefore, starts the game after click
    global finish_button
    finish_button = Button(frame, text="Başla", font=("Courier", 13, "bold"), fg="green", width=10, height=2,
                           command=lambda: start_main_game(frame))
    finish_button.place(x=650, y=600)
    finish_button.config(state=DISABLED)  # initially disable until writing is done
    # returns previous page
    prev_button = Button(frame, text="Önceki", font=("Courier", 12, "italic"), width=10, height=2,
                         command=lambda: switch_frame(frame, prev_frame))
    prev_button.place(x=450, y=600)


def start_main_game(frame):
    """
    Destroys instructions window and opens game screen.
    """
    frame.destroy()
    window.destroy()
    os.system('python main_game.py')


def instant_writer(label, texts, frame, text_index=0, char_index=0):
    """
    Rather than directly presenting texts, it creates typewriter effect.
    """
    if text_index < len(texts):
        text = texts[text_index]
        if char_index < len(text):
            label.config(text=label.cget("text") + text[char_index], justify="center")
            char_index += 1
            window.after(20, instant_writer, label, texts, frame, text_index, char_index)
        else:
            window.after(500, instant_writer, label, texts, frame, text_index + 1, 0)
    else:
        # after writing is complete, enable the "Başla" button
        finish_button.config(state=NORMAL)


def window_exit(event=None):
    """
    Inputs: Escape key.
    Outputs: Quits game regardless of status.
    """
    window.destroy()


def tas_kagit_makas_NAZIF_KARACA():
    global window

    window = center_window()
    window.bind('<Escape>', window_exit)
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=True)


    # initialize frames for each instruction page
    welcome = Frame(main_frame)
    instructions_1 = Frame(main_frame)
    instructions_2 = Frame(main_frame)
    instructions_3 = Frame(main_frame)

    # set up each page
    setup_welcome(welcome, instructions_1)
    setup_instructions_1(instructions_1, instructions_2)
    setup_instructions_2(instructions_2, instructions_1, instructions_3)
    setup_instructions_3(instructions_3, instructions_2)

    welcome.pack(fill=BOTH, expand=True)  # starts with welcome page

    window.mainloop()


if __name__ == "__main__":
    tas_kagit_makas_NAZIF_KARACA()
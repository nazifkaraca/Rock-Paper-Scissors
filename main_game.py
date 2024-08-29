from tkinter import *
from tkinter import messagebox
import random
from style import *


def center_window():
    """
    Sets window properties and centers based on screen width/height.
    """
    window = Tk()
    window.title("Taş Kağıt Makas v1")
    window.resizable(width=False, height=False)

    window.update_idletasks()
    window_width = 1200 # x
    window_height = 700 # y
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    return window


def update_ascii_art(user_choice, bot_choice):
    """
    Updates hands (depicting rock/scissors/paper) based on game mode.
    """
    if selected_text.startswith("Bot için tercihini yap."):

        user_ascii_label.config(text=ascii_rock_scissors_paper[user_choice])
        bot_ascii_label.config(text=ascii_rock_scissors_paper[bot_choice])
        user_hand_label.config(text="Sen\nBotun Seçimi:")
        bot_hand_label.config(text="Bot\nSenin Seçimin:")
    else:

        user_ascii_label.config(text=ascii_rock_scissors_paper[user_choice])
        bot_ascii_label.config(text=ascii_rock_scissors_paper[bot_choice])
        user_hand_label.config(text="Senin Seçimin:")
        bot_hand_label.config(text="Botun Seçimi:")


def game_choicer():
    """
    It randomly selects game mode.
    Outputs: It prints selected game mode text.
    """
    global user_answer
    global selected_text

    texts= [('Tercihin nedir?\nAşağıdaki kutucuğuna Taş, Kağıt ya da Makas yaz ve ENTER tuşuna tıkla!', True, 'klasik'),
            ('Bot için tercihini yap.\n Taş, Kağıt ya da Makas... ENTER ile geç!', True, 'karma'),
            ('HO HO HO! Kahin geri döndü...\n SEÇİM SIRASI BENDE ༼ つ ◕_◕ ༽つ', False, 'kahin')]

    selected_text, show_input, game_mode = random.choice(texts)

    # setting texts to present
    page1 = Frame(main_frame)
    game_title = Label(page1, text=ASCII[game_mode], font=("Courier", 16, "bold"))
    game_title.pack(side=TOP, fill=X)
    page_1_lb = Label(page1, text=selected_text, font=("Courier", 16, "bold"))
    page_1_lb.pack(pady=20)

    if show_input:
        user_answer = Entry(page1, font=('arial', 15, 'bold'), width=15)
        user_answer.pack(pady=20)
    else:
        user_answer = None

    # if 'kahin' mode selected, rather than waiting user event, skip page automatically after 3 secs.
    if selected_text.startswith("HO HO HO!"):
        window.after(3000, move_next_page)

    page1.pack(expand=True)
    return page1


def choices():
    """
    Gets user choice and randomly selects bot choice.
    """
    choices = ['taş', 'kağıt', 'makas']
    bot_answer = random.choice(choices)
    bot_answer_for_user = random.choice(choices)
    if selected_text.startswith('Bot için tercihini yap.'):
        user_input = bot_answer
        bot_input = user_answer.get()
    elif selected_text.startswith('HO HO HO!'):
        user_input = bot_answer_for_user
        bot_input = bot_answer
    else:
        user_input = user_answer.get()
        bot_input = bot_answer
    return user_input, bot_input


def compare_answers(user_input, bot_input):
    """
    Compares user and bot choices and returns result text.
    """
    global user_score, bot_score, roundd, winner_color

    cases = {'taş': 'makas',
             'kağıt': 'taş',
             'makas': 'kağıt'}

    if cases.get(user_input) == bot_input:
        result = "Tüh! Sen kazandın..."
        result_label.config(fg="green")
        user_score += 1
    elif cases.get(bot_input) == user_input:
        result = "Hahahah kolaydı (☞ﾟヮﾟ)☞"
        result_label.config(fg="red")
        bot_score += 1
    else:
        result = ("Bir dahaki sefere görüşürüz...\n"
                  "     Berabere...")
        result_label.config(fg="black")


    if user_score == 2 or bot_score == 2:
        determine_winner()
    else:
        roundd += 1
        update_info_labels()

    return result


def determine_winner():
    """
    Main determination for winner. 
    """
    global game, user_score, bot_score, roundd, user_game_wins, bot_game_wins

    if user_score == 2:
        winner = "Sen"
        user_game_wins += 1
    else:
        winner = "Bot"
        bot_game_wins += 1

    pages[count].pack_forget()
    pages[1].pack(expand=True)  # Show the result page
    window.update()

    window.after(1500, lambda: show_winner_popup(winner))


def show_winner_popup(winner):
    """
    Shows popup based on winner.
    """
    messagebox.showinfo("Oyun Bitti", f"{game}. Oyunun Kazananı: {winner}")
    window.after(500, ask_for_continuation)


def move_next_page(event=None):
    """
    Skips between input and result pages based on conditions.
    """
    global count

    if count == 0:
        if user_answer is not None and not check_answer():
            return

        user_input, bot_input = choices()

        update_ascii_art(user_input.lower(), bot_input)

        result_status = compare_answers(user_input.lower(), bot_input)
        result_label.config(text=f"\nSonuç: {result_status}")

    if count < len(pages) - 1:
        pages[count].pack_forget()
        count += 1
        pages[count].pack(expand=True)

        if count == 1 and user_score < 2 and bot_score < 2:
            window.after(3000, loop_pages)


def loop_pages():
    """
    Loops input and result pages automatically.
    """
    global count
    pages[count].pack_forget()
    count = 0
    pages[0] = game_choicer()  # Reinitialize the first page
    pages[count].pack(expand=True)


def check_answer():
    """
    Checks whether user input contains rock, paper or scissors.
    """
    entry_text = user_answer.get()
    if entry_text.lower() not in ["taş", "kağıt", "makas"]:
        messagebox.showerror("(T_T)", "         Kendine gelmeye ne dersin?\n"
                                      "TAŞ, KAĞIT YA DA MAKAS YAZACAKSIN!!!\n"
                                      "                     ( •_•)>⌐■-■")
        user_answer.delete(0, END)
        return False
    return True


def update_info_labels():
    """
    Round score, game, round, and general score are being updated.
    """
    game_label.config(text=f"Oyun: {game} || Round: {roundd}")
    user_score_label.config(text=f"Sen: {user_score}")
    bot_score_label.config(text=f"Bot: {bot_score}")
    global_score_label.config(text=f"Genel Skor\nSen: {user_game_wins} || Bot: {bot_game_wins}")


def ask_for_continuation():
    """
    After first two points, it asks both user and bot to continue.
    """
    bot_continue = random.choice([True, False])

    user_continue = messagebox.askyesno("Kaybetmek İstersen Evet De (¬‿¬)", "Yeniden oynayalım mı?")

    if user_continue and bot_continue:
        start_new_game()
    else:
        end_game(user_continue, bot_continue)


def start_new_game():
    """
    If both willing to continue, starts new game.
    """
    global game, roundd, user_score, bot_score

    game += 1
    messagebox.showinfo("Ben de devam edeceğim...", f"{game}. oyun başlasın o halde!")

    roundd = 0
    user_score = 0
    bot_score = 0
    update_info_labels()

    pages[1].pack_forget()

    loop_pages()


def end_game(user_continue, bot_continue):
    """
    If one of the sides decide to quit, show who wins and quits game.
    """
    if user_game_wins > bot_game_wins:
        overall_winner = "Maalesef kazanan Sen oldun..."
    elif user_game_wins < bot_game_wins:
        overall_winner = "Hahahaha kolaydı... Ben kazandım!"
    else:
        overall_winner = "Berabere kaldık."

    if not user_continue:
        messagebox.showinfo("Topukların Arşa Değiyor...",
                            f"Kaç bakalım ( ´･･)ﾉ(._.`)\n"
                            f"Oyun bitti... {overall_winner}!")
        window.after(100, window.destroy)
    elif not bot_continue:
        messagebox.showinfo("Bir Daha Görüşeceğiz!",
                            f"Oyun bitti... {overall_winner}!\n"
                            f"{space}")
        window.after(100, window.destroy)
    else:
        start_new_game()


def setup_page1():
    """
    Setups first page in which user enters input.
    """
    global global_score_label, user_score_label, bot_score_label, game_label

    info_frame_top = Frame(window)
    info_frame_bottom = Frame(window)
    info_frame_top.pack(side=TOP, pady=10, fill=X)
    info_frame_bottom.pack(side=BOTTOM, pady=10, fill=X)

    global_score_label = Label(info_frame_top, text=f"Genel Skor\nSen: {user_game_wins} || Bot: {bot_game_wins}",
                            font=("Courier", 14, "bold"), fg="blue")
    global_score_label.pack(anchor=CENTER)

    score_frame = Frame(info_frame_bottom)
    score_frame.pack(side=TOP, pady=5)
    user_score_label = Label(score_frame, text=f"Sen: {user_score}", font=("Courier", 14, "bold"))
    user_score_label.grid(row=0, column=0, padx=20)

    bot_score_label = Label(score_frame, text=f"Bot: {bot_score}", font=("Courier", 14, "bold"))
    bot_score_label.grid(row=0, column=1, padx=20)

    game_frame = Frame(info_frame_bottom)
    game_frame.pack(side=BOTTOM, pady=5)
    game_label = Label(game_frame, text=f"Oyun: {game} || Round: {roundd}", font=("Courier", 14, "italic"), fg="red")

    game_label.grid(row=1, column=0, padx=10)
    main_frame.pack(fill=BOTH, expand=True)


def setup_page2():
    """
    Setups user and bot choices (rock-paper-scissors) and shows result.
    """
    global page2, user_hand_label, user_ascii_label, bot_hand_label, bot_ascii_label
    global user_input_label, bot_input_label, result_label
    # set main frame for page 2
    page2 = Frame(main_frame)
    page2.pack(expand=True)
    
    ascii_frame= Frame(page2)
    ascii_frame.pack(pady=20)
    # show labels for which decision is whose and put ascii below them
    user_hand_label = Label(ascii_frame, text="", font=("Courier", 16, "bold"), justify=CENTER)
    user_ascii_label = Label(ascii_frame, text="", font=("Courier", 12), justify=CENTER)
    bot_hand_label = Label(ascii_frame, text="", font=("Courier", 16, "bold"), justify=CENTER)
    bot_ascii_label = Label(ascii_frame, text="", font=("Courier", 12), justify=CENTER)
    
    user_input_label = Label(ascii_frame, text="", font=("Courier", 16, "bold"))
    bot_input_label = Label(ascii_frame, text="", font=("Courier", 16, "bold"))
    result_label = Label(ascii_frame, text="", font=("Courier", 16, "bold"), justify=CENTER, wraplength=800)

    user_hand_label.grid(row=0, column=0, padx=50)
    user_ascii_label.grid(row=1, column=0, padx=50)
    bot_hand_label.grid(row=0, column=1, padx=50)
    bot_ascii_label.grid(row=1, column=1, padx=50)

    user_input_label.grid(row=2, column=0, columnspan=2, pady=10)
    bot_input_label.grid(row=3, column=0, columnspan=2, pady=10)
    result_label.grid(row=4, column=0, columnspan=2, pady=10)


def window_exit(event=None):
    """
    Escape key quits game.
    """
    window.destroy()

game = 1
roundd = 0
user_score = 0
bot_score = 0
user_game_wins = 0
bot_game_wins = 0
count = 0

window = center_window()
window.bind('<Return>', move_next_page)
window.bind('<Escape>', window_exit)
main_frame = Frame(window)

setup_page1()

setup_page2()

pages = [game_choicer(), page2]

page2.pack_forget()

window.mainloop()
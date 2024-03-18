import tkinter as tk

def show_notification():
    # 새로운 윈도우(알림창) 생성
    top = tk.Toplevel(root)
    top.title("허리 피자")
    top.iconbitmap('pizza.ico')

    # 알림창 크기 및 화면 중앙에 위치시키기
    window_width = 300
    window_height = 150
    screen_width = 1920
    screen_height = 1080
    center_x = int((screen_width / 2) - (window_width / 2))
    center_y = int((screen_height / 2) - (window_height / 2))
    top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # 메시지 표시
    message = tk.Label(top, text="바로 앉아주세요!", height=4)
    message.pack()

    # '확인' 버튼: 알림창을 닫고 5분 후 다시 알림을 표시
    continue_button = tk.Button(top, text="확인", command=lambda: [top.destroy(), root.after(300000, show_notification)])
    continue_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=5)

    # '중단' 버튼: 프로그램 종료
    stop_button = tk.Button(top, text="중단", command=lambda: [root.destroy()])
    stop_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=20, pady=5)

# Tkinter 윈도우 생성 및 초기 설정
root = tk.Tk()
root.withdraw()
root.iconbitmap('pizza.ico')

# 프로그램 시작 시 첫 알림 바로 실행
show_notification()

# Tkinter 이벤트 루프 시작
root.mainloop()

import tkinter as tk
from tkinter import messagebox, filedialog
import glab
import threading

G = False


def load_file_and_create_graph():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            global G
            text = glab.read_file(file_path)
            words = glab.process_text(text)
            G = glab.create_graph(words)
            messagebox.showinfo("Success", "Graph created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create graph: {e}")


def show_graph():
    if not G:
        messagebox.showinfo("Error", f"To begin, please load a file.")
        return
    glab.showDirectedGraph(G)


def query_bridge_words():
    if not G:
        messagebox.showinfo("Error", f"To begin, please load a file.")
        return
    # 使用 nonlocal 关键字来声明变量
    word1, word2 = "", ""

    def on_ok():
        # 使用 nonlocal 关键字来修改变量
        nonlocal word1, word2
        word1 = entry_word1.get().strip()
        word2 = entry_word2.get().strip()
        top.destroy()

    parent_x = root.winfo_x()
    parent_y = root.winfo_y()
    parent_width = root.winfo_width()

    # 计算 Toplevel 窗口的位置，使其位于主窗口的中心
    width = 230  # 设置 Toplevel 窗口的宽度
    height = 110  # 设置 Toplevel 窗口的高度
    x = parent_x + (parent_width - width) // 2
    y = parent_y + (root.winfo_height() - height) // 2

    # 创建 Toplevel 窗口，并设置其大小和位置
    top = tk.Toplevel(root)
    top.title("Enter Word1 and Word2")
    top.geometry(f"{width}x{height}+{x}+{y}")

    label_word1 = tk.Label(top, text="Word 1:")
    label_word1.grid(row=0, column=0, padx=5, pady=5)
    entry_word1 = tk.Entry(top)
    entry_word1.insert(0, "to")
    entry_word1.grid(row=0, column=1, padx=5, pady=5)

    label_word2 = tk.Label(top, text="Word 2:")
    label_word2.grid(row=1, column=0, padx=5, pady=5)
    entry_word2 = tk.Entry(top)
    entry_word2.insert(0, "out")
    entry_word2.grid(row=1, column=1, padx=5, pady=5)

    button_ok = tk.Button(top, text="OK", command=on_ok)
    button_ok.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    top.transient(root)  # 使对话框模式为模态
    top.grab_set()  # 禁用主窗口直到对话框关闭
    top.wait_window()  # 等待对话框关闭

    if word1 and word2:
        bridge_word = glab.find_bridge_words(G, word1, word2)
        if bridge_word:
            messagebox.showinfo("Bridge Word", f"The bridge word from {word1} to {word2} is: {bridge_word}")
        else:
            messagebox.showinfo("Bridge Word", f"No bridge words from {word1} to {word2}!")
    else:
        messagebox.showwarning("Input Error", "Please enter both word1 and word2.")


def generate_new_text():
    if not G:
        messagebox.showinfo("Error", "To begin, please load a file.")
        return

    # 创建 Toplevel 窗口，并设置其大小和位置
    top = tk.Toplevel(root)
    top.title("Generate New Text")

    entry_new_text = tk.Text(top, wrap="word", width=40, height=8)
    entry_new_text.insert(tk.END, "Seek to explore new and exciting synergies")
    entry_new_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    def on_ok():
        new_text = entry_new_text.get("1.0", "end-1c").strip()
        if new_text:
            generated_text = glab.generateNewText(G, new_text)
            messagebox.showinfo("New Text Generated", f"Input: {new_text}\nGenerated: {generated_text}")
        else:
            messagebox.showwarning("Input Error", "Please enter a text or select a file.")
        top.destroy()

    def select_file():
        top.destroy()
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    new_text = file.read()
                    if new_text:
                        generated_text = glab.generateNewText(G, new_text)
                        messagebox.showinfo("New Text Generated", f"Input: {new_text}\nGenerated: {generated_text}")
                    else:
                        messagebox.showwarning("Input Error", "Please enter a text or select a file.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file: {e}")

    sub_button_frame = tk.Frame(top, relief="groove")

    # 设置 Frame 的布局和背景颜色
    sub_button_frame.grid(row=1, column=0)

    button_select_file = tk.Button(sub_button_frame, text="Select File", command=select_file)
    button_select_file.config(width=8, height=1)  # 这些值可以根据需要调整
    button_select_file.grid(row=0, column=0, padx=5, pady=5)

    button_ok = tk.Button(sub_button_frame, text="OK", command=on_ok)
    button_ok.config(width=8, height=1)  # 这些值应该与上面的按钮一致，以保持大小统一
    button_ok.grid(row=0, column=1, padx=5, pady=5, columnspan=2)


def calculate_shortest_path():
    if not G:
        messagebox.showinfo("Error", f"To begin, please load a file.")
        return
    if not G:
        messagebox.showinfo("Error", f"To begin, please load a file.")
        return
    # 使用 nonlocal 关键字来声明变量
    word1, word2 = "", ""

    def on_ok():
        # 使用 nonlocal 关键字来修改变量
        nonlocal word1, word2
        word1 = entry_word1.get().strip()
        word2 = entry_word2.get().strip()
        top.destroy()

    parent_x = root.winfo_x()
    parent_y = root.winfo_y()
    parent_width = root.winfo_width()

    # 计算 Toplevel 窗口的位置，使其位于主窗口的中心
    width = 230  # 设置 Toplevel 窗口的宽度
    height = 110  # 设置 Toplevel 窗口的高度
    x = parent_x + (parent_width - width) // 2
    y = parent_y + (root.winfo_height() - height) // 2

    # 创建 Toplevel 窗口，并设置其大小和位置
    top = tk.Toplevel(root)
    top.title("Enter Word1 and Word2")
    top.geometry(f"{width}x{height}+{x}+{y}")

    label_word1 = tk.Label(top, text="Word 1:")
    label_word1.grid(row=0, column=0, padx=5, pady=5)
    entry_word1 = tk.Entry(top)
    entry_word1.insert(0, "to")
    entry_word1.grid(row=0, column=1, padx=5, pady=5)

    label_word2 = tk.Label(top, text="Word 2:")
    label_word2.grid(row=1, column=0, padx=5, pady=5)
    entry_word2 = tk.Entry(top)
    entry_word2.insert(0, "out")
    entry_word2.grid(row=1, column=1, padx=5, pady=5)

    button_ok = tk.Button(top, text="OK", command=on_ok)
    button_ok.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    top.transient(root)  # 使对话框模式为模态
    top.grab_set()  # 禁用主窗口直到对话框关闭
    top.wait_window()  # 等待对话框关闭
    if word1 and word2:
        path = glab.calcShortestPath(G, word1, word2)
        if path:
            messagebox.showinfo("Shortest Path", f"The shortest path from {word1} to {word2} is: {path}")
        else:
            messagebox.showinfo("Shortest Path", f"No path from {word1} to {word2}!")


# 全局变量，用于控制随机游走的停止
stop_event = threading.Event()


def random_walk():
    global stop_event  # 声明为全局变量以便在停止函数中访问
    if not G:
        messagebox.showinfo("Error", "To begin, please load a file.")
        return
    try:
        stop_event.clear()  # 重置停止事件
        top = tk.Toplevel(root)
        text_random_walk = tk.Text(top, wrap="word")
        text_random_walk.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # 按钮用于启动随机游走
        def on_start():
            stop_event.clear()
            # 启动随机游走的线程
            random_walk_thread = threading.Thread(target=glab.randomWalk, args=(G, text_random_walk, stop_event))
            random_walk_thread.start()

        sub_button_frame = tk.Frame(top, relief="groove")

        # 设置 Frame 的布局和背景颜色
        sub_button_frame.grid(row=1, column=0)
        button_start = tk.Button(sub_button_frame, text="Start", command=on_start)
        button_start.config(width=8, height=1)
        button_start.grid(row=0, column=0, padx=5, pady=5)

        # 按钮用于停止随机游走
        def on_stop():
            stop_event.set()  # 设置停止事件

        button_stop = tk.Button(sub_button_frame, text="Stop", command=on_stop)
        button_stop.config(width=8, height=1)
        button_stop.grid(row=0, column=1, padx=5, pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"Failed during random walk: {e}")


# 设置窗口标题
root = tk.Tk()
root.title("Text Graphing Tool")

# 设置窗口的背景颜色
root.config(bg="white")

# 设置窗口的最小尺寸
root.minsize(600, 200)
# 添加一个大标题
title = tk.Label(root, text="Text Graphing Tool", font=("Helvetica", 20, "bold"), bg="white")
title.pack(fill="x", pady=(20, 5))  # 使标题填满x轴，上下各有20和5像素的填充

# 创建一个 Frame 用于放置按钮，使用相对布局
button_frame = tk.Frame(root, bg="white", borderwidth=2, relief="groove")

# 设置 Frame 的布局和背景颜色
button_frame.pack(pady=(0, 10))

# 设置按钮的统一样式
button_style = dict(font=("Helvetica", 12), bg="#d0d0d0", fg="#303030",
                    relief="raised", padx=10, pady=5, compound="center")

# 设置按钮的统一大小
button_width = 20  # 设置一个固定宽度
button_height = 2  # 设置一个固定高度

# 创建按钮列表并添加到 Frame 中
buttons = [
    ("Select File", load_file_and_create_graph),
    ("Show Graph", show_graph),
    ("Query Bridge Words", query_bridge_words),
    ("Generate New Text", generate_new_text),
    ("Calculate Shortest Path", calculate_shortest_path),
    ("Random Walk", random_walk)
]

for i, (btn_text, btn_function) in enumerate(buttons):
    btn = tk.Button(button_frame, text=btn_text, command=btn_function, **button_style)
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")

# 运行 GUI 事件循环
root.mainloop()

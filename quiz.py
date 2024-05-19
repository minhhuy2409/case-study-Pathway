print("chào mừng bạn đến với AI LÀ TRIỆU PHÚ")
print("luật chơi như sau:")
print("Bạn trả lời đúng đáp án bạn sẽ được 100k từ câu 1 đến 4, 200k từ 5 đến 7 và 300k từ 8 đến 10")
print("Bạn sẽ có 4 quyền trợ giúp là: hỏi ý khán giả, 50 50 và 2 gợi ý đáp án")

import random

# Danh sách các câu hỏi và đáp án
questions1 = [
    {
        "question": "1) Loại hoa nào được coi là biểu tượng của sự đẹp đẽ và tinh khiết?",
        "options": ["A. hoa hồng", "B. hoa sen", "C. hoa cúc", "D. hoa lan"],
        "answer": "B",
        "wrong": "A",
        "hint": "Hoa có hình dạng bầu bĩnh ở phần thân, vuốt tròn theo hướng từ dưới lên trên.",


    },
    {
        "question": "2) Câu lệnh nào dùng để hiển thị dữ liệu ra màn hình trong Python?",
        "options": ["A. print()", "B. cout<<", "C. System.out.printin()", "D. echo"],
        "answer": "A",
        "wrong": "C",

    },
    {
        "question": "3) Loài động vật nào là biểu tượng của sự kiên nhẫn và sức mạnh trong văn hóa Phương Tây?",
        "options": ["A. Sư tử", "B. Hổ", "C. Rồng", "D. Voi"],
        "answer": "B",
        "wrong": "A",
        "hint": "Loài này là một loài động vật có vú thuộc họ Mèo.",

    },
    {
        "question": "4) Quốc gia nào là nơi nổi tiếng với văn hóa Samba và Carnival?",
        "options": ["A. Argentina", "B. Brazil", "C. Mexico", "D. Colombia"],
        "answer": "B",
        "wrong": "A",
        "hint": "Quốc gia này có diện tích lớn thứ 5 thế giới.",


    },
]
questions2 = [

    {
        "question": "5) Python được phát hành vào năm nào?",
        "options": ["A. 1991", "B. 1989", "C. 1985", "D. 1995"],
        "answer": "A",
        "wrong": "B",
        "hint": "Python được phát hành vào những năm 80.",
    },   
    {
        "question": "6) Ai là người phát minh ra máy tính đầu tiên trên thế giới?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. Ada Lovelace", "D. John von Neumann"],
        "answer": "A",
        "wrong": "B",
        "hint": "Ông là một nhà toán học, nhà triết học, nhà phát minh và kỹ sư cơ khí người Anh.",
    },
    {
        "question": "7) Ai là nhà triết học Hy Lạp nổi tiếng đã viết cuốn sách Chính Trị?",
        "options": ["A. Socrates", "B. Plato", "C. Aristotle", "D. Heraclitus"],
        "answer": "C",
        "wrong": "A",
        "hint": "Ông được xem là người đặt nền móng cho môn luận lý học.",

    },
]
questions3 = [

    {
        "question": "8) Ai là tác giả của cuốn tiểu thuyết Mười Nghìn Dặm Dưới Biển?",
        "options": ["A. Jules Verne", "B. H.G. Wells", "C. George Orwell", "D. Mark Twain"],
        "answer": "A",
        "wrong": "B",
        "hint": "Ông là một tiểu thuyết gia, nhà soạn kịch và nhà thơ Pháp.",

    },
    {
        "question": "9) Trong lịch sử, ai là người phụ nữ đầu tiên được công nhận là bác sĩ tại Hoa Kỳ vào thế kỷ 19?",
        "options": ["A. Elizabeth Blackwell", "B. Mary Edwards Walker", "C. Clara Barton", "D. Margaret Sanger"],
        "answer": "A",
        "wrong": "C",
    },
    {
        "question": "10) Trong thế kỷ 19, nhà văn nào viết tiểu thuyết đầu tiên trong lịch sử được viết bằng máy đánh chữ?",
        "options": ["A. Jules Verne", "B. H.G. Wells", "C. Leo Tolstoy", "D. Mark Twain"],
        "answer": "D",
        "wrong": "B",
        "hint": "Tên thật của ông là Samuel Langhorne Clemens.",
        
    },
]

money = 0

helps = {
    "ask_audience": True,
    "fifty_fifty": True,
    "hint": True,
}

# Hỏi ý kiến khán giả
def ask_audience(question):
    print("Ý kiến khán giả cho rằng đáp án đúng là: " + question["wrong"])

# 50:50
def fifty_fifty(question):
    print("Sau khi loại bỏ hai phương án sai, ta còn lại:")
    correct = question["answer"]
    options = [opt for opt in question["options"] if opt.startswith(correct)]
    incorrect = random.choice([opt for opt in question["options"] if not opt.startswith(correct)])
    print(options[0])
    print(incorrect)

# Gợi ý
def hint(question):
    print("Gợi ý: " + question["hint"])

def get_valid_input(prompt, valid_options):
    user_input = input(prompt).upper()
    while user_input not in valid_options:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        user_input = input(prompt).upper()
    return user_input

def play_game(questions, helps, prize):
    global money
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        use_help = get_valid_input("Bạn có muốn sử dụng trợ giúp không? (yes/no): ", ["YES", "NO"])
        if use_help == "YES":
            if helps["ask_audience"]:
                ask_audience(question)
                helps["ask_audience"] = False
            elif helps["fifty_fifty"]:
                fifty_fifty(question)
                helps["fifty_fifty"] = False
            elif helps["hint"]:
                hint(question)
                helps["hint"] = False
        user_answer = get_valid_input("Nhập câu trả lời của bạn (A/B/C/D): ", ["A", "B", "C", "D"])
        if user_answer == question["answer"]:
            print("Chính xác!")
            money += prize
        else:
            print("Sai! Đáp án đúng là:", question["answer"])
        print("Số tiền của bạn hiện tại là:", money)

play_game(questions1, helps, 100000)
play_game(questions2, helps, 200000)
play_game(questions3, helps, 300000)

print("Số tiền của bạn nhận được là:", money)

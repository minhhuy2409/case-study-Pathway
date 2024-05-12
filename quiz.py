print("chào mừng bạn đến với AI LÀ TRIỆU PHÚ")
print("luật chơi như sau:")
print("Bạn trả lời đúng đáp án bạn sẽ được 100k mỗi câu")
print("Bạn sẽ có 4 quyền trợ giúp là: hỏi ý khán giả, 50 50 và 2 gợi ý đáp án")
user = input("Nhập tên người chơi: ")
password = input("Nhập mật khẩu: ")

while user != "player" or password != "play":
    print("Tên người chơi hoặc mật khẩu không đúng. Vui lòng nhập lại.")
    user = input("Nhập tên người chơi: ")
    password = input("Nhập mật khẩu: ")

print("Vui lòng chỉ nhập A, B, C hoặc D.")


questions1 = [
    {
        "question": "1 Loại hoa nào được coi là biểu tượng của sự đẹp đẽ và tinh khiết?",
        "options": {
           "A": "Hoa Hồng",
            "B": "Hoa Sen",
            "C": "Hoa Cúc",
            "D": "Hoa Lan"
        },
        "answer": "B"
        
    },

    {
        "question": "2 Câu lệnh nào dùng để hiển thị dữ liệu ra màn hình trong Python?",
        "options": {
            "A": "print()",
            "B": "cout< <",
            "C": "System.out.printin()",
            "D": "echo"
        },
        "answer": "A"

    },
     
                              {
        "question": "3 Loài động vật nào là biểu tượng của sự kiên nhẫn và sức mạnh trong văn hóa Phương Tây?",
        "options": {
            "A": "Sư tử",
            "B": "Hổ",
            "C": "Rồng",
            "D": "Voi"
        },
        "answer": "B"

    },
          {
        "question": "4 Quốc gia nào là nơi nổi tiếng với văn hóa Samba và Carnival?",
        "options": {
            "A": "Argentina",
            "B": "Brazil",
            "C": "Mexico",
            "D": "Colombia"
        },
        "answer": "B"

    }]
questions2 = [


               {
        "question": "5 Python được phát hành vào năm nào?",
        "options": {
            "A": "1991",
            "B": "1989",
            "C": "2000",
            "D": "1995"
        },
        "answer": "B"

    },

                    {
       "question": "6 Ai là người phát minh ra máy tính đầu tiên trên thế giới?",
        "options": {
           "A": "Charles Babbage",
            "B": "Alan Turing",
            "C": "Ada Lovelace",
            "D": "John von Neumann"
        },
        "answer": "A"
    },
               {
        "question": "7 Ai là nhà triết học Hy Lạp nổi tiếng đã viết cuốn sách Chính Trị?",
        "options": {
            "A": "Socrates",
            "B": "Plato",
            "C": "Aristotle",
            "D": "Heraclitus"
        },
        "answer": "C"
    }]
questions3 = [

         {
        "question": "8 Ai là tác giả của cuốn tiểu thuyết Mười Nghìn Dặm Dưới Biển?",
        "options": {
            "A": "Jules Verne",
            "B": "H.G. Wells",
            "C": "George Orwellg",
            "D": "Mark Twain"
        },
        "answer": "A"
    },
 
                                   {
        "question": "9 Trong lịch sử, ai là người phụ nữ đầu tiên được công nhận là bác sĩ tại Hoa Kỳ vào thế kỷ 19?",
        "options": {
            "A": "Elizabeth Blackwell",
            "B": "Clara Barton",
            "C": "Mary Edwards Walker",
            "D": "Margaret Sanger"
        },
        "answer": "A"
    },
                                        {
        "question": "10 Trong thế kỷ 19, nhà văn nào viết tiểu thuyết đầu tiên trong lịch sử được viết bằng máy đánh chữ?",
        "options": {
            "A": "Jules Verne",
            "B": "H.G. Wells",
            "C": "Leo Tolstoyg",
            "D": "Mary Shelley"
        },
        "answer": "D"
    }
     
]

money = 0

for question in questions1:
    print(question["question"])
    for option, value in question["options"].items():
        print(option + ".", value)
    while True:
        answer = input("Nhập đáp án của bạn (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Vui lòng chỉ nhập A, B, C hoặc D!")
    if answer == question["answer"]:
        print("Đúng!")
        money += 100000
    else:
        print("Sai! Đáp án đúng là:", question["answer"])
        
print("Số tiền của bạn hiện tại là:", money)



for question in questions2:
    print(question["question"])
    for option, value in question["options"].items():
        print(option + ".", value)
    while True:
        answer = input("Nhập đáp án của bạn (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Vui lòng chỉ nhập A, B, C hoặc D!")
    if answer == question["answer"]:
        print("Đúng!")
        money += 200000
    else:
        print("Sai! Đáp án đúng là:", question["answer"])
print("Số tiền của bạn hiện tại là:", money)

        
for question in questions3:
    print(question["question"])
    for option, value in question["options"].items():
        print(option + ".", value)
    while True:
        answer = input("Nhập đáp án của bạn (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Vui lòng chỉ nhập A, B, C hoặc D!")
    if answer == question["answer"]:
        print("Đúng!")
        money += 300000
    else:
        print("Sai! Đáp án đúng là:", question["answer"])

print("Số tiền của bạn là:", money)

user = input("Nhập tên người chơi: ")
password = input("Nhập mật khẩu: ")

if user == "player" and password == "playp":
    print("Welcome!")
else:
    print("Wrong password and username.")
print("vui lòng chỉ nhập A B C D")
questions = [
    {
        "question": "1 Python được phát hành vào năm nào?",
        "options": {
            "A": "1991",
            "B": "1989",
            "C": "2000",
            "D": "1995"
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
        "question": "3 Ai là tác giả của cuốn tiểu thuyết Mười Nghìn Dặm Dưới Biển?",
        "options": {
            "A": "Jules Verne",
            "B": "H.G. Wells",
            "C": "George Orwellg",
            "D": "Mark Twain"
        },
        "answer": "A"
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
    },
               {
        "question": "5 Ai là nhà triết học Hy Lạp nổi tiếng đã viết cuốn sách Chính Trị?",
        "options": {
            "A": "Socrates",
            "B": "Plato",
            "C": "Aristotle",
            "D": "Heraclitus"
        },
        "answer": "C"
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
        "question": "7 Loại hoa nào được coi là biểu tượng của sự đẹp đẽ và tinh khiết?",
        "options": {
           "A": "Hoa Hồng",
            "B": "Hoa Sen",
            "C": "Hoa Cúc",
            "D": "Hoa Lan"
        },
        "answer": "B"
    },
                              {
        "question": "8 Loài động vật nào là biểu tượng của sự kiên nhẫn và sức mạnh trong văn hóa Phương Tây?",
        "options": {
            "A": "Sư tử",
            "B": "Hổ",
            "C": "Rồng",
            "D": "Voi"
        },
        "answer": "B"
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

score = 0

for question in questions:
    print(question["question"])
    for option, value in question["options"].items():
        print(option + ".", value)
    answer = input("Nhập đáp án của bạn: ").upper()
    if answer == question["answer"]:
        print("Đúng!")
        score += 1
    else:
        print("Sai! Đáp án đúng là:", question["answer"])
print("Số điểm của bạn là:", score)


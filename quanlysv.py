menu ={
    "1": "nhập danh sách sinh viên",
    "2": "xuất thông tin danh sách sinh viên",
    "3": "xuất thông tin danh sách sinh viên có học lực giỏi",
    "4": "sắp xếp danh sách sinh viên theo điểm",
    "5": "kết thúc"
}
while True:
    print ("==="*10 + "MENU" + "==="*10)
    for k,v in menu.items():
        print(f"{k}. {v}")
    print ("==="*10 + "===" + "==="*10)
    print ("Mời bạn chọn chức năng: ")
    lua_chon = input("nhập chức năng chương trình: ")
    match lua_chon:
        case "1":
            print("bạn đã chọn chức năng 1")
        case "2":
            print("bạn đã chọn chức năng 2")
        case "3":
            print("bạn đã chọn chức năng 3")
        case "4":
            print("bạn đã chọn chức năng 4")
        case "5":
            print("bạn đã chọn kết thúc chương trình")
            break
        case _:
            print("chức năng bạn chọn không hợp lệ, vui lòng chọn lại!")
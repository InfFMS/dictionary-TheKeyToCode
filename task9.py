# Дан граф друзей в социальной сети, где:
# Ключ словаря — имя пользователя (вершина графа).
# Значение — список друзей (смежные вершины).

# Пример входных данных:
# friends_graph = {
#     "Анна": ["Борис", "Виктор", "Дарья"],
#     "Борис": ["Анна", "Виктор"],
#     "Виктор": ["Анна", "Борис", "Дарья"],
#     "Дарья": ["Анна", "Виктор", "Елена"],
#     "Елена": ["Дарья"]
# }

# Написать функции, которые выполняют следующие операции:
# 1. Поиск друзей (соседей) для заданного пользователя.
# 2. Проверка, являются ли два пользователя друзьями (есть ли ребро между вершинами).
# 3. Поиск изолированных пользователей (вершин без рёбер).
friends_graph = {
    "Анна": ["Борис", "Виктор", "Дарья"],
    "Борис": ["Анна", "Виктор"],
    "Виктор": ["Анна", "Борис", "Дарья"],
    "Дарья": ["Анна", "Виктор", "Елена"],
    "Елена": ["Дарья"],
    "Григорий": []
}
def test_data(st):
    print(st)
    return st
def is_name_found(st):
    data = {"a": st}
    a=data["a"]
    if a in friends_graph:
        return True
    return False
def find_friends(st):
    data = {"a": st}
    a=data["a"]
    if a in friends_graph:
        s = "Друзья пользователя с именем " + a + ": " + ", ".join(friends_graph[a])
        if s:
            return s
        else:
            return "UNDEFINED ERROR!"
    return "ERROR: UNDEFINED NAME!"
def is_friends(st):
    deltadata=st.split(", ")
    print(deltadata)
    data = {"a": deltadata[0], "b": deltadata[1]}
    a=data["a"]
    b=data["b"]
    if a in friends_graph and b in friends_graph:
        if b in friends_graph[a] and a in friends_graph[b]:
            return "Да, они друзья"
        elif b in friends_graph[a] or a in friends_graph[b]:
            return "ERROR: ONLY ONE IS A FRIEND!"
        else:
            return "Они не друзья :("
    s="ERROR: UNDEFINED NAME \""
    if not(is_name_found(a)):
        s += a + "\""
        if not(is_name_found(b)):
            s+= " and \"" + b + "\"!"
        else:
            s+="!"
    elif not(is_name_found(b)):
        s += b + "\""
    else:
        return "UNDEFINED ERROR!"
    return s
def find_isolated_users(st):
    s="Изолированные пользователи(Без друзей): "
    for i in friends_graph:
        if not(friends_graph[i]):
            s+= "\"" + i + "\", "
    if s!="Изолированные пользователи(Без друзей): ":
        return s
    return "Нету Изолированных пользователей(Без друзей)!"
def add_new(st):
    if st.find(":")!=-1:
        neww=st[:st.find(":")]
        deltadata=st[st.find(":")+2:].split(", ")
    else:
        neww=st
        deltadata=[]
    # print(deltadata, neww)
    data = {"new": neww, "friends": deltadata}
    new=data["new"]
    friends=data["friends"]
    if new and not(new in friends_graph):
        friends_graph[new] = []
        for i in friends:
            if i in friends_graph:
                friends_graph[i].append(new)
                friends_graph[new].append(i)
            else:
                print("ERROR: UNDEFINED NAME \"" + i + "\"!")
    else:
        return "ERROR: THIS NAME IS ALREADY TAKEN!"
    return "SUCCESSFULLY SAVED!"
def show_all_list(st):
    for i in friends_graph:
        print(i+": " + ", ".join(friends_graph[i]))
    return " "
def add_new_friend_line(st):
    deltadata=st.split(", ")
    print(deltadata)
    if len(deltadata) != 2:
        return "ERROR: WRONG INPUT!"
    data = {"a": deltadata[0], "b": deltadata[1]}
    a=data["a"]
    b=data["b"]
    s = "ERROR: UNDEFINED NAME \""
    if not (is_name_found(a)):
        s += a + "\""
        if not (is_name_found(b)):
            s += " and \"" + b + "\"!"
        else:
            s += "!"
    elif not (is_name_found(b)):
        s += b + "\""
    else:
        return "UNDEFINED ERROR!"
    if a in friends_graph[b] and b in friends_graph[a]:
        return "ERROR: THIS LINE IS ALREADY CREATED!"
    else:
        friends_graph[a].append(b)
        friends_graph[b].append(a)
    return "SUCCESSFULLY CREATED!"
def show_all_codes(st):
    for i in codes:
        # print(codes)
        s = i + ": Смысл:" + codes[i][0] + ", input = \"" + codes[i][2] + "\""
        print(s)
o = True #Можно сделать функцию "throw_error" что при ошибке будет заканчивать бесконечный цикл
req=""
codes = {
    "test data": ["", test_data, ""],
    "isolated users": ["запросить всех пользователей без друзей", find_isolated_users, ""],
    "is friends": ["Узнать, друзья ли данные пользователи", is_friends, "name_of_user1, name_of_user2"],
    "find friends": ["Найти друзей у данного пользователя", find_friends, "name_of_user"],
    "add new": ["Создать нового пользователя", add_new, "name_of_new_user: friend1, friend2, friend3, ..."],
    "add new friend line": ["Создать новую связь", add_new_friend_line, "name_of_user1 name_of_user2"],
    "show all codes": ["Показать все возможнные коды", show_all_codes, ""],
    "show all list": ["Показать весь список друзей", show_all_list, ""]
}
while o and req!="end":
    req = input("Введите запрос(\"end\" - закончить запросы, \"show all codes\" - Показать все возможнные коды, show all list - Показать весь список друзей): ")
    if req == "end":
        o=False
        print("END OF REQUESTS")
    elif req=="show all codes":
        print(codes[req][1](""))
    elif req in codes:
        if codes[req][2]!="":
            req1=input("INPUT("+codes[req][2]+"): ")
            print(codes[req][1](req1))
        else:
            print(codes[req][1](""))
# match req:
    #     case "end":
    #         o=False
    #         print("END OF REQUESTS")
    #
# print(codes["is friends"][1]({"a":"Елена", "b":"Дарья"}))
# print(codes["isolated users"][1]({}))
# print(codes["test data"][1]({"kaka": "test1"}))
# print(find_isolated_users())

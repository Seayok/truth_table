def get_value(ls, res_ls, equation):
    if len(ls) == 0:
        for i in res_ls:
            print(i, end=' ')
        valid = False
        left_ls = []
        brack_ls = []
        tmp = equation
        for i in range(len(equation)):
            if equation[i] == "(":
                left_ls.append(i)
            elif equation[i] == ")":
                brack_ls.append([left_ls[-1], i])
                left_ls.pop(-1)
    
        res = tmp
        for i in range(len(brack_ls)):
            left, right = brack_ls[i]
            value = eval(tmp[left + 1: right])
            if value != 0:
                value = 1
            res = res.replace(tmp[left: right + 1], str(value))
        res = res.replace("-0", "1").replace("-1","0")
        if eval(res) != 0:
            res = 1
        else:
            res = 0
        print(res)
    else:
        char = ls[0]
        lsa = ls.copy()
        lsa.pop(0)
        lsb = ls.copy()
        lsb.pop(0)
        res_lsa = res_ls.copy()
        res_lsb = res_ls.copy()
        res_lsa.append("1")
        res_lsb.append("0")
        a = equation.replace(char, "1")
        b = equation.replace(char, "0")
        get_value(lsa, res_lsa, a)
        get_value(lsb, res_lsb, b)


def main():
    invalid = True
    char_ls = []
    while invalid:
        com_pro = input()
        com_pro = com_pro.replace("v", "+")
        com_pro = com_pro.replace("and", "*")
        for i in range(len(com_pro)):
            char = com_pro[i]
            if char not in ["(", ")", "*", "-", "+", " "]:
                if i != len(com_pro) - 1:
                    next_char = com_pro[i + 1]
                    if next_char not in ["(", ")", "*", "-", "+", " "]:
                        print("INVALID")
                        return
                if char not in char_ls:
                    char_ls.append(char)
        invalid = False 
    ls = char_ls.copy()
    res_ls = []
    for char in char_ls:
        print(char, end=" ")
    print("Res")
    get_value(ls, res_ls, com_pro)
    
main()   
                    



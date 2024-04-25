s = "()"

def isValid(s: str) -> bool:
    open_parens = ['(', '[', '{']
    closed_parens = [')', ']', '}']
    open_parens_w_indices = {}
    closed_parens_w_indices = {}
    for each in s:
        if each in open_parens:
            open_parens_w_indices[s.index(each)] = each
        elif each in closed_parens:
            closed_parens_w_indices[s.index(each)] = each
        
    open_parens_w_indices = sorted(open_parens_w_indices.keys())

    return False

print(isValid(s))

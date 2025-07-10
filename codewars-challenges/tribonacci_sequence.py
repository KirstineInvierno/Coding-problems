def tribonacci(signature:list[int], n:int)->list:
    for i in range(3):
        total = signature[-1] + signature[-2] + signature[-3]
        signature.append(total)
    return signature[:n]
'''4.小木棍
小 S 喜欢收集小木棍。在收集了n 根长度相等的小木棍之后，他闲来无事，便用它们拼起了数字。用小木棍拼每种数字的方法如下图所示。
 
现在小 S 希望拼出一个正整数，满足如下条件：
拼出这个数恰好使用n 根小木棍；
拼出的数没有前导0；
在满足以上两个条件的前提下，这个数尽可能小。
小 S 想知道这个数是多少，可n 很大，把木棍整理清楚就把小 S 折腾坏了，所以你需要帮他解决这个问题。如果不存在正整数满足以上条件，你需要输出 ‐1 进行报告。
输入描述：
输入的第一行包含一个正整数T，表示数据组数。接下来包含T 组数据，每组数据的格式如下：
一行包含一个整数n，表示木棍数。
对于所有测试数据，保证：1≤T≤50，1≤n≤105。
输出描述：
对于每组数据：输出一行，如果存在满足题意的正整数，输出这个数；否则输出 ‐1。
样例输入：
5
1
2
3
6
18
样例输出：
-1
1
7
6
208
样例解释：
对于第一组测试数据，不存在任何一个正整数可以使用恰好一根小木棍摆出，故输出 -1。对于第四组测试数据，注意 0 并不是一个满足要求的方案。
摆出 9、41 以及 111都恰好需要 6 根小木棍，但它们不是摆出的数最小的方案。 对于第五组测试数据，摆出 208 需要 5 + 6 + 7 = 18 根小木棍。
可以证明摆出任何一个小于 208 的正整数需要的小木棍数都不是 18。注意尽管拼出 006 也需要 18 根小木棍，但因为这个数有前导零，因此并不是一个满足要求的方案。'''

def find_smallest_number(n):
    if n == 2:
        return '1'
    elif n == 3:
        return '7'
    elif n == 4:
        return '4'
    elif n == 5:
        return '2'
    elif n == 6:
        return '6'
    elif n == 7:
        return '8'
    elif n == 8:
        return '10'
    elif n == 9:
        return '18'
    elif n == 10:
        return '22'
    elif n == 11:
        return '20'
    elif n == 12:
        return '28'
    elif n == 13:
        return '68'
    elif n == 14:
        return '88'
    elif n == 15:
        return '108'
    elif n == 16:
        return '188'
    elif n == 17:
        return '200'
    elif n == 18:
        return '208'
    else:
        # 对于更大的n，可以如下构建
        if n % 7 == 0:
            return '8' * (n // 7)
        elif n % 7 == 1:
            return '10' + '8' * ((n // 7) - 1)
        elif n % 7 == 2:
            return '1' + '8' * (n // 7)
        elif n % 7 == 3:
            return '200' + '8' * ((n // 7) - 2)
        elif n % 7 == 4:
            return '20' + '8' * ((n // 7) - 1)
        elif n % 7 == 5:
            return '2' + '8' * (n // 7)
        elif n % 7 == 6:
            return '6' + '8' * (n // 7)

# 读取输入
T = int(input('一个正整数T，表示数据组数:').strip())
results = []

print(f'请输入{T}行，一行包含一个整数n，表示木棍数：')
for _ in range(T):
    n = int(input().strip())
    if n == 1:
        results.append('-1')  # 1根木棍无法拼出任何正整数
    else:
        results.append(find_smallest_number(n))

# 输出结果
for result in results:
    print(result)

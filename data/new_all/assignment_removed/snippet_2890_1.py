class sub:

    def f1(self, s1):
        return self.f2([], sorted(s1))

    def f2(self, curr, s1):
        if s1:
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
        return [curr]
a = []
for i in range(0, n):
    b = int(input('Enter element: '))
    a.append(b)
print('Subsets: ')
print(sub().f1(a))
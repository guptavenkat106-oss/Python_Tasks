class Result:

    def calculate(self, sub1, sub2, sub3=None):
        if sub3 is None:
            total = sub1 + sub2
            average = total / 2
            print("Total (@ subject):",total)
            print("Average:", average)
        else:
            total = sub1 + sub2 + sub3
            average = total / 3
            print("Total (3 subjects):", total)
            print("Average:", average)

        print("----------------------")

r =  Result()

r.calculate(80,90)

r.calculate(75,85,95)

        

print("Enter Student Name:")
Student_name = input()
Course1 = int(input("Enter Grade points for Course 1"))
Course2 = int(input("Enter Grade points for Course 2"))
Course3 = int(input("Enter Grade points for Course 3"))

Total = Course1 + Course2 + Course3


percentile = (Total/300) * 100
if percentile < 100 and percentile > 90:
    print("Grade A")
elif percentile < 90 and percentile > 80:
    print("Grade B")
elif percentile < 80 and percentile > 70:
    print("Grade C")
elif percentile < 70 and percentile > 60:
    print("Grade D")
elif percentile < 60 and percentile > 50:
    print("Grade E")
elif percentile < 50 and percentile > 40:
    print("Grade F")




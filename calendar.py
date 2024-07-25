def isLeapYear(year):
  return year % 4 == 0 and year %100 != 0 or year % 400 == 0

def lastDay(year,month):
  m = [31,28,31,30,31,30,31,31,30,31,30,31]

  if isLeapYear(year):
    m[1] = 29
  else:
    m[1] = 28
  return m[month - 1]

def totalDay(year, month, day):
  #1년 1월 1일 부터 전 년도 12월 31일까지 지난 날짜를 계산한다.
  total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400

  #전년도 까지 지난 날짜의 합계에 전 달까지 지난 날짜를 더한다.
  for i in range(1,month):
    total += lastDay(year, i)
  return total + day

def weekDay(year, month, day):
  return totalDay(year, month, day) % 7


if __name__ == "__main__":
  year, month = map(int, input('달력을 출력할 년, 월을 입력하세요 : ').split())
  print('=' * 28)
  print('         {0:4d}년{1:2d}월'.format(year, month))
  print('=' * 28)
  print(' 일 월 화 수 목 금 토 ')
  print('=' * 28)

  for i in range(weekDay(year, month, 1)):
    #1일이 출력될 요일의 위치를 맞추기 위해서 1일의 요일만큼 반복하며 빈칸을 출력한다.
    print('    ', end = '') #빈 칸은 반복당 4칸씩 띄운다.

  #1일 부터 달력을 출력할 달의 마지막 날짜까지 반복하며 달력을 출력한다.
  for i in range(1, lastDay(year, month) + 1):
    print(' {0:2d} '.format(i), end = '')

    #출력한 날짜(i)가 토요일이고 그 달의 마지막 날짜가 아니면 줄을 바꾼다.
    if weekDay(year, month, i) == 6 and i != lastDay(year, month):
      print()

  print('\n' + '=' * 28)


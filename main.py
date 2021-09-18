import time
begin = True

while begin:
      start = int(input(" Enter Starting Number :"))
      end = int(input(" Enter ending Number : "))
      tic = time.perf_counter()
      while start <= end:

            print(start)
            start = start + 1
      toc = time.perf_counter()
      print(f"Total Time Taken {toc - tic:0.4f} seconds")

      needToContinue = input("Do you want to try again (Y/N) ")

      if str.upper(needToContinue) == "N":
            begin = False


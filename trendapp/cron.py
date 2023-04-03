def my_scheduled_job():
  print("hello world")
  f = open("cron_write.txt", "a")
  f.write("Now the file has more content!\n")
  f.close()
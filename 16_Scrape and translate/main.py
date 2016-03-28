import translate


def main():

  readable = "hello how are you today"
  chinese = translate.translateString("en","zh-CN",str(readable))
  print readable
  english = translate.translateString("zh-CN","en",chinese)
  print english


if __name__ == "__main__":
  main()
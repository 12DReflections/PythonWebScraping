import GoogleTranslate
import time




def main():
	
	sentence = open("text.txt").read()

	print sentence
	
	
	translatedHeb = GoogleTranslate.translate(sentence, 'hr','en')
	time.sleep(1)

	print translatedHeb


	translatedFR = GoogleTranslate.translate(translatedHeb, 'en','hr')
	print translatedFR




if __name__ == '__main__':
	main()
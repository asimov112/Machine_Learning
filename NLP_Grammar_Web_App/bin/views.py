#https://pypi.org/project/py-readability-metrics/
from readability import Readability
from gingerit.gingerit import GingerIt
from nltk.tokenize import sent_tokenize
from textstat import *
from flask import *
from bin import app
import textstat
import sys,os

def automatedReadabilityCategory(ARIScore):
    gradeLevel = {1:"Kindergaren",2:"First grade",3:"Second grade",4:"Third grade",
                  5:"Fourth grade",6:"Fifth grade",7:"Sixth grade",8:"Seventh grade",
                  9:"Eigth grade",10:"Ninth grade",11:"Tenth grade",12:"Eleventh grade",
                  13:"Twelfth grade",14:"College student"
                  }
    for index in range(1,15,1):
        if index == 15:
            return "No grade could be established"
        if index == ARIScore:
            return gradeLevel[index]    
    return 0 
    
def scoringCategory(readingScore):
    if (readingScore > 0) and (readingScore <= 29):
        return "Very confusing"
    if (readingScore >= 30) and (readingScore <= 49):
        return "Difficult"    
    if (readingScore >= 50) and (readingScore <= 59):
        return "Fairly Difficult"
    if (readingScore >= 60) and (readingScore <= 69):
        return "Standard"
    if (readingScore >= 70) and (readingScore <= 79):
        return "Fairly easy"
    if (readingScore >= 80) and (readingScore <= 89):
        return "Easy"
    if (readingScore >= 90) and (readingScore <= 100):
        return "Very easy"
    if (readingScore > 100):
        return "Extremely easy"

@app.route("/",methods = ["GET","POST"])
def checkSemantics():
    try:
        if request.method == "POST":
            textData = request.form.get("orgText")
            
            number_of_sentences = sent_tokenize(textData)
            # Executing grammar and spelling checker
            textParser = GingerIt()
            result = [textParser.parse(sentence)["result"] for sentence in number_of_sentences]
            print(result)
            dataResponse = ' '.join(result)

            # Runnning text analysis algorithms
            fleschReadingEaseScore = round(textstat.flesch_reading_ease(textData))
            fleschReadingRating = str(scoringCategory(fleschReadingEaseScore)) + ": " + str(fleschReadingEaseScore)
            ARIReadingScore = textstat.automated_readability_index(textData)
            ARIReadingRating = automatedReadabilityCategory(ARIReadingScore)
            LinsearScore = round(textstat.linsear_write_formula(textData),2)
                       
            return render_template("index.html",response=dataResponse,readingScore=fleschReadingRating,ARIReading=ARIReadingRating,writingScore=LinsearScore)
        return render_template("index.html")
    except Exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type,fname,exc_tb.tb_lineno)

import sqlite3
import rakeclass as RC
conn = sqlite3.connect('web2.db')

import csv
import sqlite3 as lite

conn = lite.connect('web2.db')
cur = conn.cursor()
cur.execute("SELECT content FROM content_scrape")
rows = cur.fetchall()

def selectkeywords():
    #with open('web_mainwords.csv', 'w') as f:
        #for row in rows:
            #print("Row is:",row)
            for hang in rows:
                text = hang
                print("Textla:",text)
                sentenceList = RC.split_sentences(text)
                # stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" like in Table 1.1
                stoppath = "SmartStoplist.txt"  # SMART stoplist misses some of the lower-scoring keywords in Figure 1.5, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
                stopwordpattern = RC.build_stop_word_regex(stoppath)

                # generate candidate keywords
                phraseList = RC.generate_candidate_keywords(sentenceList, stopwordpattern)

                # calculate individual word scores
                wordscores = RC.calculate_word_scores(phraseList)

                # generate candidate keyword scores
                keywordcandidates = RC.generate_candidate_keyword_scores(phraseList, wordscores)

                rake = RC.Rake("SmartStoplist.txt")
                keywords = rake.run(text)
                mainword1 = RC.inword5(wordscores)
                mainword = str(RC.inKey5(wordscores)  )
                print("mainword:",mainword)
                #conn = lite.connect('web2.db')
                #cur = conn.cursor()
            try:
                    #cur.execute("ALTER TABLE content_scrape ADD COLUMN keywordcolumn CHAR")
                cur.execute("INSERT INTO content_scrape (keywordcolumn) VALUES(?)",(mainword))
                    #cur.executemany(mainword)
            except sqlite3.IntegrityError as e:
                print('sqlite error',e.args[0]) # column name is not unique
                #cur.execute("VALUES (mainword)")
                #conn.commit()
                #conn.close()
                #f.write(str(row) +'\n')
                #f.write(str(mainword)+'\n')

                                                                                   
selectkeywords()














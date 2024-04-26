class NaiveBayesClassifier:
    def __init__(self):
        self.p_spam =None
        self.p_ham=None
        self.p_word_given_spam={}
        self.p_word_given_ham={}
    def fit(self,data):
        spam_word_cnt={}
        ham_word_cnt={}
        total_spam_word=0
        total_ham_word=0
        for email,label in data:
            for word,count in email.items():
                if(label=="spam"):
                    spam_word_cnt[word]=spam_word_cnt.get(word,0)+count
                    total_spam_word+=count
                else:
                    ham_word_cnt[word]=ham_word_cnt.get(word,0)+count
                    total_ham_word+=count
            
        self.p_ham=total_ham_word/(total_ham_word+total_spam_word)
        self.p_spam=total_spam_word/(total_ham_word+total_spam_word)

        for word,count in spam_word_cnt.items():
            self.p_word_given_spam[word]=(count+1)/(total_spam_word+len(spam_word_cnt))
        
        for word,count in ham_word_cnt.items():
            self.p_word_given_ham[word]=(count+1)/(total_ham_word+len(ham_word_cnt))
    
    def pridect(self,emails):
        y_predict=[]
        
        for email in emails:
            spam_p=self.p_spam
            ham_p=self.p_ham
            for word,count in email.items():
                if word in self.p_word_given_ham.keys():
                    ham_p*=(self.p_word_given_ham[word])**count
                if word in self.p_word_given_spam.keys():
                    spam_p*=(self.p_word_given_spam[word])**count
            
            if(spam_p>ham_p):
                y_predict.append("spam")
            else:
                y_predict.append("ham")
        return y_predict

data = [
    ({"word1": 2, "word2": 1}, "spam"),
    ({"word1": 1, "word3": 3}, "ham")
    # Add more data points here
]
test_emails = [
    {"word1": 1, "word2": 2},
    {"word3": 1, "word4": 2}
    # Add more test emails here
]
classifier=NaiveBayesClassifier()
classifier.fit(data)
predictions=classifier.pridect(test_emails)
print(predictions)



    
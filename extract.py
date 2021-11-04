from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences

def extract_summary(text):
	sentence_list = split_sentences(text)
	if len(split_sentences)==0: # Return the Warning Message if no sentence comes in
		return ['WARNING..!! There are no sentences to summarize..!']
	elif 1<=len(split_sentences)<=3: # return it as it is if the length of sentences is 1~3
		return split_sentences
	ratio_for_3_sentences = 3/len(sentence_list)
	summary_list = summarize(text , ratio_for_3_sentences, split=True)
	assert 3==len(summary_list), 'check length of source documents' # assert we return 3 sentences
	return summary_list

def translate(eng_summary_sentences):
	korean_summary_sentences = [ _ for sentences in eng_summary_sentences]
	return korean_summary_sentences

def get_summary(text):
	english_summary_list = extract_summary(text)
	korean_summary_list = translate(english_summary_list)
	return " ".join(english_summary_list),  " ".join(korean_summary_list)
	
'''
if __name__ =='__main__':
	print(extract_summary('자신이 사용하는 코드 편집 툴을 활용하여 수정 작업을 진행한다.작업이 완료되면, add, commit, push를 통해서 자신의 githu repository (origin)에 수정사항을 반영한다. 주의사항 push 진행시에 branch 이름을 명시해주어야 한다.push 완료 후 본인 계정의 github 저장소에 들어오면 Compare & pull reqeust 버튼이 활성화 되어 있다.해당 버튼을 선택하여 메시지를 작성하고 PR을 생성한다. push 완료 후 본인 계정의 github 저장소에 들어오면 Compare & pull reqeust 버튼이 활성화 되어 있다. 해당 버튼을 선택하여 메시지를 작성하고 PR을 생성한다.'))
	'''
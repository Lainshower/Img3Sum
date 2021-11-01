from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences

def extract_summary(text):
	ratio_for_3_sentences = 3/len(split_sentences(text))
	summary_list = summarize(ratio_for_3_sentences , 0.6, split=True)
	assert 3==len(summary_list), 'check length of source documents'
	return summary_list

def translate(eng_summary_sentences):
	korean_summary_sentences = [ _ for sentences in eng_summary_sentences]
	return korean_summary_sentences

def get_summary(text):
	english_summary_list = extract_summary(text)
	korean_summary_list = translate(english_summary_list)
	return " ".join(english_summary_list),  " ".join(korean_summary_list)

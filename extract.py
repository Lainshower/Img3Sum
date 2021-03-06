from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences
import requests


def extract_summary(text):
    sentence_list = split_sentences(text) # remove duplicates
    sentence_list = list(dict.fromkeys(sentence_list))
    text = " ".join(sentence_list)
    sentence_list = split_sentences(text)
    if len(sentence_list) == 0:  # Return the Warning Message if no sentence comes in
        return ['WARNING..!! There are no sentences to summarize..!']
    # return it as it is if the length of sentences is 1~3
    elif 1 <= len(sentence_list) <= 3:
        return split_sentences
    ratio_for_3_sentences = 3/len(sentence_list)
    summary_list = summarize(text, ratio_for_3_sentences, split=True)
    # assert we return 3 sentences
    assert 3 == len(summary_list), 'check length of source documents'
    return summary_list


def get_translate(text):

    url = "https://openapi.naver.com/v1/papago/n2mt"

    client_id = "DN8hEZj4W7XfX6oDpzDe"  # client_id 기입
    client_secret = "ZABewZQYKD"  # client_secret 기입

    data = {'text': text,
            'source': 'en',
            'target': 'ko'}

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode == 200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data

    else:
        return f'번역실패 <Error Code>:, {rescode}'


def translate(eng_summary_sentences):
    korean_summary_sentences = [get_translate(
        sentence) for sentence in eng_summary_sentences]
    return korean_summary_sentences


def get_summary(text):
    english_summary_list = extract_summary(text)
    korean_summary_list = translate(english_summary_list)
    return " ".join(english_summary_list),  " ".join(korean_summary_list)


'''
if __name__ == '__main__':
    #text = 'Optical character recognition of an image file with English text. Summarize extracted English text to 3 sentences. Translate summarized English text to Korean. check for grammatical errors in extracted English text.  Optical character recognition of an image file with Korean text'
    text = 'The research, conducted by a team of current and former MIT Concrete Sustainability Hub (MIT CSHub) scientists and published in Transportation Research D, finds that a set of innovative planning strategies could improve pavement network environmental and performance outcomes even if budgets don’t increase. The paper presents a novel budget allocation tool and pairs it with three innovative strategies for managing pavement networks: a mix of paving materials, a mix of short- and long-term paving actions, and a long evaluation period for those actions. This novel approach offers numerous benefits. When applied to a 30-year case study of the lowa U.S. Route network, the MIT CSHub model and management strategies cut emissions by 20 percent while sustaining current levels of road quality. Achieving this with a conventional planning approach would require the state to spend 32 percent more than it does today. The key to its success is the consideration of a fundamental — but fraught — aspect of pavement asset management: uncertainty.'
    eng_sum, kor_sum = get_summary(text)
    print(eng_sum)
    print(kor_sum)
'''
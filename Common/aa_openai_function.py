import openai
from dotenv import dotenv_values

secret = dotenv_values("./.env")
openai.api_key = secret["OPENAI_API_KEY"]

"""
    File name: aa_openai_function.py
    Description: This file contains functions to use openai api
"""

"""
    Description:
        Request openai api
    Parameters:
        content: string
        role: string
        model: string
        temperature: float
        max_tokens: int
        top_p: float
        frequency_penalty: float
        presence_penalty: float
    Return:
        chatgpt_content: string
"""
def openai_request(content, role="system", model="gpt-3.5-turbo", temperature=0, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0):
    try:
        response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
            "role": role,
            "content": content 
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
        )
        chatgpt_content = ""
        if(len(response['choices']) > 0):
            chatgpt_content = response['choices'][0]['message']['content']
        return chatgpt_content
    except Exception as e:
        print(e)
        return e

"""
    Description:
        Use chatgpt to generate a tweet from a given article
    Parameters:
        article: string
    Return:
        response: string
"""
def resume_article_chatgpt(article):
    try:
        return openai_request(content="Fait un tweet percutent a partir de l'article suivant, ne met pas de \" au tweet : \n" + article)
    except Exception as e:
        print(e)
        return e
    
"""
    Description:
        Use chatgpt to categorize a given article
    Parameters:
        article: string
    Return:
        response: string
"""
def article_category_chatgpt(article):
    try:
        return openai_request(article + "\n\nclassifie le tweet dans un de ces types\n\nConflits internationaux\nRelations diplomatiques\nÉlections à l'échelle mondiale\n\n\n\nMarchés boursiers\nCryptomonnaies\nEmploi et chômage\nEntrepreneuriat et startups\n\n\n\nAvancées médicales\nNouvelles technologies\nEspace et astronomie\nIntelligence artificielle\n\n\n\nChangements climatiques\nConservation de la nature\nÉnergies renouvelables\nPollution\n\n\n\nDiversité culturelle\nMouvements sociaux\nÉvolutions des normes sociales\n\n\n\nMaladies émergentes\nSoins de santé mentale\nRecherche médicale\n\n\n\nRéformes éducatives\nTechnologies éducatives\nEnseignement à distance\n\n\n\nSorties cinématographiques\nNouveaux albums et concerts\nÉvénements artistiques\n\n\n\nRésultats de matchs\nTransferts de joueurs\nÉvénements sportifs majeurs\n\n\n\nCrimes \nÉvénements extraordinaires\nMystères non résolus\n\nRetourne juste le type en réponse")
    except Exception as e:
        print(e)
        return e
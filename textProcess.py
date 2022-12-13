import pyttsx3
from pyChatGPT import ChatGPT

key = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..FM8vDsXsWyEum5Eg.D-luV5YV_t76qa0aDRor88f8yqKh4D-VURnkju9jwl8iTNFGUwckPIGn8LX0JP-OUJuY__PvV0NlfjHmrHw8KdzkHTS0Lm1s2sT-OZSR_aGu_A7AzZTDh253s-TAaKgHpLZB6wcb-ckKjUlV-U9fYe1U0tMxMNx7lCtyhUDkn_PBEIr8qUlLTTrqDIdC7yAJOu86YKHQMS482d2xTa2drS0A6O9t9FdcZAwVjN_lk0XE1NVE5mZ2EvglbUO1mccwdVgH2bZWfQWcfI6EyEupXUg1tvkP6pEqIMZGrs8TqiIvC9LvfE7HHUo79xF60uZuDOhJAB980mXaGRJukFakvuQG46J33fmEopbuiduwBphzZzDqKbP6SfYgOnQl-qXJt7nVRiLLyhEeOjhUHR_Pg05iuKbCtIGe94F004VkSs_lR0LeRF_esEvvhiBwJgZFXpVT1hZ7IZwK5Xp6HRGEm9_tNXu2CmZziUMRnxD9eXmdH-IWkPAwho8WKmuu_M3FHePzz-tATNptCzCMta_UoUFBkknJYMMJUeU8QuTVou2cjM5se5XH2nAOm1BioHlCF87NK-DeMkIkkLPwqeX8cAzAh0NUT612JDEcZp4gR87WZPnu0JXkSogx1ADq2SviDYuSZ95KPKJNLC3f4e6mz3pH3OU1iQOJWMlkbw4jqcflkJOVju_YUVNglRptgiDg0xodsF7Uvl9xtlQn_lpAf-qsrzPqOKH9gGs7akJn_QBaVYYw5ZSjoLNDWyycmaVP3zW2QHFEUImX43As3xPxPuQPTqizqF6nQKpW960Dxqc2aMevqEvPk43ahUlmaGlVvmjJhcpe61EvL2k_dYUIwRg1aaImnW7r7gI63trLu0v1zKc1sTHYlT-vUdja7rRx-rw1_FZp8qKZNOtYF0wEhueGuJHbD4pP1mprG9aUSCA0XMT3ln4cZIgx_oCMxTs_g6IY1bq9cADjJlqCwsPkEyXqP2mh32j0MuU96AMUo36Hr1lz1f8-0ygQYUL8DGcSFXXQ4J05rVRWhvE-yw1s3cNVq9GAByY2b7UfrIZY1juRsF8CKzOiwhcgEitwuC52e05n2utRgVEkbFnDBMOOkdax38MzuNZ9DMBFpoUoOb0i4bTY5Je5D_eQTWf4a1nUGByAizL-BYtkIMRdTDXFiMhPUf2HBGNZ7nZ3TGZWQk5Z0RwN0Fcn93ulll3Q-2FGn1qlXc8ix3CdRwKfSdHJXQaI6bvwsAu0tzqtqv1kUBfv_NAoBfQ-uOJWpErnqmhqd58xmnse7hG7d3r_e7WQlbAAj66hhhcpanpitVt0Ds1hsiXIweLXwcz5awSzjHyyTZnFdNil9vU4n9Y_TSZvoEItvGsYvT4ve53bqwgbhetCAeb_qa3BikjZ_za4r0isdKdfHCLuXRSxj5pLhJ0cPPQPIFzncZicjPNanxj8ug3ErMdggGe1pCe_x7tLOO0lq9MyR6BWb01KphaIikD3qj7O1zoXIS0ejQ4HvErYzpuGxZJCjppmEmn17HJJj6ISzTNXzk0qFBKw4TdbSTDt3SUK3GOnqcUojHQPB2nTxZuIAaFwXHWILKLeiXt7HIZLCOF5FfdNcPip0AOtxKf29VzXUKptRBGrqb9-vCM1h9_jFgQ621FxDrJq1da_xzJ6EvyHYrbunkIQ9GI8k_p8VU78V9qdzmFd9zF_YWW38fUUJKbrHCsWJfOoVv3jCGgGmSPksyJKZ2silGS8OEf2r_HOz2_stLUJn_u7xw2HPc1ZJX-BDKggS3Gj3bq2WzqmtLzN7TnWmZf-zxPOdOP1RLzABeMnX-hLQCb0cqUxbK5XCvcw28KEDwcHwzXnBtSCxkzUHwnRVw1QAXrceKdJSdetIr5FXGAq41B1rYfiAUaDQywApWJKCC2bJyLfZFYMaAhzCk7GWgSPKNpzs2KZixmp_uCw7elO63QQXGH7V5Dnd321SsEWHb7ytZrWnMSgw3CtqSVJz_Ji5ZKE5jSoCNIQsRu6PVZB365jH3P2wYuGfVWCp7MOCdFoHlgEW9S8aVjS0IIqYAuH-Gt_-3bDitR1TSaWt7RCjERc2Xd2P0G8jJgJSZ-1kYP5k_XI3V9ftOm4GCk5dPSTrxTRhDbeFnkH6UiEPYBH-pmqlc4JnZfhMigBa6f6mFNkr0d2f3zblPaH4GFEIkNHiAwBWvhqtD_ePIfPIi8wm1DZzelPDFxNkBcMPX8ZibLE9BIDryH0R6dV1I6ZyEoJQIadC1Vvcw.Att0zSbV_3B-mmdbySicEw"
api = ChatGPT(key)

def generateSentence(words):
    resp = api.send_message(f"form a sentence using the words {str(words)}")
    return resp['message']

f = open("words.txt", "r")
wordList = f.read()
f.close()
sentence = generateSentence(wordList)
engine = pyttsx3.init()
engine.say(sentence)
engine.runAndWait()
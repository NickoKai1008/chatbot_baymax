import openai

openai.api_key = "your API"

while True:
	ask = input('Chat: ')
	response = openai.Completion.create(
  		model="text-davinci-003",
  		prompt=ask,
  		temperature=0.9,
  		max_tokens=150,
  		top_p=1,
  		frequency_penalty=0,
  		presence_penalty=0.6,
  		stop=[" Human:", " AI:"]
		)

	text = response['choices'][0]['text']
	print ('Baymax: '+text)
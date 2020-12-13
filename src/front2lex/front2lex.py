import json
import boto3

# for  test
    
def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('lex-runtime')
    
    print(event)
    user_message = event.get('text','cong')

    response = client.post_text(botName = 'searchphotoalbum',
        botAlias = 'album',
        userId = '123',
        inputText = user_message)
    
    print(response)    
    
    return_message = response['message']
    print('return message is')
    print(return_message)
    return {
        'body':{
                'text':'test for code pipeline',
                'timestamp': '20201210'
                }
            }
  
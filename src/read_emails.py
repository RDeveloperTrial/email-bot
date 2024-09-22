from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (1, "month"),
    "unread": True
}

def read_gmails():

    try:
            # Call gmail API to get unread emails
            messages = gmail.get_messages(query=construct_query(query_params))
            
            return {
                'status': 1,
                'response': messages
                ###message = completion.choices[0].message.content
            }
    except:
            return {
                'status': 0,
                'response': ''
            }
    

cities_capitals={'andhra pradesh':'hyderabad',"arunachal pradesh":"itanagar","assam":"dispur","bihar":"patna","goa":"panaji",
                 "gujarat":"gandhinagar","haryana":"chandigarh","himachal pradesh":"shimla","jammu and kashmir":"srinagar in summers and jammu in winters",
                 "karnataka":"bangaluru","kerala":"thiruvananthapuram","madhya pradesh":"bhopal","maharashtra":"mumbai in summer and nagpur in winters","manipur":"imphal",
                 "meghalaya":"shillong","mizoram":"aizawl","nagaland":"kohima","orissa":"bhubaneswar","punjab":"chandigarh","rajasthan":"jaipur","sikkim":"gangtok",
                 "tamil nadu":"chennai","tripura":"agartala","uttar pradesh":"lucknow","west bengal":"kolkata","chhattisgarh":"raipur",
                 "uttarakhand":"dehradun","jharkhand":"ranchi","telangana":"hyderabad","delhi":"new delhi","andaman and nicobar islands":"port blair","chandigarh":"chandigarh",
                 "dadra and nagar haveli":"silvasa","daman and diu":"daman","lakshadweep":"kavaratti","puducherry":"puducherry"}

capitals_cities={'hyderabad':'andhra pradesh and telangana',"itanagar":"arunachal pradesh","dispur":"assam","patna":"bihar","panaji":"goa",
                 "gandhinagar":"gujarat","chandigarh":"haryana and punjab and it is the head quarter of the union teritory - chandigarh","shimla":"himachal pradesh","srinagar":"jammu and kashmir","jammu":"jammu and kashmir",
                 "bangalore":"karnataka","bangaluru":"karnataka","thiruvananthapuram":"kerala","bhopal":"madhya pradesh","mumbai":"maharashtra","bombay":"maharashtra","nagpur":"maharashtra","imphal":"manipur",
                 "shillong":"meghalaya","aizawl":"mizoram","kohima":"nagaland","bhubaneswar":"orissa","jaipur":"rajasthan","gangtok":"sikkim",
                 "chennai":"tamil nadu","agartala":"tripura","lucknow":"uttar pradesh","kolkata":"west bengal","raipur":"chhattisgarh",
                 "dehradun":"uttarakhand","ranchi":"jharkhand","new delhi":"delhi","port blair":"andaman and nicobar islands",
                 "silvasa":"dadra and nagar haveli","daman":"daman and diu","kavaratti":"lakshadweep","puducherry":"puducherry"}

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(speechlet_response):
    return {
        'version': '1.0',
        'response': speechlet_response
    }

#----------#

def get_welcome_response():
    card_title = "Welcome"
    speech_output = "Hello! Want to know about Indian states' capital? Ask me the capital of any Indian State... or... you can tell me the capital and ask me about the state to which it belongs! Ask me the capital of any Indian State by saying: tell me the capital of... or you can ask to which state does a capital belongs to by saying: tell me the state having capital..."
    reprompt_text = "Knock knock... Ask me the capital of any Indian State by saying: tell me the capital of... or you can ask to which state does a capital belongs to by saying: tell me the state having capital..."
    should_end_session = False
    return build_response(build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    
def get_end_response():
    card_title = "Goodbye"
    speech_output = "Thanks For using this skill. See ya."
    reprompt_text = "Thanks For using this skill. See ya."
    should_end_session = True
    return build_response(build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "I hope you learned something. You are the best! See ya!"
    should_end_session = True
    return build_response(build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_capital(intent, session):
    if 'value' in intent['slots']['city']:
        sel_city=intent['slots']['city']['value']
        sel_city=sel_city.lower()
        if sel_city in cities_capitals:
            if sel_city in {'delhi','andaman and nicobar islands','dadra and nagar haveli','daman and diu','lakshadweep','puducherry','chandigarh'}:
                response="The head quarter of the union teritory "+sel_city+" is "
            else: 
                response="The capital of the state "+sel_city+" is "
            your_capital=cities_capitals[sel_city]
            speech_output= response + your_capital
            reprompt_text = response + your_capital
            should_end_session=True
        else:
            speech_output = "Sorry, I dont have that information"
            reprompt_text = "Ask me the capital of any Indian State of you call tell me the capital and ask me about the state to which it belongs! Ask me the capital of any Indian State by saying: tell me the capital of... or you can ask to which state does a capital belongs to by saying: tell me the state having capital..."
            should_end_session = True
        return build_response(build_speechlet_response(
            "", speech_output, reprompt_text, should_end_session))
    else:
        speech_output="I am sorry, I dont have that information"
        reprompt_text="I am sorry, I dont have that information"
        should_end_session=True
        return build_response(build_speechlet_response(
            "", speech_output, reprompt_text, should_end_session))
        
def get_city(intent, session):
    if 'value' in intent['slots']['capital']:
        sel_capital=intent['slots']['capital']['value']
        sel_capital=sel_capital.lower()
        if sel_capital in capitals_cities:
            if sel_capital in {"new delhi","port blair","silvasa","daman","kavaratti","puducherry"}:
                response=sel_capital+" is the head quarter of the union teritory "
            else:
                response=sel_capital+" is the capital of the state "
            your_city=capitals_cities[sel_capital]
            speech_output= response + your_city
            reprompt_text = response + your_city
            should_end_session = True
        else:
            speech_output = "Sorry, I dont have that information"
            reprompt_text = "Ask me the capital of any Indian State of you call tell me the capital and ask me about the state to which it belongs! Ask me the capital of any Indian State by saying: tell me the capital of... or you can ask to which state does a capital belongs to by saying: tell me the state having capital..."
            should_end_session = True
        return build_response(build_speechlet_response(
            "", speech_output, reprompt_text, should_end_session))
    else:
        speech_output="I am sorry, I dont have that information"
        reprompt_text="I am sorry, I dont have that information"
        should_end_session=True
        return build_response(build_speechlet_response(
            "", speech_output, reprompt_text, should_end_session))

#----------#

def on_session_started(session_started_request, session):
    return get_welcome_response()

def on_launch(launch_request, session):
    return get_welcome_response()
    

def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "getCapitalIntent":
        return get_capital(intent, session)
    elif intent_name == "getCityIntent":
        return get_city(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    return get_end_response()
    
#----------#

def lambda_handler(event, context):
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

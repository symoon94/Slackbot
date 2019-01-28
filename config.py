BASE_URL = "https://slack.com/api/chat.postMessage"

token = "Your Token" # e.g. "xoxb-#%^#%^#%^"
username = 'moonbot'
channel = 'DFQ76S4LU'

# Configure the time according to time format
schedule = {
	'attendance1': {
		'time': '08:10',
		'message': "check attendance"
	},
	'attendance1': {
		'time': '08:20',
		'message': "check attendance"
	},
	'attendance1': {
		'time': '08:30',
		'message': "check attendance"
	},
	'attendance': {
		'time': '08:40',
		'message': "check attendance"
	},
	'workout': {
		'time': '10:37',
		'message': "work out"
	},
	'coding': {
		'time': '14:00',
		'message': "code"
	},
	'attendance2': {
		'time': '16:30',
		'message': "check attendance"
	},
	'attendance2': {
		'time': '16:40',
		'message': "check attendance"
	}
}

notify_before = [5,3,1]

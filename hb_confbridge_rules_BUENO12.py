'''
THIS EXAMPLE WILL NOT WORK AS IT IS - YOU MUST SPECIFY YOUR OWN VALUES!!!

This file is organized around the "Conference Bridges" that you wish to use. If you're a c-Bridge
person, think of these as "bridge groups". You might also liken them to a "reflector". If a particular
system is "ACTIVE" on a particular conference bridge, any traffid from that system will be sent
to any other system that is active on the bridge as well. This is not an "end to end" method, because
each system must independently be activated on the bridge.

The first level (e.g. "WORLDWIDE" or "STATEWIDE" in the examples) is the name of the conference
bridge. This is any arbitrary ASCII text string you want to use. Under each conference bridge
definition are the following items -- one line for each HBSystem as defined in the main HBlink
configuration file.

    * SYSTEM - The name of the sytem as listed in the main hblink configuration file (e.g. hblink.cfg)
        This MUST be the exact same name as in the main config file!!!
    * TS - Timeslot used for matching traffic to this confernce bridge
    * TGID - Talkgroup ID used for matching traffic to this conference bridge
    * ON and OFF are LISTS of Talkgroup IDs used to trigger this system off and on. Even if you
        only want one (as shown in the ON example), it has to be in list format. None can be
        handled with an empty list, such as " 'ON': [] ".
    * TO_TYPE is timeout type. If you want to use timers, ON means when it's turned on, it will
        turn off afer the timout period and OFF means it will turn back on after the timout
        period. If you don't want to use timers, set it to anything else, but 'NONE' might be
        a good value for documentation!
    * TIMOUT is a value in minutes for the timout timer. No, I won't make it 'seconds', so don't
        ask. Timers are performance "expense".
    * RESET is a list of Talkgroup IDs that, in addition to the ON and OFF lists will cause a running
        timer to be reset. This is useful   if you are using different TGIDs for voice traffic than
        triggering. If you are not, there is NO NEED to use this feature.
'''

BRIDGES = {
        'LORITO': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 9990, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [], 'OFF': [],'RESET': []},
            {'SYSTEM': 'LORO', 'TS': 2, 'TGID': 9990, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [], 'OFF': [],'RESET': []},
        ],
        'DMR+4370': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 4370, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [4370], 'OFF': [8870], 'RESET': []},
            {'SYSTEM': 'DMR+4370', 'TS': 2, 'TGID': 9, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],    
        'DMR+4371': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 4371, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [4371], 'OFF': [8871], 'RESET': []},
            {'SYSTEM': 'DMR+4371', 'TS': 2, 'TGID': 9, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ], 
        'DMR+4374': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 4374, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [4374], 'OFF': [8874], 'RESET': []},
            {'SYSTEM': 'DMR+4374', 'TS': 2, 'TGID': 9, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],  
        'DMR+21465': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 21465, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [10], 'OFF': [5], 'RESET': []},
            {'SYSTEM': 'DMR+21465', 'TS': 2, 'TGID': 21465, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
        'BM2140': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 2140, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [2140], 'OFF': [8840], 'RESET': []},
            {'SYSTEM': 'BM2140', 'TS': 2, 'TGID': 2140, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ], 
        'BM2143': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 2143, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [2143], 'OFF': [8803], 'RESET': []},
            {'SYSTEM': 'BM2143', 'TS': 2, 'TGID': 2143, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
        'BM21408': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 21408, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [21408], 'OFF': [8808], 'RESET': []},
            {'SYSTEM': 'BM21408', 'TS': 2, 'TGID': 21408, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
        'BM21443': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 21443, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [21443], 'OFF': [8843], 'RESET': []},
            {'SYSTEM': 'BM21443', 'TS': 2, 'TGID': 21443, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],        
        'BM21455': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 21455, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [21455], 'OFF': [8855], 'RESET': []},
            {'SYSTEM': 'BM21455', 'TS': 2, 'TGID': 21455, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
        'BM21465': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 21465, 'ACTIVE': False, 'TIMEOUT': 10, 'TO_TYPE': 'ON',  'ON': [5], 'OFF': [10], 'RESET': []},
            {'SYSTEM': 'BM21465', 'TS':2, 'TGID': 21465, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
        ],
        'XLX266-X': [
            {'SYSTEM': 'EA3EG', 'TS': 2, 'TGID': 4024, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4024], 'OFF': [8866], 'RESET': []},
            {'SYSTEM': 'XLX266-X', 'TS': 2, 'TGID': 4024, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [4024], 'OFF': [], 'RESET': []},
            {'SYSTEM': 'XLX266-X', 'TS': 2, 'TGID': 9, 'ACTIVE': True, 'TIMEOUT': 10, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},   
        ]   
}

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)

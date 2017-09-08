''' Get class names and part names associated with each class
Python implementation based on
http://www.stat.ucla.edu/~xianjie.chen/pascal_part_dataset/trainval.tar.gz

Define the part index of each objects.
One can merge different parts by using the same index for the
parts that are desired to be merged.
For example, one can merge
the left lower leg (llleg) and the left upper leg (luleg) of person by setting:
pimap[15]['llleg']      = 19;               # left lower leg
pimap[15]['luleg']      = 19;               # left upper leg
'''


def get_class_names():
    classes = {1: 'aeroplane',
               2: 'bicycle',
               3: 'bird',
               4: 'boat',
               5: 'bottle',
               6: 'bus',
               7: 'car',
               8: 'cat',
               9: 'chair',
               10: 'cow',
               11: 'table',
               12: 'dog',
               13: 'horse',
               14: 'motorbike',
               15: 'person',
               16: 'pottedplant',
               17: 'sheep',
               18: 'sofa',
               19: 'train',
               20: 'tvmonitor'}
    return classes


def get_pimap():
    pimap = {}

    # [aeroplane]
    pimap[1] = {}
    pimap[1]['body']        = 1
    pimap[1]['stern']       = 2
    pimap[1]['lwing']       = 3                # left wing
    pimap[1]['rwing']       = 4                # right wing
    pimap[1]['tail']        = 5
    for ii in range(1, 10 + 1):
        pimap[1][('engine_%d' % ii)] = 10+ii # multiple engines
    for ii in range(1, 10 + 1):
        pimap[1][('wheel_%d' % ii)] = 20+ii  # multiple wheels

    # [bicycle]
    pimap[2] = {}
    pimap[2]['fwheel']      = 1                # front wheel
    pimap[2]['bwheel']      = 2                # back wheel
    pimap[2]['saddle']      = 3
    pimap[2]['handlebar']   = 4                # handle bar
    pimap[2]['chainwheel']  = 5                # chain wheel
    for ii in range(1, 10 + 1):
        pimap[2][('headlight_%d' % ii)] = 10 + ii

    # [bird]
    pimap[3] = {}
    pimap[3]['head']        = 1
    pimap[3]['leye']        = 2                # left eye
    pimap[3]['reye']        = 3                # right eye
    pimap[3]['beak']        = 4
    pimap[3]['torso']       = 5
    pimap[3]['neck']        = 6
    pimap[3]['lwing']       = 7                # left wing
    pimap[3]['rwing']       = 8                # right wing
    pimap[3]['lleg']        = 9                # left leg
    pimap[3]['lfoot']       = 10               # left foot
    pimap[3]['rleg']        = 11               # right leg
    pimap[3]['rfoot']       = 12               # right foot
    pimap[3]['tail']        = 13

    # [boat]
    # only has silhouette mask

    # [bottle]
    pimap[5] = {}
    pimap[5]['cap']         = 1
    pimap[5]['body']        = 2

    # [bus]
    pimap[6] = {}
    pimap[6]['frontside']   = 1
    pimap[6]['leftside']    = 2
    pimap[6]['rightside']   = 3
    pimap[6]['backside']    = 4
    pimap[6]['roofside']    = 5
    pimap[6]['leftmirror']  = 6
    pimap[6]['rightmirror'] = 7
    pimap[6]['fliplate']    = 8                # front license plate
    pimap[6]['bliplate']    = 9                # back license plate
    for ii in range(1, 10 + 1):
        pimap[6][('door_%d' % ii)] = 10 + ii
    for ii in range(1, 10 + 1):
        pimap[6][('wheel_%d' % ii)] = 20 + ii
    for ii in range(1, 10 + 1):
        pimap[6][('headlight_%d' % ii)] = 30 + ii
    for ii in range(1, 20 + 1):
        pimap[6][('window_%d' % ii)] = 40 + ii

    # [car]
    pimap[7] = pimap[6].copy()         # car has the same set of parts with bus

    # [cat]
    pimap[8] = {}
    pimap[8]['head']        = 1
    pimap[8]['leye']        = 2                # left eye
    pimap[8]['reye']        = 3                # right eye
    pimap[8]['lear']        = 4                # left ear
    pimap[8]['rear']        = 5                # right ear
    pimap[8]['nose']        = 6
    pimap[8]['torso']       = 7
    pimap[8]['neck']        = 8
    pimap[8]['lfleg']       = 9                # left front leg
    pimap[8]['lfpa']        = 10               # left front paw
    pimap[8]['rfleg']       = 11               # right front leg
    pimap[8]['rfpa']        = 12               # right front paw
    pimap[8]['lbleg']       = 13               # left back leg
    pimap[8]['lbpa']        = 14               # left back paw
    pimap[8]['rbleg']       = 15               # right back leg
    pimap[8]['rbpa']        = 16               # right back paw
    pimap[8]['tail']        = 17

    # [chair]
    # only has sihouette mask

    # [cow]
    pimap[10] = {}
    pimap[10]['head']       = 1
    pimap[10]['leye']       = 2                # left eye
    pimap[10]['reye']       = 3                # right eye
    pimap[10]['lear']       = 4                # left ear
    pimap[10]['rear']       = 5                # right ear
    pimap[10]['muzzle']     = 6
    pimap[10]['lhorn']      = 7                # left horn
    pimap[10]['rhorn']      = 8                # right horn
    pimap[10]['torso']      = 9
    pimap[10]['neck']       = 10
    pimap[10]['lfuleg']     = 11               # left front upper leg
    pimap[10]['lflleg']     = 12               # left front lower leg
    pimap[10]['rfuleg']     = 13               # right front upper leg
    pimap[10]['rflleg']     = 14               # right front lower leg
    pimap[10]['lbuleg']     = 15               # left back upper leg
    pimap[10]['lblleg']     = 16               # left back lower leg
    pimap[10]['rbuleg']     = 17               # right back upper leg
    pimap[10]['rblleg']     = 18               # right back lower leg
    pimap[10]['tail']       = 19

    # [table]
    # only has silhouette mask

    # [dog]
    pimap[12] = pimap[8].copy()         	# dog has the same set of parts with cat,
                            		        # except for the additional
                        		            # muzzle
    pimap[12]['muzzle']     = 20

    # [horse]
    pimap[13] = pimap[10].copy()        	# horse has the same set of parts with cow,
                                            # except it has hoof instead of horn
    del pimap[13]['lhorn']
    del pimap[13]['rhorn']
    pimap[13]['lfho'] = 30
    pimap[13]['rfho'] = 31
    pimap[13]['lbho'] = 32
    pimap[13]['rbho'] = 33

    # [motorbike]
    pimap[14] = {}
    pimap[14]['fwheel']     = 1
    pimap[14]['bwheel']     = 2
    pimap[14]['handlebar']  = 3
    pimap[14]['saddle']     = 4
    for ii in range(1, 10 + 1):
        pimap[14][('headlight_%d' % ii)] = 10 + ii

    # [person]
    pimap[15] = {}
    pimap[15]['head']       = 1
    pimap[15]['leye']       = 2                    # left eye
    pimap[15]['reye']       = 3                    # right eye
    pimap[15]['lear']       = 4                    # left ear
    pimap[15]['rear']       = 5                    # right ear
    pimap[15]['lebrow']     = 6                    # left eyebrow
    pimap[15]['rebrow']     = 7                    # right eyebrow
    pimap[15]['nose']       = 8
    pimap[15]['mouth']      = 9
    pimap[15]['hair']       = 10

    pimap[15]['torso']      = 11
    pimap[15]['neck']       = 12
    pimap[15]['llarm']      = 13                   # left lower arm
    pimap[15]['luarm']      = 14                   # left upper arm
    pimap[15]['lhand']      = 15                   # left hand
    pimap[15]['rlarm']      = 16                   # right lower arm
    pimap[15]['ruarm']      = 17                   # right upper arm
    pimap[15]['rhand']      = 18                   # right hand

    pimap[15]['llleg']      = 19               	# left lower leg
    pimap[15]['luleg']      = 20               	# left upper leg
    pimap[15]['lfoot']      = 21               	# left foot
    pimap[15]['rlleg']      = 22               	# right lower leg
    pimap[15]['ruleg']      = 23               	# right upper leg
    pimap[15]['rfoot']      = 24               	# right foot

    # [pottedplant]
    pimap[16] = {}
    pimap[16]['pot']        = 1
    pimap[16]['plant']      = 2

    # [sheep]
    pimap[17] = pimap[10].copy()        # sheep has the same set of parts with cow

    # [sofa]
    # only has sihouette mask

    # [train]
    pimap[19] = {}
    pimap[19]['head']       = 1
    pimap[19]['hfrontside'] = 2                	# head front side
    pimap[19]['hleftside']  = 3                	# head left side
    pimap[19]['hrightside'] = 4                	# head right side
    pimap[19]['hbackside']  = 5                 # head back side
    pimap[19]['hroofside']  = 6                	# head roof side

    for ii in range(1, 10 + 1):
        pimap[19][('headlight_%d' % ii)] = 10 + ii

    for ii in range(1, 10 + 1):
        pimap[19][('coach_%d' % ii)] = 20 + ii

    for ii in range(1, 10 + 1):
        pimap[19][('cfrontside_%d' % ii)] = 30 + ii   # coach front side

    for ii in range(1, 10 + 1):
        pimap[19][('cleftside_%d' % ii)] = 40 + ii   # coach left side

    for ii in range(1, 10 + 1):
        pimap[19][('crightside_%d' % ii)] = 50 + ii  # coach right side

    for ii in range(1, 10 + 1):
        pimap[19][('cbackside_%d' % ii)] = 60 + ii   # coach back side

    for ii in range(1, 10 + 1):
        pimap[19][('croofside_%d' % ii)] = 70 + ii   # coach roof side


    # [tvmonitor]
    pimap[20] = {}
    pimap[20]['screen']     = 1

    return pimap

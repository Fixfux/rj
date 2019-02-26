#Authorized by http://line.me/ti/p/~kangnur04
#ALFINONH

from linepy import *
from akad.ttypes import *
from replyer import *
_session = requests.session()

botStart = time.time()
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

fino = LINE(run_bot['00'],run_bot['password'])
kang = LINE(run_bot['0'],run_bot['password'])
fn1 = LINE(run_bot['1'],run_bot['password'])
fn2 = LINE(run_bot['2'],run_bot['password'])
fn3 = LINE(run_bot['3'],run_bot['password'])
fn4 = LINE(run_bot['4'],run_bot['password'])
fn5 = LINE(run_bot['5'],run_bot['password'])
k1 = LINE(run_bot['k1'],run_bot['password'])
k2 = LINE(run_bot['k2'],run_bot['password'])

finoMID = fino.getProfile().mid
myMID = kang.getProfile().mid
fn1MID = fn1.getProfile().mid
fn2MID = fn2.getProfile().mid
fn3MID = fn3.getProfile().mid
fn4MID = fn4.getProfile().mid
fn5MID = fn5.getProfile().mid
k1MID = k1.getProfile().mid
k2MID = k2.getProfile().mid

finoProfile = fino.getProfile()
settings = fino.getSettings()
run_bot['ALFINONH'] = finoMID
run_bot["Creator"] = finoMID
run_bot["Admin"][finoMID] = True
run_bot["fino"]['AuthToken'] = str(fino.authToken)
channel = Channel(fino, fino.server.CHANNEL_ID['LINE_TIMELINE'])
channelToken = channel.getChannelResult()
run_bot["fino"]["channelAccessToken"] = str(fino.tl.channelAccessToken)
run_bot["fino"]["displayName"] = finoProfile.displayName
run_bot["fino"]["statusMessage"] = finoProfile.statusMessage
run_bot["fino"]["pictureStatus"] = finoProfile.pictureStatus
cont = fino.getContact(finoMID)
run_bot["fino"]["videoProfile"] = cont.videoProfile
coverId = fino.getProfileDetail()["result"]["objectId"]
run_bot["fino"]["coverId"] = coverId
run_bot["fino"]["Mid"] = finoMID
run_bot['kang']['AuthToken'] = str(kang.authToken)
run_bot["kang"]["Mid"] = myMID
run_bot["kang"]["channelAccessToken"] = str(kang.tl.channelAccessToken)
run_bot["kang"]["displayName"] = kang.getProfile().displayName
run_bot["kang"]["statusMessage"] = kang.getProfile().statusMessage
run_bot["kang"]["pictureStatus"] = kang.getProfile().pictureStatus
cont = kang.getContact(myMID)
run_bot["kang"]["videoProfile"] = cont.videoProfile
run_bot['fino1']['AuthToken'] = str(fn1.authToken)
run_bot["fino1"]["Mid"] = fn1MID
run_bot["fino1"]["channelAccessToken"] = str(fn1.tl.channelAccessToken)
run_bot["fino1"]["displayName"] = fn1.getProfile().displayName
run_bot["fino1"]["statusMessage"] = fn1.getProfile().statusMessage
run_bot["fino1"]["pictureStatus"] = fn1.getProfile().pictureStatus
cont = fn1.getContact(fn1MID)
run_bot["fino1"]["videoProfile"] = cont.videoProfile
coverId = fn1.getProfileDetail()["result"]["objectId"]
run_bot["fino1"]["coverId"] = coverId
run_bot['fino2']['AuthToken'] = str(fn2.authToken)
run_bot["fino2"]["Mid"] = fn2MID
run_bot["fino2"]["channelAccessToken"] = str(fn2.tl.channelAccessToken)
run_bot["fino2"]["displayName"] = fn2.getProfile().displayName
run_bot["fino2"]["statusMessage"] = fn2.getProfile().statusMessage
run_bot["fino2"]["pictureStatus"] = fn2.getProfile().pictureStatus
cont = fn2.getContact(fn2MID)
run_bot["fino2"]["videoProfile"] = cont.videoProfile
coverId = fn2.getProfileDetail()["result"]["objectId"]
run_bot["fino2"]["coverId"] = coverId
run_bot['fino3']['AuthToken'] = str(fn3.authToken)
run_bot["fino3"]["Mid"] = fn3MID
run_bot["fino3"]["channelAccessToken"] = str(fn3.tl.channelAccessToken)
run_bot["fino3"]["displayName"] = fn3.getProfile().displayName
run_bot["fino3"]["statusMessage"] = fn3.getProfile().statusMessage
run_bot["fino3"]["pictureStatus"] = fn3.getProfile().pictureStatus
cont = fn3.getContact(fn3MID)
run_bot["fino3"]["videoProfile"] = cont.videoProfile
coverId = fn3.getProfileDetail()["result"]["objectId"]
run_bot["fino3"]["coverId"] = coverId
run_bot['fino4']['AuthToken'] = str(fn4.authToken)
run_bot["fino4"]["Mid"] = fn4MID
run_bot["fino4"]["channelAccessToken"] = str(fn4.tl.channelAccessToken)
run_bot["fino4"]["displayName"] = fn4.getProfile().displayName
run_bot["fino4"]["statusMessage"] = fn4.getProfile().statusMessage
run_bot["fino4"]["pictureStatus"] = fn4.getProfile().pictureStatus
cont = fn4.getContact(fn4MID)
run_bot["fino4"]["videoProfile"] = cont.videoProfile
coverId = fn4.getProfileDetail()["result"]["objectId"]
run_bot["fino4"]["coverId"] = coverId
run_bot['fino5']['AuthToken'] = str(fn5.authToken)
run_bot["fino5"]["Mid"] = fn5MID
run_bot["fino5"]["channelAccessToken"] = str(fn5.tl.channelAccessToken)
run_bot["fino5"]["displayName"] = fn5.getProfile().displayName
run_bot["fino5"]["statusMessage"] = fn5.getProfile().statusMessage
run_bot["fino5"]["pictureStatus"] = fn5.getProfile().pictureStatus
cont = fn5.getContact(fn5MID)
run_bot["fino5"]["videoProfile"] = cont.videoProfile
coverId = fn5.getProfileDetail()["result"]["objectId"]
run_bot["fino5"]["coverId"] = coverId
run_bot['kicker1']['AuthToken'] = str(k1.authToken)
run_bot["kicker1"]["Mid"] = k1MID
run_bot["kicker1"]["channelAccessToken"] = str(k1.tl.channelAccessToken)
run_bot["kicker1"]["displayName"] = k1.getProfile().displayName
run_bot["kicker1"]["statusMessage"] = k1.getProfile().statusMessage
run_bot["kicker1"]["pictureStatus"] = k1.getProfile().pictureStatus
cont = k1.getContact(k1MID)
run_bot["kicker1"]["videoProfile"] = cont.videoProfile
coverId = k1.getProfileDetail()["result"]["objectId"]
run_bot["kicker1"]["coverId"] = coverId
run_bot['kicker2']['AuthToken'] = str(k2.authToken)
run_bot["kicker2"]["Mid"] = k2MID
run_bot["kicker2"]["channelAccessToken"] = str(k2.tl.channelAccessToken)
run_bot["kicker2"]["displayName"] = k2.getProfile().displayName
run_bot["kicker2"]["statusMessage"] = k2.getProfile().statusMessage
run_bot["kicker2"]["pictureStatus"] = k2.getProfile().pictureStatus
cont = k2.getContact(k2MID)
run_bot["kicker2"]["videoProfile"] = cont.videoProfile
coverId = k2.getProfileDetail()["result"]["objectId"]
run_bot["kicker2"]["coverId"] = coverId
with open('logged.json', 'w') as fp:
	json.dump(run_bot, fp, sort_keys=True, indent=4)
try:
    run_bot["assist"] = {}
    run_bot['assist'][myMID] = True
    run_bot['assist'][fn1MID] = True
    run_bot["assist"][fn2MID] = True
    run_bot["assist"][fn3MID] = True
    run_bot["assist"][fn4MID] = True
    run_bot["assist"][fn5MID] = True
    run_bot["assist"][k1MID] = True
    run_bot["assist"][k2MID] = True
    backupData()
except:
    print ("\nSTARTING SYSTEM...")

main = OEPoll(fino)
_FINBOT = run_bot["assist"]
Bots = _FINBOT
admin = run_bot["Admin"]
bbc = run_bot['Creator']
Owner = ["u48732f34a67da3436642249f83d16ade",bbc]
Creator = ["u48732f34a67da3436642249f83d16ade",bbc]
Master = ["u48732f34a67da3436642249f83d16ade",bbc]

FNO = [fn1,fn2,fn3,fn4,fn5]
KAC  = [fn1,fn2,fn3,fn4,fn5]
KICKER = [k1MID,k2MID]
_Random = random.choice(FNO)

protectname = []
msg_dict = {}
msg_dict1 = {}

run = {
    'finbot':True
   }
wait = {
    "clock":False,
    "cName": "> ",
    "AutoTiming": 60
   }
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

def backupData():
    try:
        backup = bot_run
        f = codecs.open('finbot1.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = run_bot
        f = codecs.open('logged.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def command(text):
    pesan = text.lower()
    if pesan.startswith(bot_run["keyCommand"]):
        cmd = pesan.replace(bot_run["keyCommand"],"")
    else:
        cmd = ""
    return cmd
    
def autoRestart():
    if time.time() - botStart > int(bot_run["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()

def restart_program():
    print ("\nRestarted\nPlease Wait...\n")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def restartBot():
    print ("\nRestarting\nPlease Wait...\n")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    fino.log("{}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("error.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                fino.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def mentionMembers2(to, mids=[]):
    if finoMID in mids: mids.remove(finoMID)
    parsed_len = len(mids)//20+1
    result = '╭───「 Mention Members 」\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 FINBOT V5.0 」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            kang.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Hai.. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+bot_run["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n[ FINBOT ]"
        kang.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO Sider Member] Error :\n" + str(error))
        logError(error)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Welcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = kang.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+bot_run["welcome"]+"\nGrup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        kang.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO Welcome Member] Error :\n" + str(error))
        logError(error)

def finbot(alfino):
    global time
    global ast
    global groupParam
    try:
        if alfino.type == 0:
            print('[ 0 ]')
            return

        if alfino.type == 5:
            print('[ 5 ]')
            if bot_run["autoBlock"] == True:
                fino.sendMessage(alfino.param1, "...Autoblock on")
                fino.blockContact(alfino.param1)
        if alfino.type == 5:
            print('[ 5 ]')
            if bot_run["autoAdd"] == True:
                if alfino.param2 not in Bots and alfino.param2 not in Master:
                    if (bot_run["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        fino.findAndAddContactsByMid(alfino.param1)
                        fino.sendMessage(alfino.param1, bot_run["message"])

        if alfino.type == 11:
            print('[ 11 ]')
            if alfino.param1 in bot_run["Pro_Qr"]:
                try:
                    if kang.getGroup(alfino.param1).preventedJoinByTicket == False:
                        if alfino.param2 not in Bots and alfino.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(alfino.param1)
                            k1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            X = k2.getGroup(alfino.param1)
                            X.preventedJoinByTicket = True
                            k2.updateGroup(X)
                            bot_run["Blacklist_User"][alfino.param2] = True
                            k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            k1.leaveGroup(msg.to)
                            k2.leaveGroup(msg.to)
                            _Random.inviteIntoGroup(alfino.param1,[KICKER])
                            kang.sendMessage(to, "Please, Don't open group link settings")
                except:
                    try:
                        if _Random.getGroup(alfino.param1).preventedJoinByTicket == False:
                            if alfino.param2 not in Bots and alfino.param2 not in Master:
                                Ticket = _Random.reissueGroupTicket(alfino.param1)
                                k2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                X = k1.getGroup(alfino.param1)
                                X.preventedJoinByTicket = True
                                k1.updateGroup(X)
                                bot_run["Blacklist_User"][alfino.param2] = True
                                k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k2.leaveGroup(alfino.param1)
                                k1.leaveGroup(msg.to)
                                _Random.inviteIntoGroup(alfino.param1,[KICKER])
                                kang.sendMessage(to, "Please, Don't open group link settings")
                    except:
                        pass
        if alfino.type == 11:
            print('[ 11: Nyusup ]')
            if bot_run["nyusup"] == True:
                try:
                    if fino.getGroup(alfino.param1).preventedJoinByTicket == False:
                        if alfino.param2 not in Bots and alfino.param2 not in Master:
                            Ticket = fino.reissueGroupTicket(alfino.param1)
                            kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                except:
                    pass

        if alfino.type == 11:
            print('[ 11 ]')
            if alfino.param2 in bot_run["Blacklist_User"]:
                try:
                    if kang.getGroup(alfino.param1).preventedJoinByTicket == False:
                    	X = kang.getGroup(alfino.param1)
                    X.preventedJoinByTicket = True
                    kang.updateGroup(X)
                    kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                except:
                    try:
                        if fn1.getGroup(alfino.param1).preventedJoinByTicket == False:
                        	X = fn1.getGroup(alfino.param1)
                        X.preventedJoinByTicket = True
                        fn1.updateGroup(X)
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                    except:
                        try:
                            if fn2.getGroup(alfino.param1).preventedJoinByTicket == False:
                            	X = fn2.getGroup(alfino.param1)
                            X.preventedJoinByTicket = True
                            fn2.updateGroup(X)
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                if fn3.getGroup(alfino.param1).preventedJoinByTicket == False:
                                	fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                X = fn3.getGroup(alfino.param1)
                                X.preventedJoinByTicket = True
                                fn3.updateGroup(X)
                            except:
                                try:
                                    if fn4.getGroup(alfino.param1).preventedJoinByTicket == False:
                                    	fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    X = fn4.getGroup(alfino.param1)
                                    X.preventedJoinByTicket = True
                                    fn4.updateGroup(X)
                                except:
                                    try:
                                        if fn5.getGroup(alfino.param1).preventedJoinByTicket == False:
                                        	fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        X = fn5.getGroup(alfino.param1)
                                        X.preventedJoinByTicket = True
                                        fn5.updateGroup(X)
                                    except:
                                        pass
        if alfino.type == 11:
            print('[ 11 ]')
            if alfino.param3 == '1':
                if alfino.param1 in protectname:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master:
                        	group = kang.getGroup(alfino.param1)
                        group.name = bot_run["pro_name"][alfino.param1]
                        kang.updateGroup(group)
                        kang.sendMessage(alfino.param1, "Group Name protected\nYou have been warned..!")
                        kang.sendMessage(alfino.param1, None, contentMetadata={'mid': alfino.param2}, contentType=13)
                        bot_run["Blacklist_User"][alfino.param2] = True
                    except:
                        pass
        if alfino.type == 11:
            print('[ 11 ]')
            if alfino.param3 == '1':
                if alfino.param1 in bot_run['pname']:
                    try:
                        G = kang.getGroup(alfino.param1)
                    except:
                        try:
                            G = fn1.getGroup(alfino.param1)
                        except:
                            try:
                                G = fn2.getGroup(alfino.param1)
                            except:
                                try:
                                    G = fn3.getGroup(alfino.param1)
                                except:
                                    try:
                                        G = fn4.getGroup(alfino.param1)
                                    except:
                                        try:
                                            G = fn5.getGroup(alfino.param1)
                                        except:
                                            pass
                    G.name = bot_run['pro_name'][alfino.param1]
                    try:
                        kang.updateGroup(G)
                    except:
                        try:
                            fn1.updateGroup(G)
                        except:
                            try:
                                fn2.updateGroup(G)
                            except:
                                try:
                                    fn3.updateGroup(G)
                                except:
                                    try:
                                        fn4.updateGroup(G)
                                    except:
                                        try:
                                            fn5.updateGroup(G)
                                        except:
                                            pass
                    if alfino.param2 in Bots and alfino.param2 in Master:
                        pass
                    else:
                        try:
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    except:
                                        try:
                                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        except:
                                            pass
        if alfino.type == 11 or alfino.type == 2:
            print('[ 2 Pro G img ]')
            if alfino.param1 in bot_run["Pro_Gimage"]:
                if alfino.param2 not in Bots and alfino.param2 not in Creator and alfino.param2 not in kangyat and alfino.param2 not in admin:
                    try:
                        group = fino.updateGroup(alfino.param1)
                        p = [image for midd in group.pictureStatus]
                        for _mid in p:
                            _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                            kang.sendMessage(to,"Please, Don't change group image settings")
                    except:
                        pass

        if alfino.type == 13:
            print('[ 13 ]')
            if finoMID in alfino.param3:
                if bot_run["autoLeave"] == True:
                    if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in Creator and alfino.param2 not in admin:
                        fino.acceptGroupInvitation(alfino.param1)
                        ginfo = fino.getGroup(alfino.param1)
                        contact = fino.getContact(alfino.param2)
                        fino.sendMessage(alfino.param1,"Hallo... " +str(ginfo.name))
                        fino.sendMessage(alfino.param1,"Sorry...! \n" +str(contact.displayName) + " Sedang gk mood... ")
                        fino.leaveGroup(alfino.param1)
                    else:
                        fino.acceptGroupInvitation(alfino.param1)
                        ginfo = fino.getGroup(alfino.param1)
                        fino.sendMessage(alfino.param1,"Hello... " +str(ginfo.name))
        if alfino.type == 13:
            print('[ 13 ]')        	
            if finoMID in alfino.param3:
                G = fino.getGroup(alfino.param1)
                if bot_run["autoJoin"] == True:
                    if bot_run["limiter"]["on"] == True:
                        if len(G.members) <= bot_run["limiter"]["members"]:
                            fino.acceptGroupInvitation(alfino.param1)
                            group = fino.getGroup(alfino.param1)
                            kang.sendMessage(alfino.param1,"Maaf jumlah member\n " + str(group.name) + " kurang dari " + str(bot_run["limiter"]["members"]))
                            fino.leaveGroup(alfino.param1)
                        else:
                            fino.acceptGroupInvitation(alfino.param1)
                    else:
                        fino.acceptGroupInvitation(alfino.param1)
        if alfino.type == 13:
            print('[ 13 ]')
            if myMID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        kang.acceptGroupInvitation(alfino.param1)
                        kang.inviteIntoGroup(alfino.param1,[KICKER])
                    else:
                        kang.acceptGroupInvitation(alfino.param1)
                        kang.inviteIntoGroup(alfino.param1,[KICKER])
                elif bot_run["limiter"]["on"] == True:
                    if len(G.members) <= bot_run["limiter"]["members"]:
                        kang.rejectGroupInvitation(alfino.param1)
            else:
                Inviter = alfino.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in bot_run["Blacklist_User"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kang.cancelGroupInvitation(alfino.param1, matched_list)
        if alfino.type == 13:
            print('[ 13 ]')
            if fn1MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn1.acceptGroupInvitation(alfino.param1)
                    else:
                        fn1.acceptGroupInvitation(alfino.param1)
        if alfino.type == 13:
            print('[ 13 ]')
            if fn2MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn2.acceptGroupInvitation(alfino.param1)
                    else:
                        fn2.acceptGroupInvitation(alfino.param1)
        if alfino.type == 13:
            print('[ 13 ]')
            if fn3MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn3.acceptGroupInvitation(alfino.param1)
                    else:
                        fn3.acceptGroupInvitation(alfino.param1)
        if alfino.type == 13:
            print('[ 13 ]')
            if fn4MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn4.acceptGroupInvitation(alfino.param1)
                    else:
                        fn4.acceptGroupInvitation(alfino.param1)
        if alfino.type == 13:
            print('[ 13 ]')
            if fn5MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn5.acceptGroupInvitation(alfino.param1)
                    else:
                        fn5.acceptGroupInvitation(alfino.param1)
        if alfino.type == 13:
            print('[ 13 ]')
            if alfino.param3 in bot_run["Blacklist_User"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            fn1.cancelGroupInvitation(alfino.param1,[alfino.param3])
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            bot_run["Blacklist_User"][alfino.param2] = True
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                fn2.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                bot_run["Blacklist_User"][alfino.param2] = True
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    fn3.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    bot_run["Blacklist_User"][alfino.param2] = True
                            except:
                                try:
                                    if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                        fn4.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        bot_run["Blacklist_User"][alfino.param2] = True
                                except:
                                    try:
                                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                            fn5.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            bot_run["Blacklist_User"][alfino.param2] = True
                                    except:
                                        pass
        if alfino.type == 13:
            print('[ 13 ]')
            if alfino.param1 in bot_run["Pro_Invite"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            fn1.cancelGroupInvitation(alfino.param1,[alfino.param3])
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            bot_run["Blacklist_User"][alfino.param2] = True
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                fn2.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                bot_run["Blacklist_User"][alfino.param2] = True
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    fn3.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    bot_run["Blacklist_User"][alfino.param2] = True
                            except:
                                try:
                                    if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                        fn4.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        bot_run["Blacklist_User"][alfino.param2] = True
                                except:
                                    try:
                                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                            fn5.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            bot_run["Blacklist_User"][alfino.param2] = True
                                    except:
                                        pass
        if alfino.type == 17:
            print('[ 17 ]')
            if alfino.param2 in bot_run["Blacklist_User"]:
         #       elif alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    except:
                                        pass

        if alfino.type == 17:
            print('[ 17 ]')
            if alfino.param1 in bot_run["Pro_Join"]:
                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    except:
                                        pass

        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param1 in bot_run["Pro_Member"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            with open('finbot1.json','w') as fp:
                                json.dump(bot_run, fp, sort_keys=True, indent=4)
                            user = kang.getContact(alfino.param2)
                            kang.sendMessage(alfino.param1,"Don't expel members in this group " + str(user.displayName))
                            try:
                                if alfino.param3 not in bot_run["Blacklist_User"]:
                                    _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    _Random.findAndAddContactsByMid(alfino.param3)
                                    _Random.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    if alfino.param3 not in bot_run["Blacklist_User"]:
                                        _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        _Random.findAndAddContactsByMid(alfino.param3)
                                        _Random.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    pass
                        else:
                            pass
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                bot_run["Blacklist_User"][alfino.param2] = True
                                with open('finbot1.json','w') as fp:
                                    json.dump(bot_run, fp, sort_keys=True, indent=4)
                                k1.acceptGroupInvitation(alfino.param1)
                                k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k1.findAndAddContactsByMid(alfino.param3)
                                k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                x = k1.getGroup(alfino.param1)
                                x.preventedJoinByTicket = False
                                k1.updateGroup(x)
                                invsend = 0
                                Ti = k1.reissueGroupTicket(alfino.param1)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                Ticket = k1.reissueGroupTicket(alfino.param1)
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    bot_run["Blacklist_User"][alfino.param2] = True
                                    with open('finbot1.json','w') as fp:
                                    	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                    k2.acceptGroupInvitation(alfino.param1)
                                    k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    k2.findAndAddContactsByMid(alfino.param3)
                                    k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    x = k2.getGroup(alfino.param1)
                                    x.preventedJoinByTicket = False
                                    k2.updateGroup(x)
                                    invsend = 0
                                    Ti = k2.reissueGroupTicket(alfino.param1)
                                    fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    Ticket = k2.reissueGroupTicket(alfino.param1)
                            except:
                            	pass

        if alfino.type == 19:
            print('[ 19 ]')        	
            if alfino.param3 in Creator:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k1.acceptGroupInvitation(alfino.param1)
                        k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                        k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        x = k1.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k1.reissueGroupTicket(alfino.param1)
                        k1.leaveGroup(alfino.param1)
                        _Random.inviteIntoGroup(alfino.param1,[k1MID])
                    except:
                        try:
                           k2.acceptGroupInvitation(alfino.param1)
                           k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                           k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                           x = k2.getGroup(alfino.param1)
                           x.preventedJoinByTicket = False
                           k2.updateGroup(x)
                           invsend = 0
                           Ti = k2.reissueGroupTicket(alfino.param1)
                           fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           Ticket = k2.reissueGroupTicket(alfino.param1)
                           k2.leaveGroup(alfino.param1)
                           _Random.inviteIntoGroup(alfino.param1,[k2MID])
                        except:
                            pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in finoMID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k1.acceptGroupInvitation(alfino.param1)
                        k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                        k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        x = k1.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k1.reissueGroupTicket(alfino.param1)
                        k1.leaveGroup(alfino.param1)
                        _Random.inviteIntoGroup(alfino.param1,[k1MID])
                    except:
                        try:
                           k2.acceptGroupInvitation(alfino.param1)
                           k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                           k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                           x = k2.getGroup(alfino.param1)
                           x.preventedJoinByTicket = False
                           k2.updateGroup(x)
                           invsend = 0
                           Ti = k2.reissueGroupTicket(alfino.param1)
                           fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           Ticket = k2.reissueGroupTicket(alfino.param1)
                           k2.leaveGroup(alfino.param1)
                           _Random.inviteIntoGroup(alfino.param1,[k2MID])
                        except:
                            pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in myMID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                        kang.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                            kang.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                kang.acceptGroupInvitation(alfino.param1)
                            except:
                                try:
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    kang.acceptGroupInvitation(alfino.param1)
                                except:
                                    try:
                                        k2.acceptGroupInvitation(alfino.param1)
                                        k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        k2.inviteIntoGroup(alfino.param1,alfino.param3)
                                        x = k2.getGroup(alfino.param1)
                                        x.preventedJoinByTicket = False
                                        k2.updateGroup(x)
                                        invsend = 0
                                        Ti = k2.reissueGroupTicket(alfino.param1)
                                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        Ticket = k2.reissueGroupTicket(alfino.param1)
                                        k2.leaveGroup(alfino.param1)
                                        _Random.inviteIntoGroup(alfino.param1,[k2MID])
                                    except:
                                        try:
                                            k1.acceptGroupInvitation(alfino.param1)
                                            k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            k1.inviteIntoGroup(alfino.param1,alfino.param3)
                                            x = k1.getGroup(alfino.param1)
                                            x.preventedJoinByTicket = False
                                            k1.updateGroup(x)
                                            invsend = 0
                                            Ti = k1.reissueGroupTicket(alfino.param1)
                                            fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            Ticket = k1.reissueGroupTicket(alfino.param1)
                                            k1.leaveGroup(alfino.param1)
                                            _Random.inviteIntoGroup(alfino.param1,[k1MID])
                                        except:
                                            pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in fn1MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn1.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn1.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn4.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn4.updateGroup(G)
                                Ticket = fn4.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn4.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn4.updateGroup(G)
                            except:
                                try:
                                    fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn1.acceptGroupInvitation(alfino.param1)
                                except:
                                    try:
                                        kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn1.acceptGroupInvitation(alfino.param1)
                                    except:
                                        try:
                                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn2.inviteIntoGroupGroup(alfino.param1,[alfino.param2])
                                            fn1.acceptGroupInvitation(alfino.param1)
                                        except:
                                            pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in fn2MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn2.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn2.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn5.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn5.updateGroup(G)
                                Ticket = fn5.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn5.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn5.updateGroup(G)
                            except:
                                try:
                                    kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn2.acceptGroupInvitation(alfino.param1)
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn2.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in fn3MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn3.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn3.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = kang.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                Ticket = kang.reissueGroupTicket(alfino.param1)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = kang.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                kang.updateGroup(G)
                            except:
                                try:
                                    fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn3.acceptGroupInvitation(alfino.param1)
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn3.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in fn4MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn4.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                            kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn4.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn1.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn1.updateGroup(G)
                                Ticket = fn1.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn1.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn1.updateGroup(G)
                            except:
                                try:
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn4.acceptGroupInvitation(alfino.param1)
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn4.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in fn5MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                        kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn5.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn5.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn2.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn2.updateGroup(G)
                                Ticket = fn2.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn2.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn2.updateGroup(G)
                            except:
                                try:
                                    fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn5.acceptGroupInvitation(alfino.param1)
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn5.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in k1MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k2.acceptGroupInvitation(alfino.param1)
                        k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                        x = k2.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k2.updateGroup(x)
                        invsend = 0
                        Ti = k2.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k2.reissueGroupTicket(alfino.param1)
                    except:
                        pass
                return
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in k2MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                        _Random.inviteIntoGroup(alfino.param1,[alfino.param3])
                        x = _Random.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        _Random.updateGroup(x)
                        invsend = 0
                        Ti = _Random.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = _Random.reissueGroupTicket(alfino.param1)
                    except:
                        pass
        if alfino.type == 19:
            print('[ 19 ]')
            if alfino.param3 in admin:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn1.findAndAddContactsByMid(alfino.param3)
                        fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn2.findAndAddContactsByMid(alfino.param3)
                            fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                        except:
                            try:
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn3.findAndAddContactsByMid(alfino.param3)
                                fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn4.findAndAddContactsByMid(alfino.param3)
                                    fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn5.findAndAddContactsByMid(alfino.param3)
                                        fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            kang.findAndAddContactsByMid(alfino.param3)
                                            kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            pass
                return

        if alfino.type == 32:
            print('[ 32 ]')
            if alfino.param1 in bot_run["Pro_Cancel"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            with open('finbot1.json','w') as fp:
                                json.dump(bot_run, fp, sort_keys=True, indent=4)
                            user = kang.getContact(alfino.param2)
                            kang.sendMessage(alfino.param1,"No permission!! You're not an admin\nPlease Do not cancel for a group member invited\nYou have been warned: " + str(user.displayName))
                            try:
                                if alfino.param3 not in bot_run["Blacklist_User"]:
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn1.findAndAddContactsByMid(alfino.param3)
                                    fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    if alfino.param3 not in bot_run["Blacklist_User"]:
                                        fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn2.findAndAddContactsByMid(alfino.param3)
                                        fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        if alfino.param3 not in bot_run["Blacklist_User"]:
                                        	fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.findAndAddContactsByMid(alfino.param3)
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            if alfino.param3 not in bot_run["Blacklist_User"]:
                                            	fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn4.findAndAddContactsByMid(alfino.param3)
                                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            try:
                                               if alfino.param3 not in bot_run["Blacklist_User"]:
                                               	fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                               fn5.findAndAddContactsByMid(alfino.param3)
                                               fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                                            except:
                                                pass
                        else:
                            pass
                    except:
                        pass

        if alfino.type == 32:
            print('[ 32 ]')
            if alfino.param3 in k1MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            try:
                                fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            try:
                                               fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                               fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                                            except:
                                                try:
                                                   k2.acceptGroupInvitation(alfino.param1)
                                                   k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                                   k2.findAndAddContactsByMid(alfino.param3)
                                                   k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                                   x = k2.getGroup(alfino.param1)
                                                   x.preventedJoinByTicket = False
                                                   k2.updateGroup(x)
                                                   invsend = 0
                                                   Ti = k2.reissueGroupTicket(alfino.param1)
                                                   fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   Ticket = k2.reissueGroupTicket(alfino.param1)
                                                except:
                                                    pass
                        else:
                            pass
                    except:
                        pass
        if alfino.type == 32:
            print('[ 32 ]')
            if alfino.param3 in k2MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in Owner:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            try:
                                fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            try:
                                               fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                               fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                                            except:
                                                try:
                                                   k1.acceptGroupInvitation(alfino.param1)
                                                   k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                                   k1.findAndAddContactsByMid(alfino.param3)
                                                   k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                                   x = k1.getGroup(alfino.param1)
                                                   x.preventedJoinByTicket = False
                                                   k1.updateGroup(x)
                                                   invsend = 0
                                                   Ti = k1.reissueGroupTicket(alfino.param1)
                                                   fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                                   Ticket = k1.reissueGroupTicket(alfino.param1)
                                                except:
                                                    pass
                        else:
                            pass
                    except:
                        pass

        if alfino.type == 25 or alfino.type == 26:
            print('[ 26 ]')
            msg = alfino.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 1:
                 if sender in Creator or sender in kangyat:
                    if bot_run["changePicture"] == True:
                       path = kang.downloadObjectMsg(msg_id)
                       path1 = fn1.downloadObjectMsg(msg_id)
                       path2 = fn2.downloadObjectMsg(msg_id)
                       path3 = fn3.downloadObjectMsg(msg_id)
                       path4 = fn4.downloadObjectMsg(msg_id)
                       path5 = fn5.downloadObjectMsg(msg_id)
                       bot_run["changePicture"] = False
                       kang.updateProfilePicture(path)
                       kang.sendMention(to,sender,cft())
                       fn1.updateProfilePicture(path1)
                       fn1.sendMention(to,sender,cft())
                       fn2.updateProfilePicture(path2)
                       fn2.sendMention(to,sender,cft())
                       fn3.updateProfilePicture(path3)
                       fn3.sendMention(to,sender,cft())
                       fn4.updateProfilePicture(path4)
                       fn4.sendMention(to,sender,cft())
                       fn5.updateProfilePicture(path5)
                       fn5.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                    if bot_run["kickerPicture"] == True:
                       path1 = k1.downloadObjectMsg(msg_id)
                       path2 = k2.downloadObjectMsg(msg_id)
                       bot_run["kickerPicture"] = False
                       k1.updateProfilePicture(path1)
                       k1.sendMention(to,sender,cft())
                       k2.updateProfilePicture(path2)
                       k2.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                    if bot_run["changePictureCover"] == True:
                       path = kang.downloadObjectMsg(msg_id, saveAs='temp/cover.jpg')
                       pa = fn1.downloadObjectMsg(msg_id, saveAs='temp/cover1.jpg')
                       paa = fn2.downloadObjectMsg(msg_id, saveAs='temp/cover2.jpg')
                       paaa = fn3.downloadObjectMsg(msg_id, saveAs='temp/cover3.jpg')
                       paaaa = fn4.downloadObjectMsg(msg_id, saveAs='temp/cover4.jpg')
                       paaaaa = fn5.downloadObjectMsg(msg_id, saveAs='temp/cover5.jpg')
                       bot_run["changePictureCover"] = False
                       kang.updateProfileCover(path)
                       fn1.updateProfileCover(pa)
                       fn2.updateProfileCover(paa)
                       fn3.updateProfileCover(paaa)
                       fn4.updateProfileCover(paaaa)
                       fn5.updateProfileCover(paaaaa)
                       kang.sendMention(to,sender,cft())
                       fn1.sendMention(to,sender,cft())
                       fn2.sendMention(to,sender,cft())
                       fn3.sendMention(to,sender,cft())
                       fn4.sendMention(to,sender,cft())
                       fn5.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if finoMID in bot_run["foto"]:
                         path = fino.downloadObjectMsg(msg.id,saveAs='temp/fino.jpg')
                         del bot_run["foto"][finoMID]
                         fino.updateProfilePicture(path)
                         fino.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if myMID in bot_run["foto"]:
                         path = kang.downloadObjectMsg(msg.id,saveAs='temp/kang.jpg')
                         del bot_run["foto"][myMID]
                         kang.updateProfilePicture(path)
                         kang.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if fn1MID in bot_run["foto"]:
                         path = fn1.downloadObjectMsg(msg.id,saveAs='temp/fn1.jpg')
                         del bot_run["foto"][fn1MID]
                         fn1.updateProfilePicture(path)
                         fn1.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if fn2MID in bot_run["foto"]:
                         path = fn2.downloadObjectMsg(msg.id,saveAs='temp/fn2.jpg')
                         del bot_run["foto"][fn2MID]
                         fn2.updateProfilePicture(path)
                         fn2.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if fn3MID in bot_run["foto"]:
                         path = fn3.downloadObjectMsg(msg.id,saveAs='temp/fn3.jpg')
                         del bot_run["foto"][fn3MID]
                         fn3.updateProfilePicture(path)
                         fn3.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if fn4MID in bot_run["foto"]:
                         path = fn4.downloadObjectMsg(msg.id,saveAs='temp/fn4.jpg')
                         del bot_run["foto"][fn4MID]
                         fn4.updateProfilePicture(path)
                         fn4.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if fn5MID in bot_run["foto"]:
                         path = fn5.downloadObjectMsg(msg.id,saveAs='temp/fn5.jpg')
                         del bot_run["foto"][fn5MID]
                         fn5.updateProfilePicture(path)
                         fn5.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if k1MID in bot_run["foto"]:
                         path = k1.downloadObjectMsg(msg.id,saveAs='temp/kicker1.jpg')
                         del bot_run["foto"][k1MID]
                         k1.updateProfilePicture(path)
                         k1.sendMention(to,sender,cft())
                 if sender in Creator or sender in kangyat:
                     if k2MID in bot_run["foto"]:
                         path = k2.downloadObjectMsg(msg.id,saveAs='temp/kicker2.jpg')
                         del bot_run["foto"][k2MID]
                         k2.updateProfilePicture(path)
                         k2.sendMention(to,sender,cft())
               if msg.contentType == 2:
                   if sender in Creator or sender in kangyat:
                       if myMID in bot_run["video"]:
                            path = kang.downloadObjectMsg(msg_id)
                            del bot_run["video"][myMID]
                            kang.updateProfileVideoPicture(path)
                            kang.sendMention(to,sender,cft())
               if msg.toType == 2:
                 if sender in Creator or sender in kangyat:
                   if bot_run["groupPicture"] == True:
                     path = kang.downloadObjectMsg(msg_id,saveAs='temp/group.jpg')
                     bot_run["groupPicture"] = False
                     kang.updateGroupPicture(msg.to, path)
                     kang.sendMention(to,sender,cft())
               if msg.contentType == 13:
                  if bot_run["invite"] == True:
                    if sender in Master or sender in admin or sender in kangyat:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kang.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                kang.sendMessage(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                kang.sendMessage(to,"Failure invitation, " + _name + "Blacklist user")
                                kang.sendMessage(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kang.findAndAddContactsByMid(target)
                                    kang.inviteIntoGroup(msg.to,[target])
                                    kang.sendMessage(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite"] = False
                                    break
                                except:
                                    try:
                                        kang.findAndAddContactsByMid(invite)
                                        kang.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite"] = False
                                    except:
                                        kang.sendMessage(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite"] = False
                                        break
               if msg.contentType == 13:
                  if bot_run["invite1"] == True:
                    if sender in Master or sender in admin or sender in kangyat:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fn1.sendMessage(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                fn1.sendMessage(to,"Failure invitation, " + _name + "Blacklist user")
                                fn1.sendMessage(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn1.findAndAddContactsByMid(target)
                                    fn1.inviteIntoGroup(msg.to,[target])
                                    fn1.sendMessage(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite1"] = False
                                    break
                                except:
                                    try:
                                        fn1.findAndAddContactsByMid(invite)
                                        fn1.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite1"] = False
                                    except:
                                        fn1.sendMessage(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite1"] = False
                                        break
               if msg.contentType == 13:
                  if bot_run["invite2"] == True:
                    if sender in Master or sender in admin or sender in kangyat:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fn2.sendMessage(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                fn2.sendMessage(to,"Failure invitation, " + _name + "Blacklist user")
                                fn2.sendMessage(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn2.findAndAddContactsByMid(target)
                                    fn2.inviteIntoGroup(msg.to,[target])
                                    fn2.sendMessage(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite1"] = False
                                    break
                                except:
                                    try:
                                        fn2.findAndAddContactsByMid(invite)
                                        fn2.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite2"] = False
                                    except:
                                        fn2.sendMessage(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite2"] = False
                                        break
               if msg.contentType == 13:
                  if bot_run["invite3"] == True:
                    if sender in Master or sender in admin or sender in kangyat:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn3.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fn3.sendMessage(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                fn3.sendMessage(to,"Failure invitation, " + _name + "Blacklist user")
                                fn3.sendMessage(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn3.findAndAddContactsByMid(target)
                                    fn3.inviteIntoGroup(msg.to,[target])
                                    fn3.sendMessage(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite3"] = False
                                    break
                                except:
                                    try:
                                        fn3.findAndAddContactsByMid(invite)
                                        fn3.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite3"] = False
                                    except:
                                        fn3.sendMessage(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite3"] = False
                                        break
               if msg.contentType == 13:
                  if bot_run["invite4"] == True:
                    if sender in Master or sender in admin or sender in kangyat:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn4.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fn4.sendMessage(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                fn4.sendMessage(to,"Failure invitation, " + _name + "Blacklist user")
                                fn4.sendMessage(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn4.findAndAddContactsByMid(target)
                                    fn4.inviteIntoGroup(msg.to,[target])
                                    fn4.sendMessage(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite4"] = False
                                    break
                                except:
                                    try:
                                        fn4.findAndAddContactsByMid(invite)
                                        fn4.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite4"] = False
                                    except:
                                        fn4.sendMessage(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite4"] = False
                                        break
               if msg.contentType == 13:
                  if bot_run["invite5"] == True:
                    if sender in Master or sender in admin or sender in kangyat:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn5.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fn5.sendMessage(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                fn5.sendMessage(to,"Failure invitation, " + _name + "Blacklist user")
                                fn5.sendMessage(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn5.findAndAddContactsByMid(target)
                                    fn5.inviteIntoGroup(msg.to,[target])
                                    fn5.sendMessage(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite5"] = False
                                    break
                                except:
                                    try:
                                        fn5.findAndAddContactsByMid(invite)
                                        fn5.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite5"] = False
                                    except:
                                        fn5.sendMessage(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite5"] = False
                                        break

               if msg.contentType == 13:
                 if bot_run["contact"] == True:
                    msg.contentType = 0
                    kang.sendMessage(to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kang.getContact(msg.contentMetadata["mid"])
                        path = kang.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        kang.sendMessage(to,"♐ Nama : " + msg.contentMetadata["displayName"] + "\n♐ MID : " + msg.contentMetadata["mid"] + "\n♐ Status Msg : " + contact.statusMessage + "\n♐ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        kang.sendImageWithURL(msg.to, image)
                 if bot_run["addContact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        kang.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        fn1.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        fn2.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        fn3.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        fn4.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        fn5.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["addContact"] = False
                 if bot_run["botAdd"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        kang.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["botAdd"] = False
                 if bot_run["bot1Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        fn1.findAndAddContactsByMid(target)
                        fn1.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot1Add"] = False
                 if bot_run["bot2Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        fn2.findAndAddContactsByMid(target)
                        fn2.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot2Add"] = False
                 if bot_run["bot3Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        fn3.findAndAddContactsByMid(target)
                        fn3.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot3Add"] = False
                 if bot_run["bot4Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        fn4.findAndAddContactsByMid(target)
                        fn4.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot4Add"] = False
                 if bot_run["bot5Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        fn5.findAndAddContactsByMid(target)
                        fn5.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot5Add"] = False
                 if bot_run["kickerAdd"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        k1.findAndAddContactsByMid(target)
                        k1.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        k2.findAndAddContactsByMid(target)
                        k2.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                 if sender in Master or sender in admin or sender in kangyat:
                  if bot_run["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Blacklist_User"]:
                        kang.getMention(to,"This user is already blacklist @!",[sender])
                        bot_run["wblacklist"] = False
                    else:
                        bot_run["wblacklist"] = True
                        bot_run["Blacklist_User"][msg.contentMetadata["mid"]] = True
                        kang.sendMessage(to,"Add to Blacklist user")
                        bot_run["wblacklist"] = False
                 if sender in Master or sender in admin or sender in kangyat:
                  if bot_run["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Blacklist_User"]:
                        del bot_run["Blacklist_User"][msg.contentMetadata["mid"]]
                        kang.getMention(to,"Blacklist deleted @!",[sender])
                        bot_run["dblacklist"] = False
                    else:
                        kang.sendMessage(to,"No blacklist")
                        bot_run["dblacklist"] = False
                 if sender in Creator or sender in kangyat:
                  if bot_run["addAdmin"] == True:
                    if msg.contentMetadata["mid"] in run_bot["Admin"]:
                        kang.getMention(to,"This user is an admin @!",[sender])
                        bot_run["addAdmin"] = False
                    else:
                        bot_run["addAdmin"] = True
                        run_bot["Admin"][msg.contentMetadata["mid"]] = True
                        kang.getMention(to,"User has been added as an admin @!",[sender])
                        bot_run["addAdmin"] = False
                 if sender in Creator or sender in kangyat:
                  if bot_run["delAdmin"] == True:
                    if msg.contentMetadata["mid"] in run_bot["Admin"]:
                        del run_bot["Admin"][msg.contentMetadata["mid"]]
                        kang.getMention(to,"This user is not an admin @!",[sender])
                        bot_run["delAdmin"] = False
                    else:
                        bot_run["delAdmin"] = True
                        kang.getMention(to,"Admin has been removed @!",[sender])
                        bot_run["delAdmin"] = False
               if msg.contentType == 0:
                    if bot_run["AutoRead"] == True:
                        kang.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == 'finbot on':
                            if sender in Creator or sender in kangyat or sender in admin:
                                run["finbot"] = True
                                kang.sendMessage(to, "Bot@Relogin")
                        elif cmd == "finbot off":
                            if sender in Creator or sender in kangyat or sender in admin:
                                run["finbot"] = False
                                kang.sendMessage(to, "system Logout")
                        elif cmd == 'help':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               kang.sendReplyMessage(msg_id, to, help())
                        elif cmd == "about":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                               kang.sendReplyMessage(msg_id, to,inventory())
                        elif cmd == "k1 stay":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                kang.inviteIntoGroup(msg.to,[k1MID])
                        elif cmd == "k2 stay":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                kang.inviteIntoGroup(msg.to,[k2MID])
                        elif cmd == "stay all":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                kang.inviteIntoGroup(msg.to,[k1MID,k2MID])
                        elif cmd == ", ":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                fino.inviteIntoGroup(msg.to,[myMID])
                                kang.acceptGroupInvitation(msg.to)
                        elif cmd == "crot" or cmd == ". ":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                fino.inviteIntoGroup(msg.to,[myMID,fn1MID,fn2MID,fn3MID,fn4MID,fn5MID,k1MID,k2MID])
                                kang.acceptGroupInvitation(msg.to)
                                fn1.acceptGroupInvitation(msg.to)
                                fn2.acceptGroupInvitation(msg.to)
                                fn3.acceptGroupInvitation(msg.to)
                                fn4.acceptGroupInvitation(msg.to)
                                fn5.acceptGroupInvitation(msg.to)
                        elif cmd == "in stand" or cmd == "js in stand":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                fn1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn1.inviteIntoGroup(msg.to,[k1MID])
                                fn2.inviteIntoGroup(msg.to,[k2MID])
                                G = fn3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fn3.updateGroup(G)
                        elif cmd == "finbot in" or cmd == "fin in":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                fn1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kang.updateGroup(G)
                        elif cmd == "kicker in" or cmd == "k in":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k2.updateGroup(G)
                        elif cmd == "kickerbye" or cmd == "k bye":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                        elif cmd == "kicker rein" or cmd == "k rein":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                fn1.inviteIntoGroup(msg.to,k1MID)
                                fn2.inviteIntoGroup(msg.to,k2MID)
                        elif cmd == "byeall" or cmd == "bye bye" or cmd == '... ':
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                                fn1.leaveGroup(msg.to)
                                fn2.leaveGroup(msg.to)
                                fn3.leaveGroup(msg.to)
                                fn4.leaveGroup(msg.to)
                                fn5.leaveGroup(msg.to)
                        elif cmd == "absen":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat or sender in admin:
                                fn1.sendMessage(to,fn1.getProfile().displayName)
                                fn2.sendMessage(to,fn2.getProfile().displayName)
                                fn3.sendMessage(to,fn3.getProfile().displayName)
                                fn4.sendMessage(to,fn4.getProfile().displayName)
                                fn5.sendMessage(to,fn5.getProfile().displayName)
                        elif cmd == "all respon":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat or sender in admin:
                                fn1.sendMessage(to,fn1.getProfile().displayName)
                                fn2.sendMessage(to,fn2.getProfile().displayName)
                                fn3.sendMessage(to,fn3.getProfile().displayName)
                                fn4.sendMessage(to,fn4.getProfile().displayName)
                                fn5.sendMessage(to,fn5.getProfile().displayName)
                        elif cmd == "check":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat or sender in admin:
                                fn1.sendMessage(to, kang.getContact(fn1MID).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+kang.getContact(fn1MID).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~finbot01', 'type': 'mt', 'subText': "Already... ", 'a-installUrl': 'https://line.me/ti/p/~finbot01', 'a-installUrl': ' https://line.me/ti/p/~finbot01', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~finbot01', 'i-linkUri': 'https://line.me/ti/p/~finbot01', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~finbot01'}, contentType=19)
                                fn2.sendMessage(to, kang.getContact(fn2MID).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+kang.getContact(fn2MID).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~finbot02', 'type': 'mt', 'subText': "Already...  ", 'a-installUrl': 'https://line.me/ti/p/~finbot02', 'a-installUrl': ' https://line.me/ti/p/~finbot02', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~finbot02', 'i-linkUri': 'https://line.me/ti/p/~finbot02', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~finbot02'}, contentType=19)
                                fn3.sendMessage(to, kang.getContact(fn3MID).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+kang.getContact(fn3MID).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~finbot03', 'type': 'mt', 'subText': "Already... . ", 'a-installUrl': 'https://line.me/ti/p/~finbot03', 'a-installUrl': ' https://line.me/ti/p/~finbot03', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~finbot03', 'i-linkUri': 'https://line.me/ti/p/~finbot03', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~finbot03'}, contentType=19)
                                fn4.sendMessage(to, kang.getContact(fn4MID).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+kang.getContact(fn4MID).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~finbot04', 'type': 'mt', 'subText': "Already... ", 'a-installUrl': 'https://line.me/ti/p/~finbot04', 'a-installUrl': ' https://line.me/ti/p/~finbot04', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~finbot04', 'i-linkUri': 'https://line.me/ti/p/~finbot04', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~finbot04'}, contentType=19)
                                fn5.sendMessage(to, kang.getContact(fn5MID).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+kang.getContact(fn5MID).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~finbot05', 'type': 'mt', 'subText': "Already... ", 'a-installUrl': 'https://line.me/ti/p/~finbot05', 'a-installUrl': ' https://line.me/ti/p/~finbot05', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~finbot05', 'i-linkUri': 'https://line.me/ti/p/~finbot05', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~finbot05'}, contentType=19)
                        elif cmd == "me" or msg.text.lower() == 'me':
                          if run["finbot"] == True:
                          	contact = fino.getContact(sender)
                          status = contact.statusMessage
                          fino.sendMessage(to, contact.displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+contact.pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~kangnur04', 'type': 'mt', 'subText': status, 'a-installUrl': 'https://line.me/ti/p/~kangnur04', 'a-installUrl': ' https://line.me/ti/p/~kangnur04', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~kangnur04', 'i-linkUri': 'https://line.me/ti/p/~kangnur04', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~kangnur04'}, contentType=19)
                        elif "Inviteme: " in msg.text:
                          if sender in Creator or sender in kangyat:
                            gid = msg.text.replace("Inviteme: ","")
                            if gid == "":
                                fino.sendMessage(to,fail())
                            else:
                                try:
                                    fino.findAndAddContactsByMid(sender)
                                    fino.inviteIntoGroup(gid,[sender])
                                except:
                                    fino.sendMessage(to,fail())
                        elif cmd == "setting" or cmd == 'settbot':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╔═══════════\n"
                                md+="║۝🄵🄸🄽 🄱🄾🅃۝\n"
                                md+="╠═══════════\n"
                                if bot_run["autoJoin"] == True: md+="║❏〘 Auto join 〙『 📲 』\n"
                                else: md+="║❏〘 Auto join 〙『 📴 』\n"
                                if bot_run["autoAdd"] == True: md+="║❏〘 Auto add 〙『 📲 』\n"
                                else: md+="║❏〘 Auto add 〙『 📴 』\n"
                                if bot_run["autoBlock"] == True: md+="║❏〘 Auto block 〙『 📲 』\n"
                                else: md+="║❏〘 Auto block 〙『 📴 』\n"
                                if bot_run["autoLeave"] == True: md+="║❏〘 Auto leave 〙『 📲 』\n"
                                else: md+="║❏〘 Auto leave 〙『 📴 』\n"
                                if bot_run["AutoRead"] == True: md+="║❏〘 Auto read 〙『 📲 』\n"
                                else: md+="║❏〘 Auto read 〙『 📴 』\n"
                                if bot_run["invite"] == True: md+="║❏〘 Auto Inv 〙『 📲 』\n"
                                else: md+="║❏〘 Auto Inv 〙『 📴 』\n"
                                if bot_run["autokick"] == True: md+="║❏〘 Warning 〙『 📲 』\n"
                                else: md+="║❏〘 Warning 〙『 📴 』\n"
                                if bot_run["checkPost"] == True: md+="║❏〘 CheckPost 〙『 📲 』\n"
                                else: md+="║❏〘 CheckPost 〙『 📴 』\n"
                                if bot_run["contact"] == True: md+="║❏〘 Contact 〙『 📲 』\n"
                                else: md+="║❏〘 Contact 〙『 📴 』\n"
                                if bot_run["changePicture"] == True: md+="║❏〘 Change pict 〙『 📲 』\n"
                                else: md+="║❏〘 Change pict 〙『 📴 』\n"
                                if bot_run["nyusup"] == True: md+="║❏〘 Mode Nyusup 〙『 📲 』\n"
                                else: md+="║❏〘 Mode Nyusup 〙『 📴 』\n"
                                if bot_run["limiter"]["on"] == True: md+="║❏〘 limiter 〙" + "『 " + str(bot_run["limiter"]["members"]) + " 』" + "\n"
                                else: md+="􀠁􀆩􏿿║❏〘 limiter 〙:『 📴 』\n"
                                if bot_run["scanner"] == True: md+="║❏〘 Scanner 〙『 📲 』\n"
                                else: md+="║❏〘 Scanner 〙『 📴 』\n"
                                if bot_run["detectMention"] == True: md+="║❏〘 Respon 〙『 📲 』\n"
                                else: md+="║❏〘 Respon 〙『 📴 』\n"
                                if bot_run["detectMention1"] == True: md+="║❏〘 Respon cont 〙『 📲 』\n"
                                else: md+="║❏〘 Respon cont 〙『 📴 』\n"
                                if bot_run["ResponPc"] == True: md+="║❏〘 Respon PC 〙『 📲 』\n"
                                else: md+="║❏〘 Respon PC 〙『 📴 』\n"
                                if bot_run["MentionKick"] == True: md+="║❏〘 Respon kick 〙『 📲 』\n"
                                else: md+="║❏〘 Respon kick 〙『 📴 』\n"
                                if bot_run["unsendMessage"] == True: md+="║❏〘 unsend Msg 〙『 📲 』\n"
                                else: md+="║❏〘 unsend Msg 〙『 📴 』\n"
                                if msg.to in bot_run["Welcome"]: md+="║❏〘 Welcome 〙『 📲 』\n"
                                else: md+="║❏〘 Welcome 〙『 📴 』\n"
                                if bot_run["pname"] == True: md+="║❏〘 Lockname 〙『 📲 』\n"
                                else: md+="║❏〘 Lockname 〙『 📴 』\n╚═══════════\n"
                                kang.sendMessage(to, md+"╔═══════════\n" + "║〘 日付 〙: ["+ datetime.strftime(timeNow,'%Y-%m-%d')+"]\n" + "╠═══════════\n" + "║〘 時間 〙[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n" + "╚═══════════")

                        elif cmd == "settpro" or cmd == 'sett protect':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md ="\n"
                                md+="[ PROTECTION ]\n"
                                md+="\n"
                                if msg.to in bot_run["Pro_Qr"]: md+="Pro QR [ ON ]\n"
                                else: md+="Pro QR [ OFF ]\n"
                                if msg.to in bot_run["Pro_Join"]: md+="Pro Joined [ ON ]\n"
                                else: md+="Pro Joined [ OFF ]\n"
                                if msg.to in bot_run["Pro_Member"]: md+="Pro Member [ ON ]\n"
                                else: md+="Pro Member [ OFF ]\n"
                                if msg.to in bot_run["Pro_Invite"]: md+="Pro Invite [ ON ]\n"
                                else: md+="Pro Invite [ OFF ]\n"
                                if msg.to in bot_run["Pro_Cancel"]: md+="Pro cancel [ ON ]\n"
                                else: md+="Pro cancel [ OFF ]\n"
                                kang.sendMessage(msg.to, md+"\n" + "["+ datetime.strftime(timeNow,'%Y-%m-%d')+"]\n" + "[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n" + "")
                        elif cmd == "costumer":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                ma = ""
                                mb = ""
                                a = 0
                                b = 0
                                for m_id in Creator:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kang.getContact(m_id).displayName + "\n"
                                kang.sendMessage(msg.to,"[ FINBOT]\n\nMaster:\n"+ma+"\nAdmin:\n"+mb+"\nTotal [ %s ]FINBOT" %(str(len(Creator)+len(run_bot["Admin"]))))
                        elif cmd == "listpro":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                mg = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                g = 0
                                gid = bot_run["Pro_Qr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Member"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Join"]
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    md += str(d) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Cancel"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    mc += str(c) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["pname"]
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Invite"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +kang.getGroup(group).name + "\n"
                                kang.sendMessage(msg.to,"\nCustom Protection\n\nURL Pro :\n"+ma+"\nKICKER Pro :\n"+mb+"\nJOINER Pro  :\n"+mc+"\nCANCEL Pro :\n"+md+"\nPro Gname :\n"+me+"\nPro Invite :\n"+mf+"\nTotal [ %s ] Mode protection is being Maintained\n[ www.finbot.eu ]" %(str(len(bot_run["Pro_Qr"])+len(bot_run["Pro_Member"])+len(bot_run["Pro_Join"])+len(bot_run["Pro_Cancel"])+len(bot_run["pname"])+len(bot_run["Pro_Invite"]))))

                        elif cmd == "allbots" or cmd == 'listbot':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                ma = ""
                                a = 0
                                for m_id in run_bot["assist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                kang.sendMessage(msg.to,"\n"+ma+"\nTotal %s AllBots" %(str(len(bot_run["assist"]))))
                        elif cmd.startswith("logininduk "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["00"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("logintalk "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["0"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("login1 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["1"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("login2 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["2"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("login3 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["3"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("login4 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["4"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("login5 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["5"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("logink1 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["k1"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif cmd.startswith("logink2 "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   run_bot["k2"] = str(key).lower()
                                   kang.sendMessage(to, "Updated to: {}".format(str(key).lower()))
                        elif 'induk login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('induk login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["kang"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'mylogin: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('mylogin: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["fino"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif 'bot1 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('bot1 login: ','')
                              if spl in [""," ","\n",None]:
                                  fn1.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["fino1"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  fn1.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'bot2 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('bot2 login: ','')
                              if spl in [""," ","\n",None]:
                                  fn2.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["fino2"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  fn2.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'bot3 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('bot3 login: ','')
                              if spl in [""," ","\n",None]:
                                  fn3.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["fino3"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  fn3.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'bot4 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('bot4 login: ','')
                              if spl in [""," ","\n",None]:
                                  fn4.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["fino4"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  fn4.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'bot5 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('bot5 login: ','')
                              if spl in [""," ","\n",None]:
                                  fn5.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["fino5"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  fn5.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'kicker1 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('kicker1 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["kicker1"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'kicker2 login: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('kicker2 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["kicker2"]["AuthToken"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"[ {} ]".format(str(spl)))
                        elif 'reload la: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('reload la: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["RELOAD"]["X-LineAccess"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif 'reload ua: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('reload ua: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["RELOAD"]["User-Agent"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif 'la chrome: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('la chrome: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["CHROMEOS"]["LA"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif 'ua chrome: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('ua chrome: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["CHROMEOS"]["UA"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif 'la mac: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('la mac: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["DESKTOPMAC"]["LA"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif 'ua mac: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('ua mac: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendReplyMessage(msg_id,to,fail())
                              else:
                                  run_bot["DESKTOPMAC"]["UA"] = spl
                                  with open('logged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendReplyMessage(msg_id,to,up()+"{}".format(str(spl)))
                        elif cmd == 'auth mac' or cmd == "desktopmac":
                           if sender in Master or sender in admin or sender in kangyat:
                              client = DESKTOPMAC(FINBOT_AUTH_QUERY_PATH_FIR, None, code_resembler.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName=system)
                              uri = "line://au/q/" + qr.verifier
                              kang.sendMessage(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA,'X-Line-Application': LA,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = DESKTOPMAC(FINBOT_AUTH_QUERY_PATH, None, algorithm.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = DESKTOPMAC(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, code_resembler.Client)
                              kang.sendMessage(to,"Login succes.. Please check your msg setting before,  Turn off your letter sealing.. Look up your inbox")
                              kang.sendText(sender,str(res.authToken))
                        elif cmd == 'auth chrome' or cmd == "chromeos":
                           if sender in Master or sender in admin or sender in kangyat:
                              client = CHROMEOS(FINBOT_AUTH_QUERY_PATH_FIR, None, code_resembler.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName=system)
                              uri = "line://au/q/" + qr.verifier
                              kang.sendMessage(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA1,'X-Line-Application': LA1,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = CHROMEOS(FINBOT_AUTH_QUERY_PATH, None, algorithm.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = CHROMEOS(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, code_resembler.Client)
                              kang.sendMessage(to,"Login succes.. Please check your msg setting before,  Turn off your letter sealing.. Look up your inbox")
                              kang.sendText(sender,str(res.authToken))
                        elif cmd == 'auth win' or cmd == "desktopwin":
                           if sender in Master or sender in admin or sender in kangyat:
                              client = DESKTOPWIN(FINBOT_AUTH_QUERY_PATH_FIR, None, code_resembler.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName=system)
                              uri = "line://au/q/" + qr.verifier
                              kang.sendMessage(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA2,'X-Line-Application': LA2,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = DESKTOPWIN(FINBOT_AUTH_QUERY_PATH, None, algorithm.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = DESKTOPWIN(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, code_resembler.Client)
                              kang.sendMessage(to,"Login succes.. Please check your msg setting before,  Turn off your letter sealing.. Look up your inbox")
                              kang.sendText(sender,str(res.authToken))
                        elif cmd == 'auth ios' or cmd == "ios":
                           if sender in Master or sender in admin or sender in kangyat:
                              client = IOS(FINBOT_AUTH_QUERY_PATH_FIR, None, code_resembler.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName=system)
                              uri = "line://au/q/" + qr.verifier
                              kang.sendMessage(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA3,'X-Line-Application': LA3,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = IOS(FINBOT_AUTH_QUERY_PATH, None, algorithm.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = IOS(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, code_resembler.Client)
                              kang.sendMessage(to,"Login succes.. Please check your msg setting before,  Turn off your letter sealing.. Look up your inbox")
                              kang.sendText(sender,str(res.authToken))
                        elif cmd == "win10":
                           if sender in Master or sender in admin or sender in kangyat:
                              client = WIN10(FINBOT_AUTH_QUERY_PATH_FIR, None, code_resembler.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName=system)
                              uri = "line://au/q/" + qr.verifier
                              kang.sendMessage(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA4,'X-Line-Application': LA4,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = WIN10(FINBOT_AUTH_QUERY_PATH, None, algorithm.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = WIN10(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, code_resembler.Client)
                              kang.sendMessage(to,"Login succes.. Please check your msg setting before,  Turn off your letter sealing.. Look up your inbox")
                              kang.sendText(sender,str(res.authToken))
                        elif cmd == 'clova' or cmd == "clovafriends":
                           if sender in Master or sender in admin or sender in kangyat:
                              client = CLOVAFRIENDS(FINBOT_AUTH_QUERY_PATH_FIR, None, code_resembler.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName=system)
                              uri = "line://au/q/" + qr.verifier
                              kang.sendMessage(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA5,'X-Line-Application': LA5,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = CLOVAFRIENDS(FINBOT_AUTH_QUERY_PATH, None, algorithm.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = CLOVAFRIENDS(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, code_resembler.Client)
                              kang.sendMessage(to,"Login succes.. Please check your msg setting before,  Turn off your letter sealing.. Look up your inbox")
                              kang.sendText(sender,str(res.authToken))

                        elif cmd == "creator" or cmd == 'owner':
                            if sender in Master or sender in kangyat:
                                kang.sendMessage(to,"╔═══════════\n║Creator \n║〘 ۝🄵🄸🄽 🄱🄾🅃۝ 〙\n╠═══════════\n║http://line.me/ti/p/~kangnur04\n╚═══════════")
                                kang.sendMessage(to, None, contentMetadata={'mid': finoMID}, contentType=13)
                        elif cmd == "add me" or cmd == 'bot add me':
                            if sender in Master or sender in kangyat or sender in admin:
                                fino.findAndAddContactsByMid(sender)
                                fino.getMention(to,"Add success @!",[sender])
                                kang.findAndAddContactsByMid(sender)
                                kang.getMention(to,"Add success @!",[sender])
                                fn1.findAndAddContactsByMid(sender)
                                fn1.getMention(to,"Add success @!",[sender])
                                fn2.findAndAddContactsByMid(sender)
                                fn2.getMention(to,"Add success @!",[sender])
                                fn3.findAndAddContactsByMid(sender)
                                fn3.getMention(to,"Add success @!",[sender])
                                fn4.findAndAddContactsByMid(sender)
                                fn4.getMention(to,"Add success @!",[sender])
                                fn5.findAndAddContactsByMid(sender)
                                fn5.getMention(to,"Add success @!",[sender])
                                k1.findAndAddContactsByMid(sender)
                                k2.findAndAddContactsByMid(sender)
                                kang.getMention(to,"Kicker Add success @!",[sender])

                        elif cmd == "addallbots":
                            if run["finbot"] == True:
                                if sender in Creator or sender in kangyat:
                                    add1 = [myMID, fn1MID, fn2MID, fn3MID, fn4MID, fn5MID, k1MID, k2MID]#fino=finoMID
                                    add2 = [finoMID, fn1MID, fn2MID, fn3MID, fn4MID, fn5MID, k1MID, k2MID]#kang=myMID
                                    add3 = [myMID,finoMID, fn2MID, fn3MID, fn4MID, fn5MID, k1MID, k2MID]#fn1=fn1MID
                                    add4 = [myMID, finoMID, fn1MID, fn3MID, fn4MID, fn5MID, k1MID, k2MID]#fn2=fn2MID
                                    add5 = [myMID, fn1MID, fn2MID, finoMID, fn4MID, fn5MID, k1MID, k2MID]#fn3=fn3MID
                                    add6 = [myMID, fn1MID, fn2MID, fn3MID, finoMID, fn5MID, k1MID, k2MID]#fn4=fn4MID
                                    add7 = [myMID, fn1MID, fn2MID, fn3MID, fn4MID, finoMID, k1MID, k2MID]#fn5=fn5MID
                                    for addcl in add1:
                                        fino.findAndAddContactsByMid(addcl)
                                        time.sleep(0.5)
                                    fino.sendMessage(to,"All Bots added")
                                    for addki in add2:
                                        kang.findAndAddContactsByMid(addki)
                                        time.sleep(0.5)
                                    kang.sendMessage(to,"All Bots added")
                                    for addkk in add3:
                                        fn1.findAndAddContactsByMid(addkk)
                                        time.sleep(0.5)
                                    fn1.sendMessage(to,"All Bots added")
                                    for addkc in add4:
                                        fn2.findAndAddContactsByMid(addkc)
                                        time.sleep(0.5)
                                    fn2.sendMessage(to,"All Bots added")
                                    for addkm in add5:
                                        fn3.findAndAddContactsByMid(addkm)
                                        time.sleep(0.5)
                                    fn3.sendMessage(to,"All Bots added")
                                    for addkb in add6:
                                        fn4.findAndAddContactsByMid(addkb)
                                        time.sleep(0.5)
                                    fn4.sendMessage(to,"All Bots added")
                                    for addkd in add7:
                                        fn5.findAndAddContactsByMid(addkd)
                                        time.sleep(0.5)
                                    fn5.sendMessage(to,"All Bots added")
                        elif cmd == "kicker addallbots":
                            if run["finbot"] == True:
                                if sender in Creator or sender in kangyat:
                                    addAll = [finoMID, myMID, fn1MID, fn2MID, fn3MID, fn4MID, fn5MID, k2MID]
                                    addAll2 = [finoMID, myMID, fn1MID, fn2MID, fn3MID, fn4MID, fn5MID, k1MID]
                                    for addk1 in addAll:
                                        k1.findAndAddContactsByMid(addk1)
                                        time.sleep(0.5)
                                    k1.sendText(sender,"All Bots added")
                                    for addk2 in addAll2:
                                        k2.findAndAddContactsByMid(addk2)
                                        time.sleep(0.5)
                                    k2.sendText(sender,"All Bots added")
                        elif "allbots add @" in msg.text:
                          if sender in Master or sender in kangyat:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        fino.findAndAddContactsByMid(str(mention['M']))
                                        kang.findAndAddContactsByMid(str(mention['M']))
                                        kang.sendMention(to,sender, "User added as friend")
                                        fn1.findAndAddContactsByMid(str(mention['M']))
                                        fn1.sendMention(to,sender, "User added as friend")
                                        fn2.findAndAddContactsByMid(str(mention['M']))
                                        fn2.sendMention(to,sender, "User added as friend")
                                        fn3.findAndAddContactsByMid(str(mention['M']))
                                        fn3.sendMention(to,sender, "User added as friend")
                                        fn4.findAndAddContactsByMid(str(mention['M']))
                                        fn4.sendMention(to,sender, "User added as friend")
                                        fn5.findAndAddContactsByMid(str(mention['M']))
                                        fn5.sendMention(to,sender, "User added as friend")
                                    except Exception as e:
                                        pass
                        elif cmd == "contact:on" or cmd == 'k on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["contact"] = True
                                bot_run["checkPost"] = False
                                bot_run["addContact"] = False
                                kang.sendMention(to,sender,on())
                        elif cmd == "contact:off" or cmd == 'k off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["contact"] = False
                                kang.sendMention(to,sender,off())
                        elif cmd == "bot add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = True
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                kang.sendMention(to,sender,intro())
                        elif cmd == "bot1 add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = True
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                fn1.sendMention(to,sender,intro())
                        elif cmd == "bot2 add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = True
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                fn2.sendMention(to,sender,intro())
                        elif cmd == "bot3 add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = True
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                fn3.sendMention(to,sender,intro())
                        elif cmd == "bot4 add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = True
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                fn4.sendMention(to,sender,intro())
                        elif cmd == "bot5 add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = True
                                bot_run["kickerAdd"] = False
                                fn5.sendMention(to,sender,intro())
                        elif cmd == "kicker add": 
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = True
                                kang.sendMention(to,sender,intro())
                        elif cmd == "tagall" or cmd == 'sepi':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               members = []
                               if msg.toType == 1:
                                   room = kang.getCompactRoom(to)
                                   members = [mem.mid for mem in room.contacts]
                               elif msg.toType == 2:
                                   group = kang.getCompactGroup(to)
                                   members = [mem.mid for mem in group.members]
                               else:
                                   return kang.sendReplyMessage(msg_id,to,fail())
                               if members:
                                   mentionMembers2(to, members)
                        elif cmd == "cek. " or cmd == 'crash':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               kang.sendMessage(to, None, contentMetadata={'mid': "ud108eea8074da128b9cd064a8a28e27a,'"}, contentType=13)
                        elif cmd == "dtstts":
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                               try:
                                   dayTime()
                               except:
                                   pass
                        elif cmd == "rm chat" or cmd == 'mychat':
                          if run["finbot"] == True:
                            if sender in Creator or sender in kangyat:
                               try:
                                   fino.removeAllMessages(alfino.param2)
                                   kang.sendMessage(to, "『 Done Boss 』")
                               except:
                                   pass
                        elif cmd == "delchat" or cmd == 'rechat':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               try:
                                   kang.removeAllMessages(alfino.param2)
                                   fn1.removeAllMessages(alfino.param2)
                                   fn2.removeAllMessages(alfino.param2)
                                   fn3.removeAllMessages(alfino.param2)
                                   fn4.removeAllMessages(alfino.param2)
                                   fn5.removeAllMessages(alfino.param2)
                                   kang.sendMessage(to, "『 Done Boss 』")
                               except:
                                   pass
                        elif cmd == "mykey":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               kang.sendMessage(to, "「Mykey」\n▪「 " + str(bot_run["keyCommand"]) + " 」")
                        elif cmd.startswith("setkey "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(to, "▪Gagal mengganti key")
                               else:
                                   bot_run["keyCommand"] = str(key).lower()
                                   kang.sendMessage(to, "「Setkey」\n▪「{}」".format(str(key).lower()))
                        elif cmd == "resetkey":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               bot_run["keyCommand"] = ""
                               kang.getMention(to, "Refreshing key\n@!", [sender])
                        elif cmd == "reboot":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               kang.getMention(to, "『 Finbot rebooting... 』\n@!", [sender])
                               bot_run["restartPoint"] = msg.to
                               restartBot()
                        elif cmd == "restart":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               eltime = time.time() - mulai
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               rest = "Restarting... \n" + "[ " + waktu(eltime) + " ]" + "\n[ {}".format(datetime.strftime(timeNow,'%Y-%m-%d')+ " ]")
                               fino.sendMessage(to,rest)
                               bot_run["restartPoint"] = msg.to
                               restart_program()
                        elif cmd == "runtime" or cmd == 'deploy':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               eltime = time.time() - mulai
                               bot_ = "╔═════════════"
                               bot_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               bot_ += "\n╠═════════════"
                               bot_ += "\n║『 Deploy Time 』"
                               bot_ += "\n║{}".format(waktu(eltime)) 
                               bot_ += "\n╚═════════════"
                               kang.sendMessage(to,str(bot_))
                        elif cmd == "listfriend" or cmd == 'temen':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = kang.getAllContactIds()
                               for i in gid:
                                   G = kang.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               kang.sendMessage(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")
                        elif cmd == 'f1temen':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = fn1.getAllContactIds()
                               for i in gid:
                                   G = fn1.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fn1.sendMessage(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")
                        elif cmd == 'f2temen':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = fn2.getAllContactIds()
                               for i in gid:
                                   G = fn2.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fn2.sendMessage(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")
                        elif cmd == 'f3temen':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = fn3.getAllContactIds()
                               for i in gid:
                                   G = fn3.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fn3.sendMessage(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")
                        elif cmd == 'f4temen':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = fn4.getAllContactIds()
                               for i in gid:
                                   G = fn4.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fn4.sendMessage(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")
                        elif cmd == 'f5temen':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = fn5.getAllContactIds()
                               for i in gid:
                                   G = fn5.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fn5.sendMessage(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")

                        elif cmd == "glink":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                if msg.toType == 2:
                                   x = kang.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      kang.updateGroup(x)
                                   gurl = kang.reissueGroupTicket(msg.to)
                                   kang.sendMessage(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║ http://line.me/R/ti/g/"+gurl + "\n╚═════════════")
                        elif cmd == "ourl":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                if msg.toType == 2:
                                   X = kang.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kang.updateGroup(X)
                                   kang.getMention(to, "『 Url opened 』\n@!", [sender])
                        elif cmd == "curl":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                if msg.toType == 2:
                                   X = kang.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kang.updateGroup(X)
                                   kang.getMention(to,"『 Url Closed 』\n@!", [sender])
                        elif cmd == "changefoto" or cmd == 'cft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["changePicture"] = True
                                kang.sendMention(to,sender,intro())
                        elif cmd == "kickerfoto" or cmd == 'k cft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["kickerPicture"] = True
                                kang.sendMention(to,sender,intro())
                        elif cmd == "coverfoto" or cmd == 'cvf':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["changePictureCover"] = True
                                kang.sendMention(to,sender,intro())
                        elif cmd == "cfotogroup" or cmd == 'cfg':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if msg.toType == 2:
                                bot_run["groupPicture"] = True
                                kang.sendMention(to,sender,intro())
                        elif cmd == 'finft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][finoMID] = True
                                fino.sendMention(to,sender,intro())
                        elif cmd == "updatefoto" or cmd == 'myft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][myMID] = True
                                kang.sendMention(to,sender,intro())
                        elif cmd == "f1cft" or cmd == 'f1ft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][fn1MID] = True
                                fn1.sendMention(to,sender,intro())
                        elif cmd == "f2cft" or cmd == 'f2ft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][fn2MID] = True
                                fn2.sendMention(to,sender,intro())
                        elif cmd == "f3cft" or cmd == 'f3ft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][fn3MID] = True
                                fn3.sendMention(to,sender,intro())
                        elif cmd == "f4cft" or cmd == 'f4ft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][fn4MID] = True
                                fn4.sendMention(to,sender,intro())
                        elif cmd == "f5cft" or cmd == 'f5ft':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["foto"][fn5MID] = True
                                fn5.sendMention(to,sender,intro())
                        elif cmd.startswith("finame: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fino.getProfile()
                                profile.displayName = string
                                fino.updateProfile(profile)
                                fino.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("cname: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.displayName = string
                                kang.updateProfile(profile)
                                kang.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("f1name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn1.getProfile()
                                profile.displayName = string
                                fn1.updateProfile(profile)
                                fn1.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("f2name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn2.getProfile()
                                profile.displayName = string
                                fn2.updateProfile(profile)
                                fn2.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("f3name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn3.getProfile()
                                profile.displayName = string
                                fn3.updateProfile(profile)
                                fn3.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("f4name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn4.getProfile()
                                profile.displayName = string
                                fn4.updateProfile(profile)
                                fn4.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("f5name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn5.getProfile()
                                profile.displayName = string
                                fn5.updateProfile(profile)
                                fn5.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("k1name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendText(Creator,"Genti nama beres boss... " + string)
                        elif cmd.startswith("k2name: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendText(Creator,"Genti nama beres boss... " + string)
                        elif cmd.startswith("allname: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile1 = fn1.getProfile()
                                profile2 = fn2.getProfile()
                                profile3 = fn3.getProfile()
                                profile4 = fn4.getProfile()
                                profile5 = fn5.getProfile()
                                profile.displayName = string
                                profile1.displayName = string
                                profile2.displayName = string
                                profile3.displayName = string
                                profile4.displayName = string
                                profile5.displayName = string
                                kang.updateProfile(profile)
                                fn1.updateProfile(profile1)
                                fn2.updateProfile(profile2)
                                fn3.updateProfile(profile3)
                                fn4.updateProfile(profile4)
                                fn5.updateProfile(profile5)
                                kang.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("cbio: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.statusMessage = string
                                kang.updateProfile(profile)
                                kang.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("allbio: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kang.getProfile()
                                profile1 = fn1.getProfile()
                                profile2 = fn2.getProfile()
                                profile3 = fn3.getProfile()
                                profile4 = fn4.getProfile()
                                profile5 = fn5.getProfile()
                                profile.statusMessage = string
                                profile1.statusMessage = string
                                profile2.statusMessage = string
                                profile3.statusMessage = string
                                profile4.statusMessage = string
                                profile5.statusMessage = string
                                kang.updateProfile(profile)
                                kang.sendReplyMessage(msg_id,to,up()+string)
                                fn1.updateProfile(profile1)
                                fn1.sendReplyMessage(msg_id,to,up()+string)
                                fn2.updateProfile(profile2)
                                fn2.sendReplyMessage(msg_id,to,up()+string)
                                fn3.updateProfile(profile3)
                                fn3.sendReplyMessage(msg_id,to,up()+string)
                                fn4.updateProfile(profile4)
                                fn4.sendReplyMessage(msg_id,to,up()+string)
                                fn5.updateProfile(profile5)
                                fn5.sendReplyMessage(msg_id,to,up()+string)
                        elif cmd.startswith("kbio: "):
                          if sender in Master or sender in kangyat:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile1 = k1.getProfile()
                                profile2 = k2.getProfile()
                                profile1.statusMessage = string
                                profile2.statusMessage = string
                                profile3.statusMessage = string
                                k1.updateProfile(profile1)
                                k1.sendReplyMessage(msg_id,to,up()+string)
                                k2.updateProfile(profile2)
                                k2.sendReplyMessage(msg_id,to,up()+string)

                        elif cmd == "byeme" or cmd == 'byebye':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                G = kang.getGroup(msg.to)
                                kang.sendMessage(to, "さようなら...!"+str(G.name))
                                kang.leaveGroup(msg.to)
                        elif cmd == "spres" or cmd == 'sprespon':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                get_profile_time_start = time.time()
                                get_profile = kang.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = kang.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = kang.getContact(myMID)
                                get_contact_time = time.time() - get_contact_time_start
                                kang.sendMessage(to, "╔═════════════\n║【Speed Respon】\n╠═══════════════\n║▪➣Get Profile\n║   %.10f\n╠═══════════════\n║▪➣Get Contact\n║   %.10f\n╠═══════════════\n║▪➣Get Group\n║   %.10f\n╚═══════════════" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               get_profile_time_start = time.time()
                               get_profile = kang.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               kang.getMention(to,"Speed acceleration...\n %.18f" % (get_profile_time/3)+ "\n@!",[sender])

                        elif cmd == "benchmark" or cmd == "spbot":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               get_profile_time_start1 = time.time()
                               get_profile = fn1.getProfile()
                               get_profile_time1 = time.time() - get_profile_time_start1
                               fn1.getMention(to,"Speed acceleration...\n %.18f" % (get_profile_time1/3)+ "\n@!",[sender])
                               
                               get_profile_time_start2 = time.time()
                               get_profile = fn2.getProfile()
                               get_profile_time2 = time.time() - get_profile_time_start2
                               fn2.getMention(to,"Speed acceleration...\n %.18f" % (get_profile_time2/3)+ "\n@!",[sender])
                               
                               get_profile_time_start3 = time.time()
                               get_profile = fn3.getProfile()
                               get_profile_time3 = time.time() - get_profile_time_start3
                               fn3.getMention(to,"Speed acceleration...\n %.18f" % (get_profile_time3/3)+ "\n@!",[sender])
                               
                               get_profile_time_start4 = time.time()
                               get_profile = fn4.getProfile()
                               get_profile_time4 = time.time() - get_profile_time_start4
                               fn4.getMention(to,"Speed acceleration...\n %.18f" % (get_profile_time4/3)+ "\n@!",[sender])
                               
                               get_profile_time_start5 = time.time()
                               get_profile = fn5.getProfile()
                               get_profile_time5 = time.time() - get_profile_time_start5
                               fn5.getMention(to,"Speed acceleration...\n %.18f" % (get_profile_time5/3)+ "\n@!",[sender])

                        elif cmd.startswith('gc '):
                          if sender in Master or sender in kangyat:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cname = kang.getContact(u).displayName
                                  cmid = kang.getContact(u).mid
                                  cstatus = kang.getContact(u).statusMessage
                                  cpic = kang.getContact(u).picturePath
                                  #print(str(a))
                                  kang.sendMessage(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                  kang.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                  if "videoProfile='{" in str(kang.getContact(u)):
                                      kang.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                  else:
                                      kang.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                              except Exception as e:
                                  kang.sendMessage(receiver, str(e))

                        elif ("Mek " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           G = kang.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           X = k2.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           k2.updateGroup(X)
                                           k1.leaveGroup(msg.to)
                                           k2.leaveGroup(msg.to)
                                       except:
                                           pass

                        elif ("hai " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           G = kang.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           k1.leaveGroup(msg.to)
                                           X = k2.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           k2.updateGroup(X)
                                           k2.leaveGroup(msg.to)
                                       except:
                                           pass

                        elif ("Dam " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           _Random.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("f1k " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           fn1.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("f2k " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           fn2.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("f3k " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           fn3.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("f4k " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           fn4.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("f5k " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           fn5.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "timer on":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              if wait["clock"] == True:
                                fino.sendMessage(to,'Bot in timing... ')
                              else:
                                wait["clock"] = True
                                tz = pytz.timezone("Asia/Jakarta")
                                now2 = datetime.now(tz=tz)
                                nowT = datetime.strftime(now2,"(%H:%M:%S)")
                                profile = fino.getProfile()
                                profile0 = kang.getProfile()
                                profile1 = fn1.getProfile()
                                profile2 = fn2.getProfile()
                                profile3 = fn3.getProfile()
                                profile4 = fn4.getProfile()
                                profile5 = fn5.getProfile()
                                profile.displayName = wait["cName"] + nowT
                                fino.updateProfile(profile)
                                profile0.displayName = wait["cName"] + nowT
                                kang.updateProfile(profile0)
                                profile1.displayName = wait["cName"] + nowT
                                fn1.updateProfile(profile1)
                                profile2.displayName = wait["cName"] + nowT
                                fn2.updateProfile(profile2)
                                profile3.displayName = wait["cName"] + nowT
                                fn3.updateProfile(profile3)
                                profile4.displayName = wait["cName"] + nowT
                                fn4.updateProfile(profile4)
                                profile5.displayName = wait["cName"] + nowT
                                fn5.updateProfile(profile5)
                                kang.sendMessage(to,"Timer on")

                        elif cmd == "timer off":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              if wait["clock"] == False:
                                kang.sendMessage(to,"Timer didn't sett up ... ")
                              else:
                                wait["clock"] = False
                                kang.sendMessage(to,"Turn off timer bot")
                        elif 'set timer: ' in msg.text:
                           if sender in Master:
                              z = msg.text.replace('set timer: ','')
                              if z in [""," ","\n",None]:
                                  kang.sendMessage(to, "Too long timer")
                              else:
                                  wait["cName"] = z
                                  kang.sendReplyMessage(msg_id,to,up()+" {}".format(str(z)))
                        elif cmd == "on time":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              if wait["clock"] == False:
                                kang.sendMessage(to,'Please sett your timer before ... ')
                              else:
                                wait["clock"] = True
                                tz = pytz.timezone("Asia/Jakarta")
                                now2 = datetime.now(tz=tz)
                                nowT = datetime.strftime(now2,"(%H:%M:%S)")
                                profile = fino.getProfile()
                                profile0 = kang.getProfile()
                                profile1 = fn1.getProfile()
                                profile2 = fn2.getProfile()
                                profile3 = fn3.getProfile()
                                profile4 = fn4.getProfile()
                                profile5 = fn5.getProfile()
                                profile.displayName = bot_run["cNf"] + nowT
                                fino.updateProfile(profile)
                                profile0.displayName = bot_run["cNk"] + nowT
                                kang.updateProfile(profile0)
                                profile1.displayName = bot_run["cNfn1"] + nowT
                                fn1.updateProfile(profile1)
                                profile2.displayName = bot_run["cNfn2"] + nowT
                                fn2.updateProfile(profile2)
                                profile3.displayName = bot_run["cNfn3"] + nowT
                                fn3.updateProfile(profile3)
                                profile4.displayName = bot_run["cNfn4"] + nowT
                                fn4.updateProfile(profile4)
                                profile5.displayName = bot_run["cNfn5"] + nowT
                                fn5.updateProfile(profile5)
                                fino.sendMessage(to,"Timer updated")
                                kang.sendMessage(to,"Timer updated")
                                fn1.sendMessage(to,"Timer updated")
                                fn2.sendMessage(to,"Timer updated")
                                fn3.sendMessage(to,"Timer updated")
                                fn4.sendMessage(to,"Timer updated")
                                fn5.sendMessage(to,"Timer updated")

                        elif cmd == "add contact:on" or text.lower() == 'add cont on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["addContact"] = True
                                bot_run["contact"] = False
                                bot_run["checkPost"] = False
                                kang.sendMention(to,sender,intro())

                        elif cmd == "autojoin on" or cmd == 'join on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["autoJoin"] = True
                                kang.sendMention(to,sender,on())
                        elif cmd == "autojoin off" or cmd == 'join off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["autoJoin"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "autoleave on" or cmd == 'leave on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["autoLeave"] = True
                                kang.sendMention(to,sender,on())
                        elif cmd == "autoleave off" or cmd == 'leave off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["autoLeave"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "autoadd on" or cmd == 'add on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["autoAdd"] = True
                                kang.sendMention(to,sender,on())
                        elif cmd == "autoadd off" or cmd == 'add off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["autoAdd"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "jointicket on" or cmd == 'ticket on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["Auto_Join_Ticket"] = True
                                kang.sendMention(to,sender,on())
                        elif cmd == "jointicket off" or cmd == 'ticket off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["Auto_Join_Ticket"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                                bot_run["wblacklist"] = True
                                bot_run["dblacklist"] = False
                                kang.sendMention(to,sender,intro())
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                                bot_run["dblacklist"] = True
                                bot_run["wblacklist"] = False
                                kang.sendMention(to,sender,intro())

                        elif cmd == "add admin:on" or cmd == 'add admin on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["addAdmin"] = True
                                bot_run["delAdmin"] = False
                                kang.sendMention(to,sender,intro())
                        elif cmd == "del admin:on" or text.lower() == 'delete admin on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["delAdmin"] = True
                                bot_run["addAdmin"] = False
                                kang.sendMention(to,sender,intro())

                        elif cmd == "invite on" or cmd == 'inv mem':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["invite"] = True
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                kang.sendMention(to,sender,intro())
                        elif cmd == "f1invite on" or cmd == 'f1inv':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["invite"] = False
                                bot_run["invite1"] = True
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                fn1.sendMention(to,sender,intro())
                        elif cmd == "f2invite on" or cmd == 'f2inv':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = True
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                fn2.sendMention(to,sender,intro())
                        elif cmd == "f3invite on" or cmd == 'f3inv':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = True
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                fn3.sendMention(to,sender,intro())
                        elif cmd == "f4invite on" or cmd == 'f4inv':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = True
                                bot_run["invite5"] = False
                                fn4.sendMention(to,sender,intro())
                        elif cmd == "f5invite on" or cmd == 'f5inv':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = True
                                fn5.sendMention(to,sender,intro())

                        elif cmd == "read on" or cmd == 'rd on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["AutoRead"] = True
                                bot_run["scanner"] = False
                                kang.sendMention(to,sender,on())
                        elif cmd == "read off" or cmd == 'rd off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                                bot_run["AutoRead"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "nyusup on" or cmd == 'nsp on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if bot_run['nyusup'] == True:
                                gid = fino.getGroupIdsJoined()
                                kang.sendMessage(to,' Spyer Bot has been set to read [ '+str(len(gid))+' ] link group notifications')
                              else:
                                gid = fino.getGroupIdsJoined()
                                bot_run["nyusup"] = True
                                kang.sendMention(to,sender,' Spyer Bot enabled for read [ '+str(len(gid))+' ] link Group notifications')
                        elif cmd == "nyusup off" or cmd == 'nsp off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if bot_run['nyusup'] == False:
                                kang.sendMessage(to,' No Spy Bot is set to read link group notifications')
                              else:
                                bot_run["nyusup"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "lock gname" or cmd == 'lgn':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              if to in bot_run['pname']:
                                kang.sendMessage(to,'Group name protection in remaining')
                              else:
                                bot_run['pname'][to] = True
                                bot_run['pro_name'][to] = kang.getGroup(to).name
                                kang.sendMention(to,sender,on())
                        elif cmd == "unlock gname" or cmd == 'ugn':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              if to not in bot_run['pname']:
                                kang.sendMessage(to,'Protect group name belum di sett tolol')
                              else:
                                del bot_run['pname'][to]
                                kang.sendMention(to,sender,off())

                        elif 'Proqr ' in msg.text:
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              txt = msg.text.replace('Proqr ','')
                              ginfo = kang.getGroup(to)
                              if txt == 'on':
                                  if to in bot_run['Pro_Qr']:
                                       kang.sendMessage(to, "Link Protection in remaining for: " + str(ginfo.name))
                                  else:
                                       bot_run['Pro_Qr'][to] = True
                                  kang.sendReplyMessage(msg_id,to,on() +': '+ str(ginfo.name))
                              elif txt == 'off':
                                    if to not in bot_run['Pro_Qr']:
                                         kang.sendMessage(to,'No Link protection for: '+str(ginfo.name))
                                    else:
                                         del bot_run['Pro_Qr'][to]
                                    kang.sendReplyMessage(msg_id,to,off() +': '+ str(ginfo.name))

                        elif 'Procancel ' in msg.text:
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              txt = msg.text.replace('Procancel ','')
                              ginfo = kang.getGroup(to)
                              if txt == 'on':
                                  if to in bot_run['Pro_Cancel']:
                                       kang.sendMessage(to, "Cancel Protection in remaining for: " + str(ginfo.name))
                                  else:
                                       bot_run['Pro_Cancel'][to] = True
                                  kang.sendReplyMessage(msg_id,to,on() +': '+ str(ginfo.name))
                              elif txt == 'off':
                                    if to not in bot_run['Pro_Cancel']:
                                         kang.sendMessage(to,'No cancel protection for: '+str(ginfo.name))
                                    else:
                                         del bot_run['Pro_Cancel'][to]
                                    kang.sendReplyMessage(msg_id,to,off() +': '+ str(ginfo.name))

                        elif 'Proinvite ' in msg.text:
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              txt = msg.text.replace('Proinvite ','')
                              ginfo = kang.getGroup(to)
                              if txt == 'on':
                                  if to in bot_run['Pro_Invite']:
                                       kang.sendMessage(to, "Invite Protection in remaining for: " + str(ginfo.name))
                                  else:
                                       bot_run['Pro_Invite'][to] = True
                                  kang.sendReplyMessage(msg_id,to,on() +': '+ str(ginfo.name))
                              elif txt == 'off':
                                    if to not in bot_run['Pro_Invite']:
                                         kang.sendMessage(to,'No invite protection for: '+str(ginfo.name))
                                    else:
                                         del bot_run['Pro_Invite'][to]
                                    kang.sendReplyMessage(msg_id,to,off() +': '+ str(ginfo.name))

                        elif 'Promember ' in msg.text:
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              txt = msg.text.replace('Promember ','')
                              ginfo = kang.getGroup(to)
                              if txt == 'on':
                                  if to in bot_run['Pro_Member']:
                                       kang.sendMessage(to, "Member Protection in remaining for: " + str(ginfo.name))
                                  else:
                                       bot_run['Pro_Member'][to] = True
                                  kang.sendReplyMessage(msg_id,to,on() +': '+ str(ginfo.name))
                              elif txt == 'off':
                                    if to not in bot_run['Pro_Member']:
                                         kang.sendMessage(to,'No member protection for: '+str(ginfo.name))
                                    else:
                                         del bot_run['Pro_Member'][to]
                                    kang.sendReplyMessage(msg_id,to,off() +': '+ str(ginfo.name))

                        elif 'Projoin ' in msg.text:
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              txt = msg.text.replace('Projoin ','')
                              ginfo = kang.getGroup(to)
                              if txt == 'on':
                                  if to in bot_run['Pro_Join']:
                                       kang.sendMessage(to, "Join Protection in remaining for: " + str(ginfo.name))
                                  else:
                                       bot_run['Pro_Join'][to] = True
                                  kang.sendReplyMessage(msg_id,to,on() +': '+ str(ginfo.name))
                              elif txt == 'off':
                                    if to not in bot_run['Pro_Join']:
                                         kang.sendMessage(to,'No join protection for: '+str(ginfo.name))
                                    else:
                                         del bot_run['Pro_Join'][to]
                                    kang.sendReplyMessage(msg_id,to,off() +': '+ str(ginfo.name))

                        elif 'Proimg ' in msg.text:
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              txt = msg.text.replace('Proimg ','')
                              ginfo = kang.getGroup(to)
                              if txt == 'on':
                                  if to in bot_run['Pro_Gimage']:
                                       kang.sendMessage(to, "Image Protection in remaining for: " + str(ginfo.name))
                                  else:
                                       bot_run['Pro_Gimage'][to] = True
                                  kang.sendReplyMessage(msg_id,to,on() +': '+ str(ginfo.name))
                              elif txt == 'off':
                                    if to not in bot_run['Pro_Gimage']:
                                         kang.sendMessage(to,'No image protection for: '+str(ginfo.name))
                                    else:
                                         del bot_run['Pro_Gimage'][to]
                                    kang.sendReplyMessage(msg_id,to,off() +': '+ str(ginfo.name))

                        elif cmd == "block:on" or cmd == 'block on':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if bot_run['autoBlock'] == True:
                                kang.sendMessage(to,'auto block user already actived')
                              else:
                                bot_run["autoBlock"] = True
                                kang.sendMention(to,sender,on())
                        elif cmd == "block:off" or cmd == 'block off':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if bot_run['autoBlock'] == False:
                                kang.sendMessage(to,'Auto block nya belum di sett boss')
                              else:
                                bot_run["autoBlock"] = False
                                kang.sendMention(to,sender,off())

                        elif cmd == "pro all on" or cmd == 'protect all on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                                bot_run["Pro_Qr"][to] = True
                                bot_run["Pro_Invite"][to] = True
                                bot_run["Pro_Cancel"][to] = True
                                bot_run["Pro_Member"][to] = True
                                bot_run["Pro_Join"][to] = True
                                bot_run["pname"][to] = True
                                bot_run["Pro_Gimage"][to] = True
                                kang.sendMention(to,sender,on())
                        elif cmd == "pro all off" or cmd == 'protect all off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                                kang.sendMention(to,sender,off())
                                del bot_run["Pro_Qr"][to]
                                del bot_run["Pro_Invite"][to]
                                del bot_run["Pro_Cancel"][to]
                                del bot_run["Pro_Member"][to]
                                del bot_run["Pro_Join"][to]
                                del bot_run["pname"][to]
                                del bot_run["Pro_Gimage"][to]
                                with open('finbot1.json', 'w') as fp:
                                	json.dump(bot_run, fp, sort_keys=True, indent=4)
                        elif cmd == "gruplist":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                               ma = ""
                               a = 0
                               gid = kang.getGroupIdsJoined()
                               for i in gid:
                                   G = kang.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â  " + str(a) + ". " +G.name+ "\n"
                               kang.sendMessage(msg.to,"[ GROUP LIST ]\n\n"+ma+"badala\n[ Total"+str(len(gid))+"Groups ]")

                        elif cmd.startswith("infogrup "):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              separate = text.split(" ")
                              number = text.replace(separate[0] + " ","")
                              groups = kang.getGroupIdsJoined()
                              ret_ = ""
                              try:
                                  group = groups[int(number)-1]
                                  G = kang.getGroup(group)
                                  try:
                                      gCreator = G.creator.displayName
                                  except:
                                      gCreator = "Tidak ditemukan"
                                  if G.invitee is None:
                                      gPending = "0"
                                  else:
                                      gPending = str(len(G.invitee))
                                  if G.preventedJoinByTicket == True:
                                      gQr = "Tertutup"
                                      gTicket = "Tidak ada"
                                  else:
                                      gQr = "Terbuka"
                                      gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                  timeCreated = []
                                  timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                  ret_ += "Group Info "
                                  ret_ += "\nmmm: {}".format(G.name)
                                  ret_ += "\nID Group : {}".format(G.id)
                                  ret_ += "\nPembuat : {}".format(gCreator)
                                  ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                  ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                  ret_ += "\nJumlah Pending : {}".format(gPending)
                                  ret_ += "\nGroup Qr : {}".format(gQr)
                                  ret_ += "\nGroup Ticket : {}".format(gTicket)
                                  ret_ += "\nPicture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                  ret_ += ""
                                  kang.sendMessage(to, str(ret_))
                                  kang.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                              except:
                                  pass
                        elif cmd.startswith("autorestart: "):
                          if run["finbot"] == True:
                           if sender in Master or sender in kangyat:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["timeRestart"] = num
                                kang.sendReplyMessage(msg_id,to,up()+strnum)
                        elif cmd.startswith("open "):
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              separate = text.split(" ")
                              number = text.replace(separate[0] + " ","")
                              groups = kang.getGroupIdsJoined()
                              ret_ = ""
                              try:
                                  group = groups[int(number)-1]
                                  G = kang.getGroup(group)
                                  G.preventedJoinByTicket = False
                                  kang.updateGroup(G)
                                  try:
                                      gCreator = G.creator.mid
                                      dia = kang.getContact(gCreator)
                                      zx = ""
                                      zxc = ""
                                      zx2 = []
                                      xpesan = 'Sukses Open Qr Creator :  '
                                      diaa = str(dia.displayName)
                                      pesan = ''
                                      pesan2 = pesan+"@a\n"
                                      xlen = str(len(zxc)+len(xpesan))
                                      xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                      zx2.append(zx)
                                      zxc += pesan2
                                  except:
                                      gCreator = "Tidak ditemukan"
                                  if G.invitee is None:
                                      gPending = "0"
                                  else:
                                      gPending = str(len(G.invitee))
                                  if G.preventedJoinByTicket == True:
                                      gQr = "Tertutup"
                                      gTicket = "Tidak ada"
                                  else:
                                      gQr = "Terbuka"
                                      gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                  timeCreated = []
                                  timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                  ret_ += xpesan+zxc
                                  ret_ += "Nama : {}".format(G.name)
                                  ret_ += "\nGroup Qr : {}".format(gQr)
                                  ret_ += "\nPendingan : {}".format(gPending)
                                  ret_ += "\nGroup Ticket : {}".format(gTicket)
                                  ret_ += ""
                                kang.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass
                        elif cmd.startswith("limiter: "):
                          if run["finbot"] == True:
                           if sender in Master or sender in kangyat:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limiter"]["members"] = num
                                kang.sendReplyMessage(msg_id,to,up()+strnum)
                        elif 'Set pesan: ' in msg.text:
                           if sender in Master or sender in kangyat:
                              spl = msg.text.replace('Set pesan: ',"")
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(to, "Something went wrong!")
                              else:
                                  bot_run["message"] = spl
                                  kang.sendReplyMessage(msg_id,to,up()+"「{}」".format(str(spl)))

                        elif cmd == "cek limit":
                            if sender in Master or sender in kangyat:
                               kang.sendMessage(to, "Total Limiter [ " + str(bot_run["limiter"]["members"]) + " ]" +"\n\nSpamtag limiter [ " + str(bot_run["limitTag"]) + " ]" + "\n\nSpamcall limiter [ " + str(bot_run["limitCall"]) + " ]" )
                        elif cmd == "cek pesan":
                            if sender in Master or sender in kangyat:
                               kang.sendMessage(to, "「Pesan Msg」\nPesan Msg:\n\n「 " + str(bot_run["message"]) + " 」")
                        elif cmd == "cek autorestart":
                            if sender in Master or sender in kangyat:
                               kang.sendMessage(to, "「Autorestart」:\n\nIn remaining time:「 " + str(bot_run["timeRestart"]) + " /scnds」")
                        elif cmd == "my token":
                            if sender in Master or sender in kangyat:
                               fino.sendMessage(to, "[ Here's your token ]\n" + str(run_bot["fino"]["AuthToken"]))
                        elif cmd == "induk token":
                            if sender in Master or sender in kangyat:
                               kang.sendMessage(to, "[ Here's finbot token ]\n" + str(run_bot["kang"]["AuthToken"]))
                        elif cmd == "bot1 token":
                            if sender in Master or sender in kangyat:
                               fn1.sendMessage(to, "[ Here's bot1 token ]\n" + str(run_bot["fino1"]["AuthToken"]))
                        elif cmd == "bot2 token":
                            if sender in Master or sender in kangyat:
                               fn2.sendMessage(to, "[ Here's bot2 token ]\n" + str(run_bot["fino2"]["AuthToken"]))
                        elif cmd == "bot3 token":
                            if sender in Master or sender in kangyat:
                               fn3.sendMessage(to, "[ Here's bot3 token ]\n" + str(run_bot["fino3"]["AuthToken"]))
                        elif cmd == "bot4 token":
                            if sender in Master or sender in kangyat:
                               fn4.sendMessage(to, "[ Here's bot4 token ]\n" + str(run_bot["fino4"]["AuthToken"]))
                        elif cmd == "bot5 token":
                            if sender in Master or sender in kangyat:
                               fn5.sendMessage(to, "[ Here's bot5 token ]\n" + str(run_bot["fino5"]["AuthToken"]))

                        elif ('pro admin 'in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                               	if target in run_bot["Admin"]:
                                   	bl = kang.getContact(target).displayName
                                   	kang.sendMessage(to,bl+': This user is an admin')
                               	else:
                                       try:
                                           run_bot["Admin"][target] = True
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                           kang.sendReplyMessage(msg_id,to,fositive())
                                       except:
                                           pass
                        elif ('rm admin 'in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                               	if target not in run_bot["Admin"]:
                                   	bl = kang.getContact(target).displayName
                                   	kang.sendMessage(to,bl+': This user is Not an admin')
                               	else:
                                       try:
                                           del run_bot["Admin"][target]
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                           kang.sendReplyMessage(msg_id,to,negative())
                                       except:
                                           pass
                        elif cmd == "adminlist" or text.lower() == 'admin list':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if run_bot["Admin"] == {}:
                                kang.sendReplyMessage(msg_id,to,List())
                              else:
                                ma = ""
                                a = 0
                                for m_id in run_bot["Admin"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                kang.sendMessage(msg.to," Adminlist\n\n"+ma+"\nTotal [ %s ] Admin User" %(str(len(run_bot["Admin"]))))
                        elif cmd == "admin cont":
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if run_bot["Admin"] == {}:
                                    kang.sendReplyMessage(msg_id,to,List())
                              else:
                                    ma = ""
                                    for i in run_bot["Admin"]:
                                        ma = kang.getContact(i)
                                        kang.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "remove admin" or cmd == 'clear  admin':
                          if run["finbot"] == True:
                            if sender in Master or sender in kangyat:
                              if run_bot["Admin"] == {}:
                                    kang.sendReplyMessage(msg_id,to,List())
                              else:
                                    ragets = kang.getContacts(run_bot["Admin"])
                                    mc = "「%i」User Admin" % len(ragets)
                                    kang.sendReplyMessage(msg_id,to,negative()+mc)
                                    run_bot["Admin"] = {}

                        elif ('banned 'in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                               	if target in bot_run["Blacklist_User"]:
                                   	bl = kang.getContact(target).displayName
                                   	kang.sendMessage(to,bl+': This user is a blacklist')
                               	else:
                                       try:
                                           bot_run["Blacklist_User"][target] = True
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                           kang.sendReplyMessage(msg_id,to,Bl())
                                       except:
                                           pass
                        elif ('unban ' in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                               	if target not in bot_run["Blacklist_User"]:
                                   	bl = kang.getContact(target).displayName
                                   	kang.sendMessage(to,bl+': This user is Not a blacklist')
                               	else:
                                       try:
                                           del bot_run["Blacklist_User"][target]
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                           kang.sendReplyMessage(msg_id,to,dBL())
                                       except:
                                           pass
                        elif cmd == "banlist" or cmd == 'bn':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              if bot_run["Blacklist_User"] == {}:
                                kang.sendReplyMessage(msg_id,to,List())
                              else:
                                ma = ""
                                a = 0
                                for m_id in bot_run["Blacklist_User"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "│ " +kang.getContact(m_id).displayName + "\n"
                                kang.sendMessage(to,"╭─「 Banned List 」─\n"+ma+"\n╰──────────\nTotal「%s」Blacklist User" %(str(len(bot_run["Blacklist_User"]))))
                        elif cmd == "dbn" or cmd == 'clearban':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              if bot_run["Blacklist_User"] == {}:
                                    kang.sendReplyMessage(msg_id,to,List())
                              else:
                                    ragets = kang.getContacts(bot_run["Blacklist_User"])
                                    mc = "「%i」User Blacklist" % len(ragets)
                                    kang.sendReplyMessage(msg_id,to,negative()+mc)
                                    bot_run["Blacklist_User"] = {}

                        elif cmd == "blc" or cmd == 'blcontact':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin or sender in kangyat:
                              if bot_run["Blacklist_User"] == {}:
                                    kang.sendReplyMessage(msg_id,to,List())
                              else:
                                    ma = ""
                                    for i in bot_run["Blacklist_User"]:
                                        ma = kang.getContact(i)
                                        kang.sendMessage(to, None, contentMetadata={'mid': i}, contentType=13)

                        elif "/ti/g/" in msg.text.lower():
                          if run["finbot"] == True:
                            #if sender in Master or sender in kangyat:
                              if bot_run["Auto_Join_Ticket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     groups = fino.findGroupByTicket(ticket_id)
                                     fino.acceptGroupInvitationByTicket(groups.id,ticket_id)
                                     group = kang.findGroupByTicket(ticket_id)
                                     kang.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     group1 = fn1.findGroupByTicket(ticket_id)
                                     fn1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group2 = fn2.findGroupByTicket(ticket_id)
                                     fn2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     group3 = fn3.findGroupByTicket(ticket_id)
                                     fn3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group4 = fn4.findGroupByTicket(ticket_id)
                                     fn4.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     group5 = fn5.findGroupByTicket(ticket_id)
                                     fn5.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     _Random.inviteIntoGroup(alfino.param1,[KICKER])

        if alfino.type == 55:
            print('[ 55 ]')
            if alfino.param2 in bot_run["Blacklist_User"]:
                _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
            else:
                pass

        if alfino.type == 59:
            print(alfino)

    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
        	os.execl(sys.executable, sys.executable, *sys.argv)
    except KeyboardInterrupt:
        sys.exit('INTERRUPT')
    except Exception as error:
        logError(error)

while True:
    try:
        autoRestart()
        operations = main.singleTrace(count=50)
        if operations is not None:
            for alfino in operations:
                finbot(alfino)
                main.setRevision(alfino.revision)
    except Exception as e:
        logError(e)

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
        atexit.register(atend)

def atend1():
    with open("Log_data1.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
        atexit.register(atend1)
